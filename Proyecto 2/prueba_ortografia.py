import os
import sys
import time
import ayudante_ortografico as ao
from colorama import Cursor, init, Fore, Style, Back
init()

def err_ao():
    print(Fore.RED + Back.WHITE + Style.BRIGHT + "Todavía no ha sido creado un ayudante ortográfico" + Fore.RESET + Back.RESET)
    time.sleep(2)
    os.system ("clear")      

def archivo_selecc():
    c = 0
    with os.scandir() as ficheros:
        ficheros = sorted([fichero.name for fichero in ficheros if fichero.is_file()])
    print("\n\nEn su directorio actual se encuentran los siguientes archivos:\n")
    for i in ficheros:
        print("{}: {}".format(c, i))
        c += 1
    return ficheros

help_o = None
guar_dicc = []
crear = False
crear_dicc = False
while True:
    print("1. Crear ayudante ortográfico")
    print("2. Cargar diccionario ")
    print("3. Eliminar palabra ")
    print("4. Corregir texto")
    print("5. Mostrar diccionario")
    print("6. Salir de aplicación")
    N = int(input("Elija una opción "))
    if N == 1:
        if crear is False:
            help_o = ao.crearAyudante()
            print(Fore.GREEN + Back.WHITE + Style.BRIGHT + "Se ha creado un ayudante ortográfico" + Fore.RESET + Back.RESET)
            crear = True
            time.sleep(1.2)
            os.system ("clear")
        else:
            print(Fore.RED + Back.WHITE + Style.BRIGHT + "Ya existe un ayudante ortográfico" + Fore.RESET + Back.RESET)
            time.sleep(1.8)
            os.system ("clear")

    elif N == 2:
        if help_o is None:
            err_ao() 
        else:
            
            while True:    
                lista_archivo = archivo_selecc()
                print("00: Regresar a menu principal")
                diccionario = int(input("Elija el diccionario que desea cargar "))
                if diccionario == 00:
                    os.system ("clear")
                    break

                if (lista_archivo[diccionario]  not in guar_dicc and 0 <= diccionario < len(lista_archivo)):
                    guar_dicc.append(lista_archivo[diccionario])
                    help_o.cargarDiccionario(lista_archivo[diccionario])
                    crear_dicc = True
                    print(Fore.GREEN + Back.WHITE + Style.BRIGHT +"Se ha cargado un diccionario" + Fore.RESET + Back.RESET)
                    od = int(input("¿Desea cargar otro diccionario? 1. Si 2. No "))
                    if od == 1:
                        pass
                    elif od == 2:
                        os.system ("clear")
                        break
                    else:
                        print(Fore.RED + Back.WHITE + Style.BRIGHT +"Opción no válida" + Fore.RESET + Back.RESET)                
                else:
                    print(Fore.RED + Back.WHITE + Style.BRIGHT + "El diccionario elegido ya está cargado" + Fore.RESET + Back.RESET)
                    mostrar_dicc = int(input("Desea ver los diccionarios cargados 1. Si 2. No "))
                    if mostrar_dicc == 1:
                        print(guar_dicc)
                        enter = input("Presione enter para continuar...")
                    elif mostrar_dicc == 2:
                        pass
                    else:
                        print(Fore.RED + Back.WHITE + Style.BRIGHT + "Opción no válida" + Fore.RESET + Back.RESET)

                os.system ("clear")
    elif N == 3:
        if help_o is None:
            err_ao() 
        else:        
            if crear_dicc is True:
                palabra = input("Ingrese la palabra que desea eliminar ")
                borrar = help_o.borrarPalabra(palabra)
                if borrar is True:
                    print(Fore.GREEN + Back.WHITE + Style.BRIGHT + "Palabra eliminada: {}".format(palabra) + Fore.RESET + Back.RESET)
                    time.sleep(1.8)
                    os.system ("clear")
                elif borrar is None:
                    print(Fore.RED + Back.WHITE + Style.BRIGHT + "Palabra no está en diccionario" + Fore.RESET + Back.RESET)
                    time.sleep(1.8)
                    os.system ("clear")
            else:
                print(Fore.RED + Back.WHITE + Style.BRIGHT + "Aún no ha cargado un diccionario" + Fore.RESET + Back.RESET)
                time.sleep(1.8)
                os.system ("clear")

    elif N == 4:
        if help_o is None:
            err_ao() 
        else:
            if crear_dicc is False:
                print(Fore.RED + Back.WHITE + Style.BRIGHT + "No se ha cargado diccionario" + Fore.RESET + Back.RESET)
                time.sleep(1.8)
                os.system ("clear")      
            else:    
                while True:    
                    lista_archivo = archivo_selecc()
                    print("00: Regresar a menu principal")
                    texto = int(input("Elija el texto que desea corregir "))
                    if texto == 00:
                        os.system ("clear")
                        break
                    salida = help_o.corregirTexto(lista_archivo[texto])
                    print(Fore.GREEN + Back.WHITE + Style.BRIGHT +"Se generó el archivo: {}".format(salida) + Fore.RESET + Back.RESET)
                    time.sleep(3)
                    os.system ("clear")

    elif N == 5:      
        if help_o is None:
            err_ao()       
        else:
            if crear_dicc is False:
                print(Fore.RED + Back.WHITE + Style.BRIGHT + "No se ha cargado diccionario" + Fore.RESET + Back.RESET)
                time.sleep(1.8)
                os.system ("clear")      
            else:       
                help_o.mostrar()
                continuar = input("Presione cualquier tecla para continuar...")
                os.system ("clear")

    elif N == 6:
        if os.name == "posix":
            print("===", os.name, "===")
            sys.exit()
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            pass
    else:
        print(Fore.RED + Back.WHITE + Style.BRIGHT + "Opción no válida" + Fore.RESET + Back.RESET)
        time.sleep(1.2)
        os.system ("clear")