# todo_app.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No hay tareas en la lista.")
        else:
            print("Tareas:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\n1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            task = input("Ingrese la tarea: ")
            todo_list.add_task(task)
            print("Tarea agregada con éxito.")
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
