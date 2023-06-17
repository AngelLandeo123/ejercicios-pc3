def longitud_de_la_ultima_palabra(texto):
    texto_nuevo = texto.strip()
    palabras_separadas = texto_nuevo.split(" ")
    ultima_palabra = palabras_separadas[-1]
    return len(ultima_palabra)
    
try:
    palabras = "    holi   ko  ghf"
    longitud = longitud_de_la_ultima_palabra(palabras)
    print(longitud)
    
except:
    print("Ingrese palabras porfavor.")
    
     

