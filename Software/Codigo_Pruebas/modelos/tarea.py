class Tarea:
    def __init__(self, id, titulo, descripcion, fecha_inicio, fecha_fin, prioridad):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.prioridad = prioridad

    def __str__(self):
        return f"Tarea {self.id}: {self.titulo}, fecha inicio: {self.fecha_inicio}, fecha fin: {self.fecha_fin}"