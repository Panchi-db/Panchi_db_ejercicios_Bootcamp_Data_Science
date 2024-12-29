import alumnos_crud as alumnos

menu=  """WEB de ALUMN@S de la UNID.
            OPCIONES:
            1.- Listado completo de alumn@s
            2.- Listado de alumn@s por edad
            3.- Estado administrativo
            4.- Buscar almun@ por email
            5.- Alta nuev@ alumn@
            6.- Actualizar datos alumn@
            7.- Baja alumn@s
            8.- Eliminar alumnado
            9.- Salir de la WEB."""
            
            
            
            
            
            
while True:

    opcion = int(input(menu))
    match opcion:
        case 1:
            alumnos.lista_alumno ()
        
        case 2:
            alumnos.listado_edad ()
            
        case 3:
            alumnos.estado_administrativo()
            
        case 4:
            alumnos.busca_alumno()
                       
        case 5:
            alumnos.crea_alumno()
            
        case 6:
            alumnos.actualiza_alumno()
                
        case 7:
           alumnos.baja_alumno()
           
        case 8:
            alumnos.elimina_listado()
            
        case 9:
            print ("8.- Has salido de la WEB. \n    ¡Hasta pronto!.")
            break
             
        case _:
            print ("    ¡ERROR FATAL!\n    Elige otra opción.")
            break           