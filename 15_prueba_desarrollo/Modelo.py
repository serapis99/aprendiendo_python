import sqlite3

class Modelo:
    def __init__(self, nombre_bd="Basedatos/base_de_datos.db"):
        self.nombre_bd=nombre_bd
        self.conectar_bd()
    
    def conectar_bd(self):
        self.conn=sqlite3.connect(self.nombre_bd)
        self.cursor=self.conn.cursor()
    
    def cerrar_bd(self):
        self.conn.close()

    def crear_tablas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS formularios(
                numIdentificacion INTEGER NOT NULL PRIMARY KEY,
                nombres VARCHAR(30) NOT NULL,
                apellidos VARCHAR(30) NOT NULL,
                tipoIdentificacion VARCHAR(2) NOT NULL,
                estadoCivil INTEGER NOT NULL,
                fechaNacimiento DATE NOT NULL,
                numBeneficiarios INTEGER NOT NULL DEFAULT 0,
                fechaIngreso DATE NOT NULL             
        )''')
        self.cursor.execute('''
CREATE TABLE IF NOT EXISTS imagenes(
        numIdentificacion INTEGER NOT NULL,
        nombreImagen VARCHAR(30) NOT NULL,
        fecha DATE NOT NULL,
        PRIMARY KEY(numIdentificacion,nombreImagen),
        CONSTRAINT imagenes_fk1 FOREIGN KEY(numIdentificacion)
            REFERENCES formularios (numIdentificacion) ON UPDATE CASCADE ON DELETE NO ACTION
)

''')

    def buscar_formulario(self, id):
        self.cursor.execute("select * from formularios where numIdentificacion=?",(id,))
        if self.cursor.fetchone()==None:
            return False
        else:
            return True

    def obtener_formularios(self):
        self.cursor.execute("SELECT f.numIdentificacion, f.nombres, f.apellidos, f.tipoIdentificacion, f.estadoCivil, f.fechaNacimiento, f.numBeneficiarios, f.fechaIngreso, SUM(CASE WHEN i.nombreImagen IS NOT NULL THEN 1 ELSE 0 END) as cantidad_imagenes  FROM formularios as f left join imagenes as i on f.numIdentificacion = i.numIdentificacion group by f.numIdentificacion")
        return self.cursor.fetchall()
    
    def nuevo_formulario(self,numIdentificacion,nombre,apellido,tipoIdentificacion,estadoCivil,fechaNacimiento,numBeneficiarios,fechaIngreso):
        sql=f"""INSERT INTO formularios (numIdentificacion,
        nombres,apellidos,tipoIdentificacion, estadoCivil,
        fechaNacimiento,numBeneficiarios,fechaIngreso) 
        VALUES('{numIdentificacion}','{nombre}', '{apellido}',
        '{tipoIdentificacion}', '{estadoCivil}','{fechaNacimiento}', '{numBeneficiarios}','{fechaIngreso}')"""
        self.cursor.execute(sql)
        self.cursor.connection.commit()
    
    def actualizar_formulario(self,numIdentificacion,nombre,apellido,tipoIdentificacion,estadoCivil,fechaNacimiento,numBeneficiarios,fechaIngreso):
        sql=f"""UPDATE formularios SET nombres='{nombre}', apellidos='{apellido}', tipoIdentificacion='{tipoIdentificacion}',
        estadoCivil='{estadoCivil}', fechaNacimiento='{fechaNacimiento}', numBeneficiarios='{numBeneficiarios}', fechaIngreso='{fechaIngreso}'
        WHERE numIdentificacion='{numIdentificacion}'
        """
        print(sql)
        self.cursor.execute(sql)
        self.cursor.connection.commit()

    def eliminar_formulario(self,numIdentificacion):
        sql=f"DELETE FROM formularios WHERE numIdentificacion={numIdentificacion}"
        self.cursor.execute(sql)
        self.cursor.connection.commit()
if __name__=='__main__':
    gestor_bd=Modelo()
    gestor_bd.cerrar_bd()