notas=[
    {
        "nombre":"Calculo",
        "pp":3.5,
        "sp":2.5,
        "tp":1.5
    },
    {
        "nombre":"Quimica",
        "pp":2.5,
        "sp":3.0,
        "tp":5.0
    },
    {
        "nombre":"Deporte",
        "pp":2.4,
        "sp":2.0,
        "tp":2.2
    },
    {
        "nombre":"Logica",
        "pp":1.5,
        "sp":4.0,
        "tp":4.5
    }
]

# 4.1 Calcula la nota final de cada materia (30%, 30%, 40%)
# y agregue el valor a los datos

def c41_final():
    copia_notas=notas.copy()

    for indice,datos in enumerate(copia_notas):
        corte1=datos["pp"]*0.3
        corte2=datos["sp"]*0.3
        corte3=datos["tp"]*0.4
        nota_final=corte1+corte2+corte3
        notas[indice]["nf"]=nota_final

    # crear el titulo a imprimir
    print()
    print("agregando Nota final".center(60,"*"))
    print()

    # recorre el arreglo para imprimir
    for datos in notas:
        print(f"{datos}")

# 4.2 Calcule el promedio de las notas

def c42_promedio():
    global notas

    # crear el titulo a imprimir
    print()
    print("Calculando Promedios".center(60,"*"))
    print()

    promedio=0

    for nota in notas:
        promedio_materia=nota["pp"]+nota["sp"]+nota["tp"]
        promedio_materia/=3
        nombre=nota["nombre"]
        print(f"en la materia {nombre} el promedio fue: {(promedio_materia):.2f}")
        promedio+=promedio_materia
    
    print(f"El promedio de todas las materias fue {(promedio/len(notas)):.2f}")

# llamar las funciones y mostrar los resultados

c41_final()
c41_final()
c42_promedio()
c41_final()
c42_promedio()
c42_promedio()