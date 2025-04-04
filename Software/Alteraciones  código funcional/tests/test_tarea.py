import unittest
from modelos.tarea import Tarea

class TestTarea(unittest.TestCase):

    def test_crear_tarea(self):
        tarea = Tarea(1, "Tarea de ejemplo", "Descripción de la tarea", "2022-01-01", "2022-01-31", "Alta")
        self.assertIsNotNone(tarea)
        self.assertEqual(tarea.id, 1)
        self.assertEqual(tarea.titulo, "Tarea de ejemplo")
        self.assertEqual(tarea.descripcion, "Descripción de la tarea")
        self.assertEqual(tarea.fecha_inicio, "2022-01-01")
        self.assertEqual(tarea.fecha_fin, "2022-01-31")
        self.assertEqual(tarea.prioridad, "Alta")

    def test_validar_fecha_inicio(self):
        tarea = Tarea(1, "Tarea de ejemplo", "Descripción de la tarea", "2022-01-01", "2022-01-31", "Alta")
        self.assertTrue(tarea.validar_fecha_inicio("2022-01-01"))
        self.assertFalse(tarea.validar_fecha_inicio("2022-02-01"))

if __name__ == "__main__":
    unittest.main()