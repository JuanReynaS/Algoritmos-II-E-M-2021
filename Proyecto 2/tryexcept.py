while True:
    try:    
        x = int(input("Dame un numero: "))
        print("numero")
        break  # Si no da error, corto el while con break
    except ValueError:
        print("Eso no es un número, prueba otra vez...")