while True:
    try:
        fraccion = input("Introduzca una fraccion con formato X/Y: " )
        x , y = map(int,fraccion.split("/"))
        if y == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.") 
        elif x >= y:
            raise ValueError("X debe ser mayor o igual a Y.")
        porcentaje = (x / y)* 100
        porcentaje_redondeado = round(porcentaje)
        if porcentaje <= 1:
            nivel = "Nivel de combustible es E"
        elif porcentaje >= 99:
            nivel = "Nivel de combustible es F"
        else:
            nivel = (f"{porcentaje_redondeado} % ")
        print(f"Su nivel de combustible es {nivel}.")
        break
    except ValueError:
            print("Error: Ingrese denuevo la fraccion.")
    except ZeroDivisionError as e:
            print("Error:", str(e))










