class Task:
    def __init__(self, title: str, description: str):
        if not title or title.strip() == "":
            raise ValueError("Título da tarefa não pode ser vazio.")

        self.title = title
        self.description = description
        self.completed = False


class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, title: str, description: str):
        if title in self.tasks:
            raise ValueError("Já existe uma tarefa com esse título.")

        task = Task(title, description)
        self.tasks[title] = task
        return task

    def list_tasks(self):
        return list(self.tasks.values())

    def get_task(self, title: str):
        if title not in self.tasks:
            raise KeyError("Tarefa não encontrada.")
        return self.tasks[title]

    def complete_task(self, title: str):
        task = self.get_task(title)
        task.completed = True

    def remove_task(self, title: str):
        if title not in self.tasks:
            raise KeyError("Tarefa não encontrada.")
        del self.tasks[title]
