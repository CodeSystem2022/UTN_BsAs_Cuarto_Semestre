
import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)



try:
    with conexion:
         with conexion.cursor() as cursor:

            sentencia = 'insert into persona (nombre,apellido,email) values (%s,%s,%s)'
            valores =(('carlos','lara','clara@mail.com'),
            ('pedro','gomez','pgomez@mail.com'),
            ( 'luis','diaz','ldiez@mail.com') # es un tupla de tuplas
                      )
           #clase 5 parte5

            cursor.executemany(sentencia,valores)
            registros_insertados = cursor.rowcount
            print(f'los registros insertados son : {registros_insertados}')


except Exception as e:
    print(f'Ocurrio un error : {e}')
finally:
    conexion.close()

