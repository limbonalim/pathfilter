import tkinter as tk
from utils.config import config

data = config.get_config()
extensions = [extension["name"] for extension in data["extensions"] if extension["isActive"]]


def open_extensions_window(main_window):
    # Создаем окно настроек расширений
    extensions_window = tk.Toplevel(main_window)
    extensions_window.title("Extensions Settings")
    extensions_window.geometry("1000x500")
    # Здесь добавьте элементы управления для настроек расширений

    scroll_container = tk.Frame(extensions_window)
    scroll_container.pack(fill="both", expand=True, padx=10, pady=50)

    global_state = []

    def save_all():
        global data, global_state
        data["config"] = global_state
        config.set_config(data)

    def add_directory(name='', types=[], index=-1):
       ui_group_dir = tk.LabelFrame(scroll_container, text="Настройки папки", padx=5, pady=5)
       ui_group_dir.pack(pady=5, fill="x")

       local_state = {"name": name, "types": types}
       
       extension_vars = {}

       edit = tk.Entry(ui_group_dir, width=30)

       edit.delete(0, tk.END)
       edit.insert(0, name)
       edit.pack(pady=10)

       def on_click(name):
           btn_save.config(state="normal")
           val = extension_vars[name].get()

           for i in range(len(local_state["types"])):
               if local_state["types"][i]["name"] == name:
                   local_state["types"][i]["isActive"] = False if val == 0 else True

       def on_delete():
           global global_state
           global_state.remove(local_state)
           ui_group_dir.destroy()

       def on_save():
            global global_state
            local_state["name"] = edit.get()

            if local_state["name"] != '':
                if index > 0:
                    global_state[index] = local_state
                else:
                    global_state.append(local_state)
            else:
                ui_group_dir.destroy()
           

       for item in extensions:
           default_var = 0
           if types:
               for type in types:
                   if type['name'] == item:
                       default_var = 1 if type['isActive']else 0
           
           var = tk.IntVar(value=default_var)
           extension_vars[item] = var
           new_type = {'name': item, 'isActive': False if default_var == 0 else True}
           local_state['types'].append(new_type)

           check = tk.Checkbutton(ui_group_dir, text=item, variable=var, command=lambda i=item: on_click(i))
           check.pack(side="left", padx=2)
    

       btn_del = tk.Button(ui_group_dir, text="X", fg="red", command=on_delete)
       btn_del.pack(side="right", padx=5)

       btn_save = tk.Button(ui_group_dir, text="Save", command=on_save)
       btn_save.pack(side="right", padx=10)
    

    def init():
        global global_state
        global_state = data["config"]

        for i in range(len(global_state)):
            add_directory(global_state[i]["name"], global_state[i]["types"], i)

    init()
        
    button_plus = tk.Button(
        extensions_window,
        text="+",
        command=add_directory,
        width=2,
        height=1,
    )
    button_plus.place(x=10, y=10)

    global_save_plus = tk.Button(
        extensions_window,
        text="Save All",
        command=save_all,
    )
    global_save_plus.place(x=50, y=10)


