import psycopg2  # Librería para conectar con PostgreSQL

# Datos para la conexion
dns = "dbname=test_bd user=postgres password=admin host=127.0.0.1 port=5432"

# Conexión con la base de datos
conexion = psycopg2.connect(dns)

# conexion = psycopg2.connect(
#     user='postgres',
#     password='admin',
#     host='127.0.0.1',
#     port='5432',
#     database='test_bd'
# )
print(conexion)

# Uso correcto de la conexion con try/finally
try:
    with conexion:
        with conexion.cursor() as cursor:  # Cierra el recurso abierto como cursor
            # sentencia = 'SELECT * FROM persona' # Sentencia SQL para recuperar todos los registros de la tabla
            # sentencia = 'SELECT id_persona, nombre FROM persona' # recuperar id y nombre de la tabla

            # %s place holder, sustituye el valor de la variable
            # Sentencia SQL para recuperar un registro de la tabla
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = input('Ingrese nro de id_persona: ')
            # Ejecutamos la sentencia con el valor de la variable (como una tupla)
            cursor.execute(sentencia, (id_persona,))

            # cursor.execute(sentencia)  # Ejecutamos la sentencia

            registros = cursor.fetchone()  # Recuperamos el primer registro
            # registros = cursor.fetchall()  # Recuperamos los registros

            print(registros)  # Mostramos los registros
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

'''
# Creación de cursor
cursor = conexion.cursor()
print(cursor)

# Creación de sentencia SQL
sentencia = 'SELECT * FROM persona'

# Ejecución de sentencia
cursor.execute(sentencia)

# Recuperación de los registros de la sentencia
registros = cursor.fetchall()

# Se muestran los registros
print(registros)

# Cierre de cursor
cursor.close()

# Cierre de conexión
conexion.close()
'''
