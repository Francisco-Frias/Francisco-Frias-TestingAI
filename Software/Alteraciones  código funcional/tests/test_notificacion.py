import unittest
from modelos.notificacion import Notificacion

class TestNotificacion(unittest.TestCase):

    def test_crear_notificacion(self):
        notificacion = Notificacion(1, "Mensaje de ejemplo", "2022-01-01")
        self.assertIsNotNone(notificacion)
        self.assertEqual(notificacion.id, 1)
        self.assertEqual(notificacion.mensaje, "Mensaje de ejemplo")
        self.assertEqual(notificacion.fecha_envio, "2022-01-01")

if __name__ == "__main__":
    unittest.main()