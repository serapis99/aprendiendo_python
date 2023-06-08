import psycopg2

conection=psycopg2.connect(
    host='localhost',
    user='postgres',
    database='test_db',
    password='123456',
    port="5432"
)

conection.autocommit=True

cursor=conection.cursor()
query='INSERT INTO public."Persona"(id_persona, nombre, apellido, email) VALUES (8, \'ruben\', \'gacha\', \'rgacha@mail.com\')'
cursor.execute(query)
cursor.close

conection.close