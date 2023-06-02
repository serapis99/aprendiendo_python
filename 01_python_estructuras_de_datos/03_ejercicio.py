# diccionario de diccionario

notas={
    "Calculo":{
        "pp":3.5,
        "sp":2.5,
        "tp":1.5
    },
    "Quimica":{
        "pp":2.5,
        "sp":3.0,
        "tp":5.0
    },
    "Deporte":{
        "pp":2.4,
        "sp":2.0,
        "tp":2.2
    },
    "Logica":{
        "pp":1.5,
        "sp":4.0,
        "tp":4.5
    },
}

# 3.1 Calcula la nota final de cada materia (30%, 30%, 40%)
# y agregue el valor a los datos

def c31_final():
    copia_notas=notas.copy()
    for materia in copia_notas:
        corte1=copia_notas[materia]["pp"]*0.3
        corte2=copia_notas[materia]["sp"]*0.3
        corte3=copia_notas[materia]["tp"]*0.4
        nota_final=corte1+corte2+corte3
        notas[materia]["nf"]=nota_final

    # crear el titulo a imprimir
    print()
    print("agregando Nota final".center(60,"*"))
    print()

    # recorre el arreglo para imprimir
    for clave in notas.keys():
        print(f"En la clave {clave} las notas son: {notas[clave]}")


# 3.2 Calcule el promedio de las notas

def c32_promedio():
    global notas

    # crear el titulo a imprimir
    print()
    print("Calculando Promedios".center(60,"*"))
    print()

    promedio=0

    for clave in notas.keys():
        promedio_materia=notas[clave]["pp"]+notas[clave]["sp"]+notas[clave]["tp"]
        promedio_materia/=3
        print(f"en la materia {clave} el promedio fue: {(promedio_materia):.2f}")
        promedio+=promedio_materia
    
    print(f"El promedio de todas las materias fue {(promedio/len(notas)):.2f}")

# llamar las funciones y mostrar los resultados

c31_final()
c31_final()
c32_promedio()
c31_final()
c32_promedio()
c32_promedio()
