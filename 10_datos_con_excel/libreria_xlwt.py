from xlwt import Workbook
import psycopg2


# --------------------conectarnos a la base de datos ------------
conection=psycopg2.connect(
    host='localhost',
    user='postgres',
    database='test_db',
    password='123456',
    port="5432"
)

cursor=conection.cursor()
sentencia='SELECT * FROM public."Persona"'
cursor.execute(sentencia)
registros=cursor.fetchall()
cursor.close()
conection.close()


# ---------------- creando excel con xlwt --------------------------
wb=Workbook()
sheet=wb.add_sheet("Hoja 1")

# --------------- escribiendo en memoria los datos ----------------
sheet.write(0,0,'ID')
sheet.write(0,1,'Nombre')
sheet.write(0,2,'Apellido')
sheet.write(0,3,'Email')

i=1
for row in registros:
    sheet.write(i,0,row[0])
    sheet.write(i,1,row[1])
    sheet.write(i,2,row[2])
    sheet.write(i,3,row[3])
    i+=1
        
# -------- guardar los datos de memoria a un excel ------------
wb.save("datos.xls")