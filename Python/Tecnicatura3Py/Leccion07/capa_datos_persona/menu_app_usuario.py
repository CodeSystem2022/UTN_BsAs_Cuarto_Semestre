from Leccion007.capa_datos_persona.Usuario import Usuario
from Leccion007.capa_datos_persona.Usuario_dao import UsuarioDao
from logger_base import log

opcion = None
while opcion != 5:
    print("Opcion: ")
    print('1-Listar usuarios')
    print('2-Agregar usuario')
    print('3-Modificar usuario')
    print('4-Eliminar usuario')
    print(('5-Salir'))
    opcion = int(input('Digite la opcion (1-5): '))
    if opcion ==1:
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            log.info(usuario)

    elif opcion ==2:
        username_var =input('Digite el nombre de usuario: ')
        password_var = input('Digite su contraseña: ')
        usuario= Usuario(username=username_var, password=password_var)
        usuario_insertado = UsuarioDao.insertar(usuario)
        log.INFO(f'Usuario insertado: {usuario_insertado}')
else:
        log.info("Salimos de la aplicación, hasta pronto")
