from modelos.tarea import Tarea

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, tarea):
        self.tareas.remove(tarea)

    def mostrar_tareas(self):
        for tarea in self.tareas:
            print(tarea)