from gestores.gestor_tareas import GestorTareas
from gestores.gestor_usuarios import GestorUsuarios
from modelos.usuario import Usuario
from modelos.tarea import Tarea

def main():
    gestor_tareas = GestorTareas()
    gestor_usuarios = GestorUsuarios()

    # Crear un usuario
    usuario = Usuario(1, "Juan", "Pérez", "juan.perez@example.com", "password")
    gestor_usuarios.agregar_usuario(usuario)

    # Crear una tarea
    tarea = Tarea(1, "Tarea de ejemplo", "Descripción de la tarea", "2022-01-01", "2022-01-31", "Alta")
    gestor_tareas.agregar_tarea(tarea)

    # Mostrar usuarios y tareas
    gestor_usuarios.mostrar_usuarios()
    gestor_tareas.mostrar_tareas()

if __name__ == "__main__":
    main()