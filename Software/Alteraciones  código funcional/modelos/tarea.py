class Tarea:
    def __init__(self, id, titulo, descripcion, fecha_inicio, fecha_fin, prioridad):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.prioridad = prioridad

    def validar_fecha_inicio(self, fecha_inicio):
        # Error de lógica: comparación incorrecta
        return self.fecha_inicio <= fecha_inicio

    def validar_fecha_fin(self, fecha_fin):
        # Error de tipo: atributo no definido
        return self.fecha_fin <= fecha_fin and self.fecha_fin is not None

    def __str__(self):
        # Error de sintaxis: uso incorrecto de comillas
        return f'Tarea {self.id}: {self.titulo}, fecha inicio: {self.fecha_inicio}, fecha fin: {self.fecha_fin}'