#import suma
#import resta
#import multiplicacion
#import division

#num1 = int(input("Ingrese primer numero: "))
#num2 = int(input("Ingrese segundo numero: "))
from operaciones import suma_enteros
from operaciones import resta_enteros
from operaciones import multiplicacion_enteros
from operaciones import division_enteros
def main():
    while True:
     try:
        print("*******OPERACIONES*******")
        num1 = int(input("Ingrese primer numero: "))
        num2 = int(input("Ingrese segundo numero: "))
        s = suma_enteros(num1,num2)
        r = resta_enteros(num1,num2)
        m = multiplicacion_enteros(num1,num2)
        d = division_enteros(num1,num2)
        return (f"La suma de los numeros es: {s}\nLa resta de los numeros es: {r}\nLa multiplicacion de los numeros es: {m}\nLa division de los numeros es: {d}")
     except ValueError:
        print("Tipo de dato invalido")

operacion = main()
print(operacion)

