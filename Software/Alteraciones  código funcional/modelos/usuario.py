class Usuario:
    def __init__(self, id, nombre, apellido, correo, contraseña):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = contraseña

    def validar_contraseña(self, contraseña):
        # Error de tipo: comparación de tipos incompatibles
        return self.contraseña == str(contraseña)

    def __str__(self):
        # Error de sintaxis: falta el return
        print(f"Usuario {self.id}: {self.nombre} {self.apellido}, correo: {self.correo}")