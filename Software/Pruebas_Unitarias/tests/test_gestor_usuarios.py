import unittest
from gestor_usuarios import GestorUsuarios
from usuario import Usuario

class TestGestorUsuarios(unittest.TestCase):

    def test_agregar_usuario(self):
        gestor_usuarios = GestorUsuarios()
        usuario = Usuario(1, "Juan", "Pérez", "juan.perez@example.com", "password")
        gestor_usuarios.agregar_usuario(usuario)
        self.assertIsNotNone(gestor_usuarios.usuarios)
        self.assertEqual(len(gestor_usuarios.usuarios), 1)

    def test_eliminar_usuario(self):
        gestor_usuarios = GestorUsuarios()
        usuario = Usuario(1, "Juan", "Pérez", "juan.perez@example.com", "password")
        gestor_usuarios.agregar_usuario(usuario)
        gestor_usuarios.eliminar_usuario(usuario)
        self.assertIsNotNone(gestor_usuarios.usuarios)
        self.assertEqual(len(gestor_usuarios.usuarios), 0)

if __name__ == "__main__":
    unittest.main()