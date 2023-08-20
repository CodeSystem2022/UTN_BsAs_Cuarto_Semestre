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

            sentencia = 'delete from persona where id_persona=%s'
            valores = (7,)  # es un tupla

            #clase 5 parte5

            cursor.execute(sentencia, valores)
            registros_borrados = cursor.rowcount
            print(f'los registros borrados son : {registros_borrados}')


except Exception as e:
    print(f'Ocurrio un error : {e}')
finally:
    conexion.close()

