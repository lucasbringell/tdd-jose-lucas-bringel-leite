import pytest
from src.todo import ToDoList, Task

def test_criar_tarefa():
    todo = ToDoList()
    task = todo.add_task("Estudar TDD", "Ler sobre ciclo red-green-refactor")
    
    assert task.title == "Estudar TDD"
    assert task.description == "Ler sobre ciclo red-green-refactor"
    assert task.completed is False

    import pytest
from src.todo import ToDoList, Task

def test_criar_tarefa():
    todo = ToDoList()
    task = todo.add_task("Estudar TDD", "Ler sobre ciclo red-green-refactor")
    
    assert task.title == "Estudar TDD"
    assert task.description == "Ler sobre ciclo red-green-refactor"
    assert task.completed is False

def test_nao_permite_titulo_vazio():
    todo = ToDoList()
    with pytest.raises(ValueError):
        todo.add_task("", "Descrição qualquer")

import pytest
from src.todo import ToDoList, Task

def test_criar_tarefa():
    todo = ToDoList()
    task = todo.add_task("Estudar TDD", "Ler sobre ciclo red-green-refactor")
    
    assert task.title == "Estudar TDD"
    assert task.description == "Ler sobre ciclo red-green-refactor"
    assert task.completed is False

def test_nao_permite_titulo_vazio():
    todo = ToDoList()
    with pytest.raises(ValueError):
        todo.add_task("", "Descrição qualquer")

def test_nao_permite_titulos_duplicados():
    todo = ToDoList()
    todo.add_task("Treinar", "Ir para academia")
    
    with pytest.raises(ValueError):
        todo.add_task("Treinar", "Outro texto")
import pytest
from src.todo import ToDoList, Task

def test_criar_tarefa():
    todo = ToDoList()
    task = todo.add_task("Estudar TDD", "Ler sobre ciclo red-green-refactor")
    
    assert task.title == "Estudar TDD"
    assert task.description == "Ler sobre ciclo red-green-refactor"
    assert task.completed is False

def test_nao_permite_titulo_vazio():
    todo = ToDoList()
    with pytest.raises(ValueError):
        todo.add_task("", "Descrição qualquer")

def test_nao_permite_titulos_duplicados():
    todo = ToDoList()
    todo.add_task("Treinar", "Ir para academia")
    
    with pytest.raises(ValueError):
        todo.add_task("Treinar", "Outro texto")

def test_listar_tarefas():
    todo = ToDoList()
    todo.add_task("Tarefa 1", "A")
    todo.add_task("Tarefa 2", "B")
    
    tarefas = todo.list_tasks()
    assert len(tarefas) == 2

def test_concluir_tarefa():
    todo = ToDoList()
    todo.add_task("Organizar mesa", "Limpar área de trabalho")

    todo.complete_task("Organizar mesa")
    tarefa = todo.get_task("Organizar mesa")

    assert tarefa.completed is True
import pytest
from src.todo import ToDoList, Task

def test_criar_tarefa():
    todo = ToDoList()
    task = todo.add_task("Estudar TDD", "Ler sobre ciclo red-green-refactor")
    
    assert task.title == "Estudar TDD"
    assert task.description == "Ler sobre ciclo red-green-refactor"
    assert task.completed is False

def test_nao_permite_titulo_vazio():
    todo = ToDoList()
    with pytest.raises(ValueError):
        todo.add_task("", "Descrição qualquer")

def test_nao_permite_titulos_duplicados():
    todo = ToDoList()
    todo.add_task("Treinar", "Ir para academia")
    
    with pytest.raises(ValueError):
        todo.add_task("Treinar", "Outro texto")

def test_listar_tarefas():
    todo = ToDoList()
    todo.add_task("Tarefa 1", "A")
    todo.add_task("Tarefa 2", "B")
    
    tarefas = todo.list_tasks()
    assert len(tarefas) == 2

def test_concluir_tarefa():
    todo = ToDoList()
    todo.add_task("Organizar mesa", "Limpar área de trabalho")

    todo.complete_task("Organizar mesa")
    tarefa = todo.get_task("Organizar mesa")

    assert tarefa.completed is True

def test_remover_tarefa():
    todo = ToDoList()
    todo.add_task("Dormir cedo", "Ir para cama 22h")
    
    todo.remove_task("Dormir cedo")
    
    assert len(todo.list_tasks()) == 0

def test_tarefa_inexistente_nao_conclui():
    todo = ToDoList()
    with pytest.raises(KeyError):
        todo.complete_task("algo que não existe")

def test_tarefa_inexistente_nao_remove():
    todo = ToDoList()
    with pytest.raises(KeyError):
        todo.remove_task("inexistente")
