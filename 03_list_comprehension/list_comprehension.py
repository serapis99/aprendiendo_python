# lista de forma normal

def titulo(titulo:str)->None:
    print()
    print(titulo.center(60,'*'))
    print()

titulo("lista de forma normal")

lista= []
for i in range(9):
    lista.append(i)
print(lista)

titulo("Usando list comprehension normal")

lista2=[i for i in range(9)]
print(lista2)

titulo("Usando list comprehension con condicion")
lista3=[i for i in range(9) if i%2==0]
print(lista3)

titulo("Usando list comprehension con una operacion en los items")
lista4=[i/2 for i in range(9)]
print(lista4)

titulo("Usando list comprehension con un string")
nombre =['andres','sebastian','john','peter']
nombre =[i.upper() for i in nombre]
print(nombre)

titulo("list comprehension usando propiedades de un objeto")

class Estudiante():
    def __init__(self,nombre:str,nota:int) -> None:
        self.nombre=nombre
        self.nota=nota

estudiantes=list()

nombres =['andres','sebastian','john','peter']

for i in nombres:
    nota=5
    e = Estudiante(i,nota)
    estudiantes.append(e)

suma= sum(e.nota for e in estudiantes)
print(suma)