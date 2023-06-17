#def cali(): 
while True:
   try:
      calificaciones = input("Ingrese las calificaciones separadas por comas: ")
      calificaciones_separadas = calificaciones.split(",")
      lista_de_calificaciones = []
      for calificacion in calificaciones_separadas:
            entero = int(calificacion.strip())
            lista_de_calificaciones.append(entero)
      print(lista_de_calificaciones)
   except ValueError:
        print("ERROR!! Tipeo erroneo y/o ingrese numeros enteros.")

#num = cali()
#print(num)








