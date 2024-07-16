import streamlit as st
import file_module as fm

# Load todos from file
def load_todos():
    return fm.get_todos()

# Write todos to file
def save_todos(todos):
    fm.write_todos(todos)

# Add a new todo
def add_todo():
    new_todo = st.session_state["new_todo"].strip().capitalize()
    if new_todo:
        todos.append(f'{new_todo}\n')
        save_todos(todos)
        st.session_state["new_todo"] = ""

# Load current todos
todos = load_todos()

# Streamlit app layout
st.title("My To-Do App")
st.subheader("This is my to-do app.")
st.write("Manage your tasks efficiently.")

# Display todos with checkboxes
for i, todo in enumerate(todos):
    if st.checkbox(todo.strip(), key=f"{todo.strip()}_{i}"):
        todos.remove(todo)
        save_todos(todos)
        del st.session_state[f"{todo.strip()}_{i}"]
        st.experimental_rerun()

# Input for new todo
st.text_input(label="", placeholder="Add new to-do", on_change=add_todo, key='new_todo')
