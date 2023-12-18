import os
alumnos =[] #esto es una lista vacia
isActive =True
menu = "1. Registrar alumno\n2. Registrar notas\n3. Salir\n:)"
subMenuNotas = ["Parciales","Quices","Trabajos","Regresar al menu principal"]
opMenu = 0
while (isActive) :
    os.system("cls")
    try:
        opMenu =int(input(menu))
    except ValueError: 
        print("Error en el dato de ingreso")
        os.system("pause")
    else: 
        if(opMenu==1):
            pass
        elif (opMenu==2):
            opNotas=0 #es una variable local al if(estrurctura condicional 2)
            isActiveGrades =True 
            while(isActiveGrades):
                os.system("cls")
                for i,item in enumerate(subMenuNotas):
                    print(f"{i+1}.{item}")  
                try:
                    opNotas = int(input(":)"))
                except ValueError:
                        print("Error en el dato de ingreso")
                        os.system("pause")
                else: 
                    if(opNotas==1):
                        pass
                    elif (opNotas==2):
                        pass
                    elif (opNotas==3):
                        pass
                    elif (opNotas==4):
                        isActiveGrades=False
                    else:
                        pass
        elif(opMenu==3):
            os.system("cls")
            print("Gracias por usar nuestro sistema")
            isActive=False
        else: 
            os.system("cls")
            print("opción inválida")
    os.system("pause")
