
from gestores.gestor_tareas import GestorTareas
from gestores.gestor_usuarios import GestorUsuarios

class Aplicacion:
    def __init__(self):
        self.gestor_tareas = GestorTareas()
        self.gestor_usuarios = GestorUsuarios()

    def iniciar_aplicacion(self):
        print("Iniciando aplicación...")
        self.menu_principal()

    def menu_principal(self):
        while True:
            print("Menú principal:")
            print("1. Agregar tarea")
            print("2. Eliminar tarea")
            print("3. Mostrar tareas")
            print("4. Agregar usuario")
            print("5. Eliminar usuario")
            print("6. Mostrar usuarios")
            print("7. Salir")
            opcion = input("Ingrese una opción: ")
            if opcion == "1":
                self.agregar_tarea()
            elif opcion == "2":
                self.eliminar_tarea()
            elif opcion == "3":
                self.mostrar_tareas()
            elif opcion == "4":
                self.agregar_usuario()
            elif opcion == "5":
                self.eliminar_usuario()
            elif opcion == "6":
                self.mostrar_usuarios()
            elif opcion == "7":
                print("Saliendo de la aplicación...")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

    def agregar_tarea(self):
        titulo = input("Ingrese el título de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        fecha_inicio = input("Ingrese la fecha de inicio de la tarea: ")
        fecha_fin = input("Ingrese la fecha de fin de la tarea: ")
        prioridad = input("Ingrese la prioridad de la tarea: ")
        tarea = Tarea(len(self.gestor_tareas.tareas) + 1, titulo, descripcion, fecha_inicio, fecha_fin, prioridad)
        self.gestor_tareas.agregar_tarea(tarea)
        print("Tarea agregada con éxito.")

    def eliminar_tarea(self):
        id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
        tarea = next((tarea for tarea in self.gestor_tareas.tareas if tarea.id == id_tarea), None)
        if tarea:
            self.gestor_tareas.eliminar_tarea(tarea)
            print("Tarea eliminada con éxito.")
        else:
            print("Tarea no encontrada.")

    def mostrar_tareas(self):
        print("Tareas:")
        for tarea in self.gestor_tareas.tareas:
            print(tarea)

    def agregar_usuario(self):
        nombre = input("Ingrese el nombre del usuario: ")
        apellido = input("Ingrese el apellido del usuario: ")
        correo = input("Ingrese el correo del usuario: ")
        contraseña = input("Ingrese la contraseña del usuario: ")
        usuario = Usuario(len(self.gestor_usuarios.usuarios) + 1, nombre, apellido, correo, contraseña)
        self.gestor_usuarios.agregar_usuario(usuario)
        print("Usuario agregado con éxito.")

    def eliminar_usuario(self):
        id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
        usuario = next((usuario for usuario in self.gestor_usuarios.usuarios if usuario.id == id_usuario), None)
        if usuario:
            self.gestor_usuarios.eliminar_usuario(usuario)
            print("Usuario eliminado con éxito.")
        else:
            print("Usuario no encontrado.")

    def mostrar_usuarios(self):
        print("Usuarios:")
        for usuario in self.gestor_usuarios.usuarios:
            print(usuario)
