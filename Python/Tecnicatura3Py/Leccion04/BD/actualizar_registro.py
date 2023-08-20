
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

            sentencia = 'update persona set nombre=%s,apellido=%s,email=%s where id_persona=%s'
            valores = (
                      ('juan ', 'castro', 'jcastro@mail.com', 4),
                      ('maria ', 'martinez', 'mmartinez@mail.com', 5)
            )

            # es un tupla de tuplas
            cursor.executemany(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'los registros actualizados son : {registros_actualizados}')


except Exception as e:
    print(f'Ocurrio un error : {e}')
finally:
    conexion.close()
