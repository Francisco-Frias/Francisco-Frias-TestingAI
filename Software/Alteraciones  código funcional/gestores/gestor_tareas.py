from modelos.tarea import Tarea

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        # Error de lógica: no se verifica si la tarea ya existe
        self.tareas.append(tarea)

    def eliminar_tarea(self, tarea):
        # Error de tipo: no se verifica si la tarea es None
        self.tareas.remove(tarea)

    def mostrar_tareas(self):
        # Error de sintaxis: uso incorrecto de comillas
        for tarea in self.tareas:
            print(f'Tarea {tarea.id}: {tarea.titulo}, fecha inicio: {tarea.fecha_inicio}, fecha fin: {tarea.fecha_fin}')