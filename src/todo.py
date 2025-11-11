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

    # src/todo.py
class Task:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, title: str, description: str):
        task = Task(title, description)
        self.tasks[title] = task
        return task

# src/todo.py
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
        task = Task(title, description)
        self.tasks[title] = task
        return task
# src/todo.py
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
# src/todo.py
class Task:
    def __init__(self, title: str, description: str):
        if not title or title.strip() == "":
            raise ValueError("Título da tarefa não pode ser vazio.")
        self.title = title
        self.description = description
        self.completed = False

    def __repr__(self):
        return f"Task(title={self.title!r}, completed={self.completed})"

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
# src/todo.py
class Task:
    def __init__(self, title: str, description: str):
        if not title or title.strip() == "":
            raise ValueError("Título da tarefa não pode ser vazio.")
        self.title = title
        self.description = description
        self.completed = False

    def __repr__(self):
        return f"Task(title={self.title!r}, completed={self.completed})"

class ToDoList:
    def __init__(self):
        # usar dicionário para acesso por título (único)
        self.tasks = {}

    def add_task(self, title: str, description: str):
        if title in self.tasks:
            raise ValueError("Já existe uma tarefa com esse título.")
        task = Task(title, description)
        self.tasks[title] = task
        return task

    def list_tasks(self):
        """Retorna lista de objetos Task."""
        return list(self.tasks.values())

    def get_task(self, title: str):
        """Retorna Task pelo título ou KeyError se não existir."""
        if title not in self.tasks:
            raise KeyError("Tarefa não encontrada.")
        return self.tasks[title]

    def complete_task(self, title: str):
        """Marca tarefa como concluída — lança KeyError se não existir."""
        task = self.get_task(title)
        task.completed = True

    def remove_task(self, title: str):
        """Remove tarefa — lança KeyError se não existir."""
        if title not in self.tasks:
            raise KeyError("Tarefa não encontrada.")
        del self.tasks[title]
# src/todo.py
from typing import List

class Task:
    """
    Representa uma tarefa simples com título, descrição e status.
    """
    def __init__(self, title: str, description: str):
        if not title or title.strip() == "":
            raise ValueError("Título da tarefa não pode ser vazio.")
        self.title = title.strip()
        self.description = description or ""
        self.completed = False

    def __repr__(self):
        return f"Task(title={self.title!r}, completed={self.completed})"

class ToDoList:
    """
    Gerenciador em memória de tarefas.
    - Não permite títulos duplicados
    - Operações: adicionar, listar, obter, concluir, remover
    """
    def __init__(self):
        self._tasks = {}  # map title -> Task

    def add_task(self, title: str, description: str) -> Task:
        if title in self._tasks:
            raise ValueError(f"Já existe uma tarefa com o título '{title}'.")
        task = Task(title, description)
        self._tasks[task.title] = task
        return task

    def list_tasks(self) -> List[Task]:
        return list(self._tasks.values())

    def get_task(self, title: str) -> Task:
        try:
            return self._tasks[title]
        except KeyError:
            raise KeyError(f"Tarefa '{title}' não encontrada.")

    def complete_task(self, title: str) -> None:
        task = self.get_task(title)
        task.completed = True

    def remove_task(self, title: str) -> None:
        if title not in self._tasks:
            raise KeyError(f"Tarefa '{title}' não encontrada.")
        del self._tasks[title]
