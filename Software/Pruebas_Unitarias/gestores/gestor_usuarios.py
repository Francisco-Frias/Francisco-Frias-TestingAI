from modelos.usuario import Usuario

class GestorUsuarios:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        self.usuarios.remove(usuario)

    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)