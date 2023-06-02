# Diccionario de listas

notas={
    "Calculo":[3.5, 2.5, 1.5],
    "Quimica":[2.5, 3.0, 5.0],
    "Deporte":[2.4, 2.0, 2.2],
    "Logica":[1.5, 4.0, 4.5]
}

# 2.1 Calcula la nota final de cada materia (30%,30%,40%) 
# y agrege el valor a los datos

def c21_final():
    copia_notas=notas.copy()
    for clave in copia_notas.keys():
        # eliminar valores sobrantes de la lista
        if len(copia_notas[clave])>3:
            del(notas[clave][3:])
        
        corte1=copia_notas[clave][0]*0.3
        corte2=copia_notas[clave][1]*0.3
        corte3=copia_notas[clave][2]*0.4
        nota_final=corte1+corte2+corte3
        notas[clave].append(nota_final)

    # crear el titulo a imprimir
    print()
    print("agregando Nota final".center(60,"*"))
    print()

    # recorre el arreglo para imprimir
    for clave in notas.keys():
        print(f"En la clave {clave} las notas son: {notas[clave]}")

# 2.2 Calcule el promedio de las notas

def c22_promedio():
    global notas

    # crear el titulo a imprimir
    print()
    print("Calculando Promedios".center(60,"*"))
    print()

    promedio=0

    for clave in notas.keys():
        promedio_materia=0
        for i,nota in enumerate(notas[clave]):  
            if i<=2:
                promedio_materia+=nota
            else:
                break

        print(f"en la materia {clave} el promedio fue: {(promedio_materia/3):.2f}")
        promedio+=promedio_materia/3
    
    print(f"El promedio de todas las materias fue {(promedio/len(notas)):.2f}")

# llamar las funciones y mostrar los resultados

c21_final()
c21_final()
c22_promedio()
c21_final()
c22_promedio()
c22_promedio()