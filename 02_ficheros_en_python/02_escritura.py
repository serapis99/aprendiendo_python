# al abrirlo con el parametro **w** se sobreescribe el archivo 
with open('datos.txt','w') as f:
    for i in range(1,11):
        texto=f'datos escritos en la linea {i} \n'
        f.write(texto) # escribe el texto en el archivo
