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

nombre = 'Juan'
edad = 19
sueldo = 3000 
mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
print(mensaje_con_formato )

mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo)
print(mensaje)


mensaje = 'Sueldo {2:.2f} Nombre {0} Edad {1} '.format(nombre, edad, sueldo)
print(mensaje)

mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
print(mensaje)

diccionario = {'nombre': 'Ivan', 'Edad': 35, 'Sueldo': 8000.00}
mensaje = f'Nombre {persona[nombre]}'.format(persona=diccionario)

print(mensaje)




















