from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'system') #¿Para qué sirve esta línea?

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.clock import Clock
from itertools import cycle

import random

Builder.load_file('design.kv')

class MyWidget(BoxLayout):
    random_number = StringProperty()
    string = StringProperty()
    if_label_text="Hello World!"

    def __init__(self):
        super(MyWidget, self).__init__()
        self.random_number = str(random.randint(1, 100))+'\n'
        self.listText = cycle(('Hola', 'soy', 'una', 'etiqueta'))
        Clock.schedule_interval(self.change_label_text, 0.6) #¿Para qué sirve esta línea?

    def numero_aleatorio(self):
        self.random_number += str(random.randint(1, 100))+'\n'

    def change_label_text(self, *args):
        self.string = next(self.listText)

class myApp(App):
    def build(self):
        return MyWidget()
    def on_pause(self): #¿Para qué sirve esta función?
        return True
    def on_resume(self): #¿Para que sirve esta función?
        pass
g = "Esto es un mensaje guardado en una variable" #Aquí está la variable que guarda el texto que quiero mostrar

if __name__ in ('__main__', '__android__'): #¿Para qué sirve esta línea?
    myApp().run()