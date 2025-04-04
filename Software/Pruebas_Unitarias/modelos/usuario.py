class Usuario:
    def __init__(self, id, nombre, apellido, correo, contraseña):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = contraseña

    def validar_contraseña(self, contraseña):
        return self.contraseña == contraseña

    def __str__(self):
        return f"Usuario {self.id}: {self.nombre} {self.apellido}, correo: {self.correo}"