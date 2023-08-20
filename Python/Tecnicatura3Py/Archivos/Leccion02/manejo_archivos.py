# Declaramos una variable

# Busca y abre el archivo, si no existe, lo crea
# Puede generar excepciones, lo encerramos en un try catch
# 'w' = write
# 'r' = read
# 'a' = append (anexar información)
# 'x' = crea el archivo
# 't' = text (tipo de archivo texto)
# 'b' = binary (tipo de archivo binario)
# 'w+' = escribe y lee
# 'r+' = lee y escribe
try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('Como por ejemplo: acción, ejecución y producción\n')
    archivo.write('Con esto terminamos.')
except Exception as e:
    print(e)
finally:  # Se ejecuta siempre
    archivo.close()  # se debe cerrar el archivo
