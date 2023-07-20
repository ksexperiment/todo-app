import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="existing_todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[label], [input_box, add_button], [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 13))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["existing_todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["existing_todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window["existing_todos"].update(values=todos)
        case "Complete":
            todo_to_complete = values["existing_todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["existing_todos"].update(values=todos)
            window["todo"].update(value="")
        case "Exit":
            break
        case "existing_todos":
            window["todo"].update(value=values["existing_todos"][0])
        case sg.WIN_CLOSED:
            break

window.close()