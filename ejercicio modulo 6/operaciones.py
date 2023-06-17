#Funcion de suma:
def suma_enteros(num1, num2):
    try:
        suma = num1 + num2
        return suma
    except ValueError:
        print("Error: Tipo de dato no valido.")


#Funcion de resta:
def resta_enteros(num1, num2):
    try:
        resta = num1 - num2
        return resta
    except ValueError:
        print("Error: Tipo de dato no valido.")


#Funcion de multiplicacion:        
def multiplicacion_enteros(num1, num2):
    try:
        producto = num1 * num2
        return producto
    except ValueError:
        print("Error: Tipo de dato no valido.")


#Funcion de division:
def division_enteros(num1, num2):
    try:
        if num1 > 0 and num2 > 0:
            cociente = num1 / num2
            return cociente
        else:
            mensaje = "No se puede dividir entre cero"
            return mensaje
    except ValueError:
        print("Error: Tipo de dato no valido.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")







