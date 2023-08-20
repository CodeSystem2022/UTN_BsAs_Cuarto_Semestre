from capa_datos_persona.Usuario import Usuario
from capa_datos_persona.cursor_del_pool import CursorDelPool
from logger_base import log



class UsuarioDAO:

     _SELECT = 'select * from usuario order by id_usuario'
     _INSERTAR = 'INSERT INTO usuario(username, password) VALUE (%s, %s)'
     _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE is_usuario=&s'
     _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

     @classmethod
     def seleccionar(cls):
         with CursorDelPool() as cursor:
         cursor.execute(cls.SELECT)
         registros = cursor.fetchall()
         usuarios = []
         for registro in registros:
             usuario = Usuario(registro[0], registro[1], registro[2])
             usuarios.append(usuario)
         return usuarios 

      @classmethod
      def insertar(cls, usuario):
          with CursorDelPool() as cursor:
              log.debug(f'Usuario a insertar: {usuario}')
              valores = (usuario.username, usuario.password)
              cursor.execute(cls._INSERTAR, valores)
              return cursor.rowcount


       
      @classmethod
      def actualizar(cls, usuario):
          with CursorDelPool() as cursor:
              log.debug(f'Usuario a actualizar: {usuario}')
              valores = (usuario.username, usuario.password, usuario.id_usuario)
              cursor.execute(cls._ACTUALIZAR, valores)
              return cursor.rowcount

      @classmethod
      def eliminar(cls, usuario):
          with CursorDelPool() as cursor:
              log.debug(f'Usuario a eliminar: {usuario}')
              valores = (usuario.id_usuario)
              cursor.execute(cls._ELIMINAR, valores)
              return cursor.rowcount























