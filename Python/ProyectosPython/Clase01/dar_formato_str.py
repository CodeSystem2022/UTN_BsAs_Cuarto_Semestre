# dar fromato a un string

nombre = 'Ariel'
edad = 28
mensaje_con_formato = 'Mi nombre es %s y tengo %d años'% (nombre, edad)
print(mensaje_con_formato)
# creamos una tupla
persona = ('Carla', 'Gomez',5000.00) 
mensaje_con_formato ='Hola %s %s . Tu sueldo es  %.2f' % persona
print(mensaje_con_formato)
mensaje_con_formato ='Hola %s %s . Tu sueldo es  %.2f' 
print(mensaje_con_formato % persona)

