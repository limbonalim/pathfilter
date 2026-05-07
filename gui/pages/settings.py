from tkinter import filedialog
import tkinter as tk
from tkinter import ttk


from utils.config import config

# 1. Читаем файл config
lang = config.get_language()
data = config.get_config()
default_config = config.get_default_config()


def open_settings_window(main_window):
    # Изменение заначения edit
    def change_entry_value(value):
        path_entry.config(state="normal")
        path_entry.delete(0, tk.END)
        path_entry.insert(0, value)
        path_entry.config(state="readonly")

    # Создаем окно настроек
    settings_window = tk.Toplevel(main_window)
    settings_window.title("Настройки")
    settings_window.geometry("300x400")

    # Добавляем элементы окно настроек
    label = tk.Label(settings_window, text="Нажмите, чтобы выбрать путь:")
    label.pack(pady=10)

    path_entry = tk.Entry(settings_window, width=40)
    change_entry_value(data["path"])
    path_entry.pack(pady=10)

    # Выбор папки
    def choose_folder():
        global data
        btn_save.config(state="normal")
        folder = filedialog.askdirectory(title="Выберите рабочую директорию")
        if folder:
            data["path"] = folder
            change_entry_value(data["path"])

    # Сброс настроек до default
    def set_default_settings():
        global data
        data = default_config
        btn_save.config(state="normal")
        change_entry_value(default_config["path"])

    # Сохранение настроек
    def save_settings():
        global data
        config.set_config(data)
        change_entry_value(data["path"])
        settings_window.destroy()

    # Отмена
    def cancel():
        settings_window.destroy()

    btn_find_folder = tk.Button(
        settings_window, text=lang["btn_find_folder"], command=choose_folder
    )
    btn_find_folder.pack(pady=10)

    btn_set_default = tk.Button(
        settings_window, text=lang["btn_set_default"], command=set_default_settings
    )
    btn_set_default.pack(pady=10)

    btn_save = tk.Button(
        settings_window, text=lang["btn_save"], command=save_settings, state="disabled"
    )
    btn_save.pack(pady=10)

    btn_cancel = tk.Button(settings_window, text=lang["btn_cancel"], command=cancel)
    btn_cancel.pack(pady=10)

    # lang_map = {item["name"]: item["code"] for item in data["language-list"]}
    # def on_select(event):
    #     selected_name = combo.get()  # Получаем текст (напр. "Russian")
    #     selected_code = lang_map.get(selected_name)  # Достаем код (напр. "RU")

    #     print(f"Отображается: {selected_name}")
    #     print(f"Используется код: {selected_code}")
    #     label.config(text=f"Код для сервера: {selected_code}")

    # combo = ttk.Combobox(settings_window, values=lang_map)
    # # combo.current(0)
    # combo.bind("<<ComboboxSelected>>", on_select)
    # combo.pack(pady=20)

    languages = ["ENG", "RU"]

    def on_select(event):
        # Получаем выбранное значение
        selected = combo.get()
        print(f"Выбран язык: {selected}")

        data["language"] = selected
        btn_save.config(state="normal")

    combo = ttk.Combobox(settings_window, values=languages)
    combo.bind("<<ComboboxSelected>>", on_select)
    combo.current(languages.index(data["language"]))
    combo.pack(pady=20)
