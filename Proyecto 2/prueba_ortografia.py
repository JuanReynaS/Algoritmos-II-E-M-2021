#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Descripción: En este módulo se despliega un menú que interactuá con ayudante 
#              ortográfico.
#
#             >./ python3 prueba_ortografia.py
#
# Creado por: Juan Reyna
# email: 10-10883@usb.ve
# version: 1.0


import os
import sys
import time
import ayudante_ortografico as ao
from colorama import init, Fore, Style, Back
import os.path as osp

init()


def clear():
    """ Procedimiento que limpia pantalla de acuerdo al sistema operativo
    """
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def err_ao():
    """ Mensaje de error en caso de ejecutar acción de cargar diccionario,
        borrar palabra, mostrar diccionario, corregir  sin crear ayudante
        ortográfico.
    """
    print(Fore.RED + Back.WHITE + Style.BRIGHT 
          + "Todavía no ha sido creado un ayudante ortográfico"
          + Fore.RESET + Back.RESET)
    time.sleep(2)
    clear()


help_o = None # Se convierte en un objeto de la clase ayudante ortográfico.
crear = False # Se vuelve True si se crea ayudante ortográfico.
crear_dicc = False #Se vuelve True si se ha cargado al menos un diccionario.

# Se crea un menú que interactúa con el ayudante ortográfico.
while True:
    try:    
        print("1. Crear ayudante ortográfico")
        print("2. Cargar diccionario ")
        print("3. Eliminar palabra ")
        print("4. Corregir texto")
        print("5. Mostrar diccionario")
        print("6. Salir de aplicación")
        
        N = int(input("Elija una opción ")) # N: Almacena la opción de menú
                                            #    elegida por usuario

        
        if type(N) != int or N < 1 or N > 6:

            print(Fore.RED + Back.WHITE + Style.BRIGHT
                  + "Debe seleccionar número entero entre 1 y 6"
                  + Fore.RESET + Back.RESET)
            
            time.sleep(1.5)
            clear()

        elif N == 1: # Opción 1: Crear ayudante ortográfico
            if crear is False:
                help_o = ao.crearAyudante()
                print(Fore.GREEN + Back.WHITE + Style.BRIGHT
                      + "Se ha creado un ayudante ortográfico"
                      + Fore.RESET + Back.RESET)
                crear = True
                time.sleep(1.2)
                clear()
            else:
                print(Fore.RED + Back.WHITE + Style.BRIGHT
                      + "Ya existe un ayudante ortográfico"
                      + Fore.RESET + Back.RESET)
                time.sleep(1.8)
                clear()

        elif N == 2: # Opción 2: Cargar diccionario
            if help_o is None:
                err_ao()
            else:
                
                while True:
                    clear()
                    men2 = "Indique la ruta de diccionario a agregar "
                    diccionario = input(men2)
                    
                    # salida: almacena el resultado de procesar archivo que se
                    #         intenta cargar como diccionario

                    salida = help_o.cargarDiccionario(diccionario)
                    
                    if salida is False: 
                        print(Fore.RED + Back.WHITE + Style.BRIGHT
                              + "Archivo seleccionado no es válido como diccionario"
                              + Fore.RESET + Back.RESET)
                        print(Fore.RED + Back.WHITE + Style.BRIGHT
                              + "Archivo no tiene una palabra válida por línea."
                              + Fore.RESET + Back.RESET)

                        time.sleep(1.8)
                        clear()

                    elif salida is True:
                        print(Fore.GREEN + Back.WHITE + Style.BRIGHT
                              + "Se ha cargado un diccionario"
                              + Fore.RESET
                              + Back.RESET)
                        
                        crear_dicc = True                
                                
                        men = "¿Desea cargar otro diccionario? 1. Si 2. No "
                        opc = int(input(men))
                        
                        if type(opc) != int or (opc < 1 or opc > 2):
                                   
                            print(Fore.GREEN + Back.WHITE + Style.BRIGHT
                                  + "Opción inválida"
                                  + Fore.RESET + Back.RESET) 
                                
                        elif opc == 1:
                            clear()
                        
                        elif opc == 2:
                            clear()
                            break


                    elif salida is None:
                            print(Fore.RED + Back.WHITE + Style.BRIGHT
                                  + "El diccionario elegido ya está cargado"
                                  + Fore.RESET + Back.RESET)

                            men1 = "Desea ver los diccionarios cargados 1. Si 2. No "
                            opc = int(input(men1))
                            
                            if (type(opc) != int or
                               (opc < 1 and opc > 2)):
                                   
                                print(Fore.RED + Back.WHITE + Style.BRIGHT
                                      + "Opción inválida"
                                      + Fore.RESET + Back.RESET) 

                            elif opc == 1:
                                print(help_o.guar_dicc)
                                enter = input("Presione Enter para continuar...")
                                
                            elif opc == 2:
                                pass
                                

                            men = "¿Desea cargar otro diccionario? 1. Si 2. No "
                            opc = int(input(men))
                            
                            if type(opc) != int or (opc < 1 or opc > 2):
                                       
                                print(Fore.GREEN + Back.WHITE + Style.BRIGHT
                                      + "Opción inválida"
                                      + Fore.RESET + Back.RESET) 
                                    
                            elif opc == 1:
                                clear()
                            
                            elif opc == 2:
                                clear()
                                break


                    else: # Archivo no es válido
                        print(Fore.RED + Back.WHITE + Style.BRIGHT
                              + str(salida) + Fore.RESET + Back.RESET)
                        time.sleep(1.8)
                        
                        men = "¿Desea cargar un diccionario? 1. Si 2. No "
                        opc = int(input(men))
                        
                        if type(opc) != int or (opc < 1 or opc > 2):
                                   
                            print(Fore.GREEN + Back.WHITE + Style.BRIGHT
                                  + "Opción inválida"
                                  + Fore.RESET + Back.RESET) 
                                
                        elif opc == 1:
                            clear()
                        
                        elif opc == 2:
                            clear()
                            break

        elif N == 3: # Opción 3: Eliminar palabra de diccionario
            if help_o is None:
                err_ao()
            else:
                # Se verifica que haya un diccionario creado
                if crear_dicc is True:                                       
                    palabra = input("Ingrese la palabra que desea eliminar ")
                    
                    # borrar: Almacena resultado de procesar palabra para
                    #         ser eliminada
                    borrar = help_o.borrarPalabra(palabra) 
                    if borrar is True:

                        print(Fore.GREEN + Back.WHITE + Style.BRIGHT
                              + "Palabra eliminada: {}".format(palabra)
                              + Fore.RESET + Back.RESET)

                        time.sleep(1.8)
                        clear()
                    elif borrar is None:

                        print(Fore.RED + Back.WHITE + Style.BRIGHT 
                              + "Palabra no está en diccionario"
                              + Fore.RESET + Back.RESET)

                        time.sleep(1.8)
                        clear()
                    elif borrar is False:

                        print(Fore.RED + Back.WHITE + Style.BRIGHT
                              + "Palabra no es válida"
                              + Fore.RESET + Back.RESET)

                        time.sleep(1.8)
                        clear()

                else:

                    print(Fore.RED + Back.WHITE + Style.BRIGHT 
                          + "Aún no ha cargado un diccionario"
                          + Fore.RESET + Back.RESET)

                    time.sleep(1.8)
                    clear()

        elif N == 4: # Opción 4: Corregir texto

            if help_o is None:
                err_ao()
            else:
                clear()
                if crear_dicc is False:
                    print(Fore.RED + Back.WHITE + Style.BRIGHT
                          + "No se ha cargado diccionario"
                          + Fore.RESET + Back.RESET)
                    time.sleep(1.8)
                    clear()
                else:
                    
                    while True:                            
                        men2 = "Indique la ruta y nombre de texto a corregir "
                        texto = input(men2)
                        ruta, nombre = osp.split(texto)
                        if nombre in help_o.guar_dicc:
                            
                            print(Fore.RED + Back.WHITE + Style.BRIGHT
                                  + "Existen archivos cargados como "
                                    "diccionarios con el mismo nombre que "
                                  + nombre
                                  + Fore.RESET + Back.RESET)                              
                            
                            time.sleep(2)
                            clear()
                        else:                                
                            salida = help_o.corregirTexto(texto)
                            
                            if salida is None:
                                nom = "foutput.out"
                                
                                print(Fore.GREEN + Back.WHITE + Style.BRIGHT
                                      + "\nSe generó el archivo: {}".format(nom)
                                      + Fore.RESET + Back.RESET)
                                
                                print("¿Desea corregir otro texto?")
                                
                                opc = int(input("1. Si   2. No "))                                        
                                
                                if type(opc) != int or (opc < 1 or opc > 2):
                                    
                                    print(Fore.GREEN + Back.WHITE + Style.BRIGHT
                                          + "Opción inválida"
                                          + Fore.RESET + Back.RESET) 
                                
                                elif opc == 1:
                                    clear()
                                elif opc == 2:
                                    clear()
                                    break


                            elif salida is not None:
                                print(Fore.RED + Back.WHITE + Style.BRIGHT
                                      + str(salida) + Fore.RESET + Back.RESET)
                                                                  
                                print("¿Desea corregir otro texto?")
                                
                                opc = int(input("1. Si   2. No "))                                        
                                
                                if type(opc) != int or (opc < 1 or opc > 2):
                                    
                                    print(Fore.GREEN + Back.WHITE + Style.BRIGHT
                                          +"Opción inválida"
                                          + Fore.RESET + Back.RESET) 
                                
                                elif opc == 1:
                                    clear()
                                elif opc == 2:
                                    clear()
                                    break

        elif N == 5: #Opción 5: Mostrar diccionario
            if help_o is None:
                err_ao()
            else:
                if crear_dicc is False:

                    print(Fore.RED + Back.WHITE + Style.BRIGHT
                          + "No se ha cargado diccionario"
                          + Fore.RESET + Back.RESET)

                    time.sleep(1.8)
                    clear()
                else:
                    help_o.imprimirDiccionario()
                    continuar = input("Presione enter para continuar...")
                    clear()

        elif N == 6: # Opción 6: Salir
            sys.exit()

    except ValueError:
        print(Fore.RED + Back.WHITE + Style.BRIGHT
              + "Intrudujo un valor no entero"
              + Fore.RESET + Back.RESET)
        time.sleep(1.5)
        clear()
