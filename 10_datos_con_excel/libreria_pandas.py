import psycopg2
import pandas as pd

# -------------------- conectando y extrayendo datos de una base de datos -----------
conection=psycopg2.connect(
    host='localhost',
    user='postgres',
    database='test_db',
    password='123456',
    port="5432"
)

conection.autocommit=True

query='SELECT * FROM public."Persona"'

#  usando pandas para realizar la consulta a la base de datos
# se crea un dataframe
df=pd.read_sql(query,con=conection)
conection.close

# imprimiendo el dataframe
print(df)

# se guarda el dataframe en un excel
df.to_excel("datos.xlsx",index=False)
