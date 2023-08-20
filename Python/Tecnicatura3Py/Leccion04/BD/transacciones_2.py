# clase 6.2 manejo de transacciones

import psycopg2 as bd

conexion = bd.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)

try:
    #conexion.autocommit = False esto no deberia estat
    cursor = conexion.cursor()
    sentencia= 'insert into persona(nombre,apellido,email)values (%s,%s,%s)'
    valores= ('maria', 'Esparza', 'mesparza@gmail.com')
    cursor.execute(sentencia, valores)
    sentencia = 'update persona set nombre=%s, apellido=%s,email=%s where id_persona=%s'
    valores = ('juan', 'juarez', 'jjuarez@mail.com', 1)
    cursor.execute(sentencia, valores)
    conexion.commit()

except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo un rollback : {e}')
finally:
    conexion.close()