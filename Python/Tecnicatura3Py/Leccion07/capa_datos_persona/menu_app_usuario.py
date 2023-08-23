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
    elif opcion == 3:
        id_usuario_var = int(input('Digite el id del usuario a modificar: '))
        usarname_var = input('Digite el nombre del usuario a modificar: ')
        password_var = input('Digite la contraseña del usuario a modificar: ')
        usuario= Usuario(id_usuario=id_usuario_var, username=username_var,password=password_var)
        usuario_actualizado = UsuarioDao.actualizar(usuario)
        log.INFO(f'Usuario actualizado: {usuario_actualizado}')
    elif opcion == 4:
        id_usuario_var = int(input('Digite el id del usuario a eliminar: '))
        usuario= Usuario(id_usuario=id_usuario_var)
        usuario_eliminado = UsuarioDao.eliminar(usuario)
        log.INFO(f'Usuario eliminado: {usuario_eliminado}')
else:
        log.info("Salimos de la aplicación, hasta pronto")
