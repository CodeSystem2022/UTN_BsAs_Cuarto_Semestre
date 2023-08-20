from NumerosIgualesException import *

resultado = None

# Prueba lo q esta dentro del try, si surge alguna excepcion la imprime
try:
    a = int(input('Digite el primer nro: '))
    b = int(input('Digite el segundo nro: '))
    if a == b:
        # la palabra reservada raise lanza una excepción
        raise NumerosIgualesException('Son números iguales')
    resultado = a / b
except TypeError as e:
    print(f'DESDE TypeError: Ocurrió un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'DESDE ZeroDivisionError: Ocurrió un error: {type(e)}')
except Exception as e:
    print(f'DESDE Exception: Ocurrió un error: {type(e)}')
else:  # Funciona solo cuando el programa no arroja ninguna excepcion // OPCIONAL
    print('TRY/ELSE: Todo funcionó con éxito!')
finally:  # Siempre se va a ejecutar
    print('TRY/FINALLY: Ejecución del try finalizado')

print(f'El resultado es: {resultado}')
