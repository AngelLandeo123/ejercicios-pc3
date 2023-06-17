def triangulopascal(filas):
    primera_fila = [1]
    numero_de_filas = filas
    valor = numero_de_filas
    espacio = "\t".expandtabs(valor+1)
    print("{}{}".format(espacio, primera_fila))
    for i in range(1, numero_de_filas):
        longitud = len(primera_fila)
        nueva_fila = [1]
        for j in range(0, longitud-1):
            operacion = primera_fila[j]+primera_fila[j+1]
            nueva_fila.append(operacion)
        nueva_fila.append(1)
        espacio = "\t".expandtabs(valor)
        valor -= 1
        print("{}{}".format(espacio, nueva_fila))
        primera_fila = nueva_fila
while True:
    try: 
        numero = int(input("Ingrese el numero de filas del triangulo pascal: ")) 
        pascal = triangulopascal(numero) 
        print(pascal)
        print("Gracias :)")
        break
    except ValueError:
        print("ERROR: Ingrese un numero entero.")       

