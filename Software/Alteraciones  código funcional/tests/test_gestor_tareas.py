import unittest
from gestores.gestor_tareas import GestorTareas
from modelos.tarea import Tarea

class TestGestorTareas(unittest.TestCase):

    def test_agregar_tarea(self):
        gestor_tareas = GestorTareas()
        tarea = Tarea(1, "Tarea de ejemplo", "Descripción de la tarea", "2022-01-01", "2022-01-31", "Alta")
        gestor_tareas.agregar_tarea(tarea)
        self.assertEqual(len(gestor_tareas.tareas), 1)

    def test_eliminar_tarea(self):
        gestor_tareas = GestorTareas()
        tarea = Tarea(1, "Tarea de ejemplo", "Descripción de la tarea", "2022-01-01", "2022-01-31", "Alta")
        gestor_tareas.agregar_tarea(tarea)
        gestor_tareas.eliminar_tarea(tarea)
        self.assertEqual(len(gestor_tareas.tareas), 0)

if __name__ == "__main__":
    unittest.main()