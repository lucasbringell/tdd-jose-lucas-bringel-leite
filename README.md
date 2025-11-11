# ✅ To-Do List — Desenvolvimento Guiado por Testes (TDD)

Este projeto implementa um **Gerenciador de Tarefas (To-Do List)** utilizando a metodologia **TDD — Test-Driven Development**, seguindo rigorosamente o ciclo:

> **RED → GREEN → REFACTOR**

A aplicação foi desenvolvida em Python, com testes automatizados usando **PyTest**.

---

## 📌 Objetivo do Projeto

O sistema permite:

- Criar tarefas  
- Listar tarefas cadastradas  
- Marcar tarefas como concluídas  
- Remover tarefas  
- Impedir títulos duplicados  
- Impedir criação de tarefas sem título  

Este projeto faz parte de uma atividade prática cujo foco está no desenvolvimento incremental guiado por testes, com commits pequenos e frequentes representando cada etapa do ciclo TDD.

---

## 🧪 Tecnologias Utilizadas

- **Python 3.x**
- **PyTest** (framework de testes)
- Git/GitHub para controle de versões

---

## 🧱 Estrutura do Projeto

tdd-lucas-leite/
├── src/
│ └── todo.py
│
├── tests/
│ └── test_todo.py
│
├── README.md


- **src/** contém o código da aplicação  
- **tests/** contém os testes unitários  
- O projeto usa módulos simples e independentes para facilitar manutenção e testes

---

## ✅ Funcionalidades Implementadas

### ✔ Criar tarefa
- Requer título obrigatório
- Descrição opcional
- Inicia com status *pendente*

### ✔ Impedir títulos duplicados
- O sistema não permite criar duas tarefas com o mesmo nome

### ✔ Listar tarefas cadastradas
- Retorna todas as tarefas como objetos `Task`

### ✔ Marcar tarefa como concluída
- Atualiza o status para *True*

### ✔ Remover tarefa
- Remove pelo título
- Lança erro se não existir

### ✔ Tratamento de exceções
- `ValueError` para campos inválidos
- `KeyError` para tarefas inexistentes

