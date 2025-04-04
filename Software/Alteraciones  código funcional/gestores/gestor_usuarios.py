from modelos.usuario import Usuario

class GestorUsuarios:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        # Error de lógica: no se verifica si el usuario ya existe
        self.usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        # Error de tipo: no se verifica si el usuario es None
        self.usuarios.remove(usuario)

    def mostrar_usuarios(self):
        # Error de sintaxis: uso incorrecto de comillas
        for usuario in self.usuarios:
            print(f'Usuario {usuario.id}: {usuario.nombre} {usuario.apellido}, correo: {usuario.correo}')