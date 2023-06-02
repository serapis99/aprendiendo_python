# caso 1: Lista de Listas

notas=[
    ['Calculo', 3.5, 2.5, 1.5],
    ['Quimica', 2.5, 3.0, 5.0],
    ['Deporte', 2.4, 2.0, 2.2],
    ['Logica', 1.5, 4.0, 4.5]
]

# 1.1 Calcula la nota final de cada materia (30% ,30%, 40%)
# y agregue el valor a los datos

def c11_final():
    # se indica que debe usar la variable global notas
    global notas

    # se copia el arreglo para poder modificar el principal
    copia_notas=notas.copy() 

    # se recorre el elemento copiado para hacer las operaciones
    for indice,nota_materia in enumerate(copia_notas):
        # se valida si la lista es mayor a 4 para eliminar el sobrante
        if len(nota_materia)>4:
            del(notas[indice][4:])

        corte1=nota_materia[1]*0.3
        corte2=nota_materia[2]*0.3
        corte3=nota_materia[3]*0.4
        nota_final=corte1+corte2+corte3
        notas[indice].append(nota_final)

    # crear el titulo a imprimir
    print()
    print("agregando Nota final".center(60,"*"))
    print()

    # recorre el arreglo para imprimir
    for nota_materia in notas:
        print(nota_materia)


# 1.2 Calcule el promedio de las notas del estudiante
def c12_promedio():
    global notas

    # crear el titulo a imprimir
    print()
    print("Calculando Promedios".center(60,"*"))
    print()

    promedio=0
    for materia in notas:
        promedio_materia=0
        for i,nota in enumerate(materia):
            if i>0 and i<=3:
                promedio_materia+=nota
            elif i==0:
                continue
            else:
                break
        print(f"en la materia {materia[0]} el promedio fue: {(promedio_materia/3):.2f}")
        promedio+=promedio_materia/3
    
    print(f"El promedio de todas las materias fue {(promedio/len(notas)):.2f}")

# llamar las funciones y mostrar los resultados

c11_final()

c11_final()
c12_promedio()
c11_final()

c12_promedio()
c12_promedio()