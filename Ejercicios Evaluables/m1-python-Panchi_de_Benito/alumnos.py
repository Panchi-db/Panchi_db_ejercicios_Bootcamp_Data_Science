
#CREACIÓN CLASE ALUMNO

from datetime import datetime

class Alumnos:
    
    def __init__ (self, nombre, apellido, telefono, 
                  email, estudiante, not_med, f_cum):
        
        self.nombre= nombre
        self.apellido= apellido
        self.telefono= telefono
        self.email= email
        self.estudiante= estudiante
        self.not_med= not_med
        self.f_cum= datetime.strptime (f_cum, "%d/%m/%Y")
        print(" ")
    def calcular_edad (self):
        hoy = datetime.now()
        edad= hoy.year - self.f_cum.year
        if (hoy.month, hoy.day) < (self.f_cum.month, self.f_cum.day):
            edad-=1
        return edad
    def actualizar_alumno (self, dato, nuevo_dato):
        datos_actualizables= ["nombre", "apellido", "telefono", "email"]
        if dato in datos_actualizables:
            setattr(self, dato, nuevo_dato)
            print (f" El {dato} se ha actualizado a : {nuevo_dato}")
        else:
            print ("El dato no es actualizable")
    def __str__(self):
        return f"""Alumn@.-\n Nombre: {self.nombre} \n Apellido: {self.apellido} \n Teléfono: {self.telefono}\n Email: {self.email}\n Edad: {self.calcular_edad()} \n Estudiante: {self.estudiante} \n Nota media:{self.not_med} \n Cumpleños: {self.f_cum.strftime('%d/%m/%y')}\n  """
        
    def __repr__(self):
        return f" Alumn@s: (Nombre: {self.nombre}, Apellido: {self.apellido}, Teléfono: {self.telefono}, Email: {self.email}, Edad: {self.calcular_edad()}, Estudiante: {self.estudiante}, Nota media:{self.not_med} Cumpleaños: {self.f_cum.strftime('%d/%m/%y')})" 
    
