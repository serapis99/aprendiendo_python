import os
directorio=os.getcwd()

# trae los elementos de la ruta actual
contenido=os.listdir() 
print(contenido)

# trae los elementos de una ruta especifica
contenido = os.listdir(path=directorio) 
print(contenido)