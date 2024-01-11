from .conexion_bd import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion=ConexionDB()
    sql='''
    CREATE TABLE peliculas(
        id_pelicula Integer,
        nombre varchar(100),
        duracion varchar(10),
        genero varchar(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo='Crear Tabla'
        mensaje='Se creo la tabla correctamente'
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo='Crear Tabla'
        mensaje='No se creo la tabla correctamente'
        messagebox.showwarning(titulo,mensaje)


def borrar_tabla():
    conexion=ConexionDB()
    sql='DROP TABLE peliculas'
    try: 
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo='Eliminar Tabla'
        mensaje='Se Elimina la tabla correctamente'
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo='Eliminar Tabla'
        mensaje='No se elimina la tabla correctamente'
        messagebox.showwarning(titulo,mensaje)


class Peliculas():
    def __init__(self, nombre, duracion,genero):
        self.id_pelicula=None
        self.nombre=nombre
        self.duracion=duracion
        self.genero=genero

    def __str__(self):
        return f'Pelicula {self.nombre} con una duracion {self.duracion} y es de {self.genero} '
    

def guardar(pelicula):
    conexion=ConexionDB()
    sql=f"""INSERT INTO peliculas (nombre,duracion,genero) 
    VALUES('{pelicula.nombre}','{pelicula.duracion}', '{pelicula.genero}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla peliculas no esta creado en la base de datos'
        messagebox.showerror(titulo,mensaje)

def listar():
    conexion=ConexionDB()
    lista_peliculas=[]
    sql="SELECT * FROM peliculas"
    try:
        conexion.cursor.execute(sql)
        lista_peliculas=conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo='Conexion al Registro'
        mensaje='Crea la tabla en la base de datos'
        messagebox.showerror(titulo,mensaje)

    return lista_peliculas

def editar(pelicula,id_pelicula):
    conexion=ConexionDB()
    sql=f"""UPDATE peliculas 
    SET nombre='{pelicula.nombre}', duracion='{pelicula.duracion}', genero='{pelicula.genero}' 
    WHERE id_pelicula={id_pelicula}
    """

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo='Edicion de datos'
        mensaje='No se apodido editar este registro'
        messagebox.showerror(titulo,mensaje)

def eliminar(id_pelicula):
    conexion=ConexionDB()
    sql=f"DELETE FROM peliculas WHERE id_pelicula={id_pelicula}"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo='Eliminar Datos'
        mensaje='No se pudo eliminar el registro'
        messagebox.showerror(titulo,mensaje)