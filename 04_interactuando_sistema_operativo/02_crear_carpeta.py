import os

nueva_carpeta="nueva carpeta" # Nombre de la carpeta a crear
directorio_actual=os.getcwd() # Traer la ruta actual
path=os.path.join(directorio_actual,nueva_carpeta) # crea una ruta completa con la carpeta a crear
os.mkdir(path) # crea la ruta que se le pasa