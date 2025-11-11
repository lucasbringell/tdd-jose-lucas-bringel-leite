import pytest
from src.todo import ToDoList, Task

def test_criar_tarefa():
    todo = ToDoList()
    task = todo.add_task("Estudar TDD", "Ler sobre ciclo red-green-refactor")
    
    assert task.title == "Estudar TDD"
    assert task.description == "Ler sobre ciclo red-green-refactor"
    assert task.completed is False
