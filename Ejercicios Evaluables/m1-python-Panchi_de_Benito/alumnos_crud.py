from alumnos import Alumnos

alumnos= [Alumnos ("Iluminada", "Blanco", "555689798", "iblan@unid.org", True, 6.6, "1/3/2001"),
 Alumnos ("Juan", "Valdez", "555987465","juanva@unid.org", True, 7.9, "4/1/1995"),
Alumnos ("Sinesio", "Delgado", "555987456", "side@unid.org", True, 8.8, "5/1/2002"),
Alumnos ("Begoña", "Parada", "555111234", "bepa@unid.org", False, 5.1,"6/1/1986")]


def lista_alumno ():
    print ("Listado alumn@s")
    for alumno in alumnos:
        print (f" {alumno}")
    if not alumnos:
        print ("No existen alumn@s.")
        print ("\n") 
            
def listado_edad ():
    print ("Alumn@s por edad")
    alumnos_por_edad= sorted(alumnos, key= lambda alumno : alumno.f_cum)
    for alumno in alumnos_por_edad:
        print (alumno)
        
def estado_administrativo():
    print ("Estado Administrativo")
    for alumno in alumnos:
        if alumno.estudiante:
            print (f"{alumno.nombre} {alumno.apellido}: Alta")
        else:
            print( f"{alumno.nombre} {alumno.apellido}: Baja")
            print("\n")
            break
        
def busca_alumno():
    print ("Búsqueda por email")
    email= input("Introduce un email:")
    found= False
    for alumno in alumnos:
        if email.lower() == alumno.email.lower():
            print(alumno)
            found= True
            print ("\n")
            break   #No consigo que haga el "break" cuando encuentra el email
        if not found:
            print ("El email no existe en la BBDD. Escríbelo bien:")
    print("\n")
    #break si lo pongo me dice que solo dentro de un loop JN si me deja
            
def crea_alumno():
    print("Alta alumn@")
    nombre= input("Introduce el nombre:")
    apellido= input("Introduce el apellido:")
    telefono= input("Introduce el teléfono: \n XXXXXXXXX")
    email= input("Introduce el email: ")
    not_med= float(input("Introduce la nota media:"))
    estudiante= bool(input("¿Está matriculad@? \n Opciones: True/False"))
    f_cum= input ("Introduce la fecha de nacimiento: \n Formto dd/mm/aaa")
    nuevo_alumno= Alumnos (nombre, apellido, telefono , email, estudiante, not_med, f_cum)
    alumnos.append(nuevo_alumno)
    print ("Alumn@ creado correctamente")
    print(nuevo_alumno)
    #break si funiona en JN
    
def actualiza_alumno():
    print ("Actualización datos administrativos")
    if not alumnos:
        print ("No hay alumn@s dados de alta")
    else:
        email= input("Introduce el email del alumn@ a actualizar")
        found= False
        for alumno in alumnos:
            if alumno.email.lower()== email.lower():
                found= True
                print(f" Alumno encontrado: \n {alumno}")
                dato= input("Para actualizar Nombre, escribe la plabra 'Nombre', no el nombre concreto. \n Igual con el resto de datos: 'Apellido', 'Teléfono' (sin acento), 'Email' que quieras actualizar: ").strip().lower()
                if dato in ["nombre", "apellido", "telefono", "email"]:
                    nuevo_dato= input("Nuevo dato:")
                    alumno.actualizar_alumno(dato, nuevo_dato)
                    print ("Dato actualizado correctamente:")
                    print(alumno)
                     
                else:
                    print(f" El dato {dato} no es modificable")
                    
def baja_alumno():
    print("Baja individual alumn@s")
    if not alumnos:
        print("No existen alumn@s")
    else:
        baja= input("Introduce el nombre del alumno: ").strip().lower()
        found= False
        for alumno in alumnos:
            if alumno.nombre.lower() == baja.lower():
                alumnos.remove(alumno)
                print (f" Alumn@ {alumno.nombre} {alumno.apellido} ha sido dado de baja")
                found= True
                
            if not found:
                print (f"No se ha encontrado al alumn@ {baja}")
                
            
def elimina_listado():
    print ("Borra listado")
    alumnos.clear()
    print ("""Todos los alumn@s han sido dad@s de baja correctamente.\n
           Para nuevo alta selecciona opción 4 y sigue las intrucciones.""")
                       
     