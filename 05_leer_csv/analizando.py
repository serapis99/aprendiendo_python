import csv

dic={
    'pregunta1':{
        'vivos':0,
        'muertos':0,
        'total':0
    },
    'pregunta2':{
        'porcentaje':0
    },
    'pregunta3':{
        'clases':[]
    },
    'pregunta4':{
        'hombres':0,
        'mujeres':0
    },
    'pregunta5':{
        'ticket':set()
    }


}

with open("titanic.csv") as file:
    datos=csv.reader(file,delimiter=',')
    for i,linea in enumerate(datos):
        # validando si es la cabecera
        if i==0:
            continue
        else:

            # se calcula cuantos registros hay
            dic['pregunta1']['total']+=1

            # se valida si murio o no
            if linea[1]=='0':
                dic['pregunta1']['muertos']+=1
            else:
                dic['pregunta1']['vivos']+=1

            # se valida si la clase existe o no 
            if linea[2] not in dic['pregunta3']['clases']:
                dic['pregunta3']['clases'].append(linea[2])

            # se valida si es hombre o mujer
            if linea[4]=='male':
                dic['pregunta4']['hombres']+=1
            else:
                dic['pregunta4']['mujeres']+=1
            
            # se agraga a una coleccion set el ticket
            dic['pregunta5']['ticket'].add(linea[8])


# se calcula el porcentaje
dic['pregunta2']['porcentaje']=dic['pregunta1']['vivos']/dic['pregunta1']['total']

# se formatean las respuestas
pregunta1="murieron {0} de {1} pasajeros".format(dic['pregunta1']['muertos'],dic['pregunta1']['total'])
pregunta2="el porcentaje de personas que sobrevivieron son {0:.2f}%".format(dic['pregunta2']['porcentaje'])
pregunta3="La cantidad de clases en el titanic son {0} ".format(len(dic['pregunta3']['clases']))
pregunta4="la cantidad de hombres era {0} y la cantidad de mujeres era {1}".format(dic['pregunta4']['hombres'],dic['pregunta4']['mujeres'])
pregunta5="la cantidad de tickets diferentes fueron {0} ".format(len(dic['pregunta5']['ticket']))

# se imprimen las respuestas
print(pregunta1)
print(pregunta2)
print(pregunta3)
print(pregunta4)
print(pregunta5)