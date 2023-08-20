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
            valores =('carlos,'lara',clara@mail.com') # es un tupla

            #clase 5 parte5
            entrada = input('digite los id persona separados por coma : ')
            cursor.execute(sentencia,valores)
            registros_insertador = cursor.rowcount
            print(f'los registros insertados son : {registros_insertados}')


except Exception as e:
    print(f'Ocurrio un error : {e}')
finally:
    conexion.close()

