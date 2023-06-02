# se usa el contexto **with** para abrir y cerrar la conexion al archivo

with open("datos.txt","r") as f:
    
    print()
    print("lectura de una sola linea".center(60,"*"))
    print()

    # lee una linea, depende donde este el cursor.
    print(f.readline())

    print()
    print("lectura de todas las lines y salida en lista".center(60,"*"))
    print()

    # lee todas las lineas y devuelve una lista
    f.seek(0) # mueve el cursor a la posicion 0
    lista=f.readlines()
    lista=[i.replace('\n','') for i in lista]
    print(lista)

    print()
    print("lectura de todas las lineas salida en texto".center(60,"*"))
    print()

    # lee todas las lineas y devuelve un string
    f.seek(0) # mueve el cursor a la posicion 0
    texto=f.read()
    print(texto)

