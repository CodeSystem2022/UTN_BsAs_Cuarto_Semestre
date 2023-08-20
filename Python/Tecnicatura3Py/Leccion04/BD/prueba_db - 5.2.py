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
            sentencia = 'select * from personas '
            #sentencia = 'select * from personas where id_presona=2'
            #s#entencia = 'select * from personas where id_persona=%s' #placeholder
            #cursor.execute(sentencia,(id_persona,))
            cursor.execute(sentencia)
            #registros = cursor.fetchall() # se recuperan los registros q seran una lista
            registros = cursor.fetchone()  # se recuperan los registros q seran una lista

            print(registros)

except Exception as e:
    print(f'Ocurrio un error : {e}')
finally:
    conexion.close()

