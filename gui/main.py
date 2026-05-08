import tkinter as tk
from utils.config import config

from init import init, check_path
from gui.pages.settings import open_settings_window

from utils.watchdog import run_watchdog, stop_watchdog
from gui.pages.extensions import open_extensions_window


def open_settings():
    open_settings_window(main_window)


def run():
    result = check_path()
    if result == "NEED_CONFIG":
        open_settings()
    elif result == "SUCCESS":
        run_watchdog()


def upgate_ui(event=None):
    global lang
    lang = config.get_language()
    btn_settings.config(text=lang["btn_settings"])
    btn_run.config(text=lang["btn_run"])
    btn_stop.config(text=lang["btn_stop"])


def stop():
    stop_watchdog()


def open_extensions():
    open_extensions_window(main_window)


lang = config.get_language()

# 1. Создаем главное окно
main_window = tk.Tk()
main_window.title("Path Filter")
main_window.geometry("500x200")  # Устанавливаем размер окна
main_window.bind("<<LanguageChanged>>", upgate_ui)

btn_settings = tk.Button(main_window, text=lang["btn_settings"], command=open_settings)
btn_settings.pack(pady=10)

btn_run = tk.Button(main_window, text=lang["btn_run"], command=run)
btn_run.pack(pady=10)

btn_stop = tk.Button(main_window, text=lang["btn_stop"], command=stop)
btn_stop.pack(pady=10)

btn_extensions = tk.Button(main_window, text="Extensions", command=open_extensions)
btn_extensions.pack(pady=10)

# 3. Запускаем цикл обработки событий
main_window.mainloop()
