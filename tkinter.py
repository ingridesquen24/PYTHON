import tkinter as tk
from tkinter import ttk

def abrir_ventana_secundaria():
    # Crear una ventana secundaria.
    veterinaria= tk.Toplevel()
    veterinaria.geometry("100x100")
    veterinaria.configure(background="sky blue")
    veterinaria.title("FORMULARIO DE SINTOMAS ")



    label4=tk.Label(veterinaria ,text='Secreción ocular con apariencia acuosa',bg="pink")
    label4.pack(ipadx=10, ipady=10)
    label5=tk.Label(veterinaria ,text='Fiebre',bg="sky blue")
    label5.pack(ipadx=10, ipady=10)
    label6=tk.Label(veterinaria ,text='Descarga nasal',bg="pink")
    label6.pack(ipadx=10, ipady=10)
    label7=tk.Label(veterinaria ,text='Pérdida de apetito',bg="sky blue")
    label7.pack(ipadx=10, ipady=10)
    label8=tk.Label(veterinaria ,text='Vómito',bg="pink")
    label8.pack(ipadx=10, ipady=10)
    label9=tk.Label(veterinaria ,text='Diarrea',bg="sky blue")
    label9.pack(ipadx=10, ipady=10)
    label10=tk.Label(veterinaria ,text='deshidratacion',bg="pink")
    label10.pack(ipadx=10, ipady=10)
    label11=tk.Label(veterinaria ,text='Diarreas sanguinolentas',bg="sky blue")
    label11.pack(ipadx=10, ipady=10)
    label12=tk.Label(veterinaria ,text='Convulsiones',bg="pink")
    label12.pack(ipadx=10, ipady=10)
    label13=tk.Label(veterinaria ,text='HIPERTENSION',bg="sky blue")
    label13.pack(ipadx=10, ipady=10)
    label14=tk.Label(veterinaria ,text='Taquicardia',bg="pink")
    label14.pack(ipadx=10, ipady=10)
    label15=tk.Label(veterinaria ,text='Hipertemia',bg="sky blue")
    label15.pack(ipadx=10, ipady=10)
    
    label16=tk.Label(veterinaria ,text='deshidratacion',bg="pink")
    label16.pack(ipadx=10, ipady=10)
    
    boton_cerrar = ttk.Button(
       veterinaria,
        text="SALIR", 
        command=veterinaria.destroy
       )
       
   

    boton_cerrar.place(x=75, y=75)
    boton_cerrar.pack()
    
    

# Crear la ventana principal.
ventana_principal = tk.Tk()
ventana_principal.config(width=100, height=100)
ventana_principal.geometry("700x700")


ventana_principal.title("CLINICA VETERINARIA  VET PET")
ventana_principal.configure(background="SKY BLUE")
label =tk.Label(ventana_principal, text='DNI',bg="pink")
label.pack(ipadx=10, ipady=10)
entry = tk.Entry()
entry.place(x=50, y=50)
entry.pack()
label2 =tk.Label(ventana_principal, text='NOMBRE DE MASCOTA',bg="pink")
label2.pack(ipadx=10, ipady=10)
entry2 = tk.Entry()
entry2.place(x=50, y=50)
entry2.pack()

boton_abrir = ttk.Button(
    
    ventana_principal,
    text="ACEPTAR",

    command=abrir_ventana_secundaria
)
boton_abrir.place(x=100, y=100)
boton_abrir.pack()
ventana_principal.mainloop()
#la funcion mainloop  es para quqe se muestre  el programa