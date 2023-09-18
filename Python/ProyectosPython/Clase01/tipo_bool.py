# Bool contiene los valores de True y False
# Los tipos numéricos, es false para el 0 (cero), true para los demas valores
valor=0
resultado = bool(valor)
print(f'valor: {valor}, Resultado:¨{resultado}')

valor= 0.1
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')#
# Falta código de issues anteriores.
#

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