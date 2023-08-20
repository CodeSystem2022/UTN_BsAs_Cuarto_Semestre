# 'r' = read
archivo = open('prueba.txt', 'r', encoding='utf8')
# print(archivo.read(18))  # Los primeros x caracteres
# print(archivo.read(9))  # Continua la iteracion anterior
#
# print(archivo.readline())  # Una linea
# print(archivo.readline())  # La siguiente linea

# 'a' = append
# Cambiamos el modo append por write, ya que sino duplica el contenido cada vez q se ejecuta
archivo2 = open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())
archivo.close()
archivo2.close()
