import unittest
from usuario import Usuario

class TestUsuario(unittest.TestCase):

    def test_crear_usuario(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan.perez@example.com", "password")
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.id, 1)
        self.assertEqual(usuario.nombre, "Juan")
        self.assertEqual(usuario.apellido, "Pérez")
        self.assertEqual(usuario.correo, "juan.perez@example.com")
        self.assertEqual(usuario.contraseña, "password")

    def test_validar_contraseña(self):
        usuario = Usuario(1, "Juan", "Pérez", "juan.perez@example.com", "password")
        self.assertTrue(usuario.validar_contraseña("password"))
        self.assertFalse(usuario.validar_contraseña("incorrecta"))

if __name__ == "__main__":
    unittest.main()