# al abrirlo con el parametro **a** se agrega al final del archivo
with open('datos.txt','a') as f:
    f.write("datos escritos en la linea 11\n")
    f.write("datos escritos en la linea 12\n")