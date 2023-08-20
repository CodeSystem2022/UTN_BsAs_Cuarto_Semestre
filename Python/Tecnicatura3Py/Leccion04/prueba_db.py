import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)

cursor = conexion.cursor()
sentencia = 'select * from personas'
cursor.execute(sentencia)
registros = cursor.fetchall() # se recuperan los registros q seran una lista
print(registros)
cursor.close()
conexion.close()

