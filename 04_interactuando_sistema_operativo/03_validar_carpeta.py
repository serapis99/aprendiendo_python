import os

nueva_carpeta="nueva carpeta" # Nombre de la carpeta a crear
directorio_actual=os.getcwd() # Traer la ruta actual
path=os.path.join(directorio_actual,nueva_carpeta) # crea una ruta completa con la carpeta a crear
existe_carpeta=os.path.exists(path) # valida si la ruta ya existe 
if not existe_carpeta:
    print("Se crea la ruta")
    os.mkdir(path) # crea la ruta que se le pasa
else:
    print("La ruta ya existia")