from kivymd.app  import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'system')
from kivy.lang import Builder
class ui(ScreenManager):
    
    pass
class MainApp(MDApp):
    def build(Self):
        Self.theme_cls.theme_style="Dark"
        Self.theme_cls.theme_palette="Teal"
        Builder.load_file('design.kv')
        
        
        return ui()
    def change_style(self,checked,value):
        
        if value:
            self.theme_cls.theme_style="Dark"
        else:
            self.theme_cls.theme_style="Light"
if __name__=="__main__":
    MainApp().run()
 