class Notificacion:
    def __init__(self, id, mensaje, fecha_envio):
        self.id = id
        self.mensaje = mensaje
        self.fecha_envio = fecha_envio

    def __str__(self):
        return f"Notificación {self.id}: {self.mensaje}, fecha envío: {self.fecha_envio}"