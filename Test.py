import FreeSimpleGUI as sg


label = sg.Text("Enter Todos")
text_box = sg.InputText(tootltip="Enter todo")
btn = sg.Button("Add")

window = sg.Window('My To-do app', layout=[[label,text_box],[btn]],
                   font=('Helvetica', 20))

window.read()
window.close()