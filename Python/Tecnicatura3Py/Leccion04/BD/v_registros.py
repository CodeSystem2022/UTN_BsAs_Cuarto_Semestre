
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
            sentencia = 'select * from personas where id_persona IN (1.2)'
            #clase 5 parte5
            entrada = input('digite los id persona separados por coma : ')
            llaves.primarias = (tuple(entrada.split(',')),)
            llaves_primarias =((1,2,3),)
            cursor.execute(sentencia,llaves_primarias)
            cursor.execute(sentencia,(id_persona,))
            cursor.execute(sentencia)
            registros = cursor.fetchall() # se recuperan los registros q seran una lista
            # registros = cursor.fetchone()  # se recuperan los registros q seran una lista
            for registro in registros:
                print(registros)

except Exception as e:
    print(f'Ocurrio un error : {e}')
finally:
    conexion.close()

