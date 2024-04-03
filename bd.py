import sql as sql

class Alumno():
    
    def datos(self,nombre="",apellidos="",edad=5,dni="", grado="",seccion =""):
        self.nombre=nombre
        self.apellidos=apellidos
        self.edad=edad
        self.dni=dni
        self.grado=grado
        self.seccion=seccion
    
    def nombre(self):
        return self.nombre
    def apellidos(self):
        return self.apellidos
    def edad(self):
        return self.edad
    def grado(self):
        return self.dni
    def dni(self):
        return self.grado
    def seccion(self):
        return self.seccion
    
    def validacion_nombre(self, nombre):
        self.nombre=nombre
    def validacion_apellidos(self, apellidos):
        self.apellidos=apellidos

    def validacion_edad(self,edad):
        if edad <5:
            print( "Alumno no presenta los requisitos de edad para nivel primario")
            self.edad=5
        else:
            self.edad=edad
            
            
    def validacion_dni(self):
        letras="qwertyuiopasdfghjklñmnbvcxz"
        if len(self.dni)!=9:
            print("DNI INCORRECTO , POR FAVOR INGRESE NUEVAMENTE")
            
            self.dni=""
        else:
            letras=self.dni[8]
            num=int(self.dni[8])
            if letras.upper()!=letras[num%23]:
                print("dni incorrecto")
                self.dni=""
    def dni_correcta(self,dni):
        self.dni=dni
        self.validacion_dni
        
    def validacion_grado(self,grado):
        if len(self.grado)!=7:
            print( "incorrecto" )
    def validacion_correcta_grado(self,grado):
        self.grado=grado
        self.validacion_grado
    def seccion(self,seccion):
        self.seccion=seccion
    def mostrar(self):
        
     return "Nombre:"+self.nombre+"Apellidos"+self.apellidos+"edad"+self.edad+"dni"+self.dni+"grado"+self.grado+"seccion"+self.seccion
                
   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        