import os

carpeta_eliminar="nueva carpeta" # Nombre de la carpeta a crear
directorio_actual=os.getcwd() # Traer la ruta actual
path=os.path.join(directorio_actual,carpeta_eliminar) # crea una ruta completa con la carpeta a crear
existe_carpeta=os.path.exists(path) # valida si la ruta ya existe 
if existe_carpeta:
    os.rmdir(path) # crea la ruta que se le pasa
    print("Se elimina la carpeta")
else:
    print("No existe la carpeta a eliminar")