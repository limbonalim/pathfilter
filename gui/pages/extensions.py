import tkinter as tk


def open_extensions_window(main_window):
    # Создаем окно настроек расширений
    extensions_window = tk.Toplevel(main_window)
    extensions_window.title("Extensions Settings")
    extensions_window.geometry("500x500")
    # Здесь добавьте элементы управления для настроек расширений

    def add_directory():
        ui_group = tk.LabelFrame(extensions_window)
        ui_group.pack(pady=10, padx=10, fill="x")
        ui_group.place(x=50, y=0)

        eddit = tk.Entry(ui_group, width=30)
        eddit.pack(pady=10)

        check = tk.Checkbutton(ui_group, text="jpg")
        check.pack(pady=10)

        check_e = tk.Checkbutton(ui_group, text="exe")
        check_e.pack(pady=10)
        
    button_plus = tk.Button(
        extensions_window,
        text="+",
        command=add_directory,
        width=2,
        height=1,
    )
    button_plus.pack(pady=10)
    button_plus.place(x=10, y=10)
