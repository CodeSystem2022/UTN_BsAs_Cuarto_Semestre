# Manejo de contexto with: sintaxis simplificada
from ManejoArchivos import ManejoArchivos

# with open('prueba.txt', 'r', encoding='utf8') as archivo:
#     print(archivo.read())
# No hace falta ni el try ni el finally, se ejecutan de forma automatica
# Utiliza diferentes métodos:
# __enter__  es el que abre
# __exit__ es el q cierra

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
