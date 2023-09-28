# Bool contiene los valores de True y False
# Los tipos numéricos, es false para el 0 (cero), true para los demas valores
valor=0
resultado = bool(valor)
print(f'valor: {valor}, Resultado:¨{resultado}')

valor= 0.1
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')



#Tipo string -> False '', True demas valores
valor=''
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor='Hola'
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

#Tipo colecciones ->False para colecciones vacias
#Tipo colecciones -> True para todas las demas
#Lista
valor = []
resultado = bool(valor)
print(f'valor de una lista vacia: {valor}, Resultado:{resultado}')

valor = [2,3,4]
resultado, = bool(valor)
print(f'valor de una lista con elementos: {valor}, Resultado:{resultado}')

#Tupla
valor=()
resultado= bool(valor)
print(f'valor de una tupla vacia: {valor}, Resultado:{resultado}')

valor=(5,)
resultado= bool(valor)
print(f'valor de una tupla con elementos: {valor}, Resultado:{resultado}')

#Diccionario
valor={}
resultado= bool(valor)
print(f'valor de un diccionario vacio: {valor}, Resultado:{resultado}')

valor={'Nombre':'Juan','Apellido':'Perez'}
resultado= bool(valor)
print(f'valor de un diccionario con elementos: {valor}, Resultado:{resultado}')



# mchalin (#56)
# En sentencia de control, es false cuando es None, true para los demás valores
if bool(''):
    print('Es true')
else:
    print('Es false')

if bool(' '):
    print('Es true')
else:
    print('Es false')

# mchalin (#57)
# Con ciclo while, es false cuando es 0, true para los demás valores
variable = 0
while variable:
    print(variable)
    print('Es true')
    break
else:
    print('Es false')

variable = 1
while variable:
    print(variable)
    print('Es true')
    break
else:
    print('Es false')



