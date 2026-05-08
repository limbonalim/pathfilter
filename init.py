import os
import time

from utils.setup_folders import SetupFolders
from utils.config import config


def check_path():
    data = config.get_config()
    const_path = data["path"]
    if not const_path or const_path == "Выберите папку для работы":
        return "NEED_CONFIG"
    else:
        return "SUCCESS"


def try_delete_file(file):
    number_of_attempts = 5
    second = 1
    for _ in range(number_of_attempts):
        try:
            if os.path.exists(file):
                os.remove(file)
                break
        except PermissionError:
            time.sleep(second)
        except Exception as e:
            print(f"Error deleting file {file}: {e}")
            break


def try_move_file(file, dir_name):
    number_of_attempts = 5
    second = 1
    for _ in range(number_of_attempts):
        try:
            if os.path.exists(file):
                os.rename(file, f"{dir_name}/{file}")
                break
        except PermissionError:
            time.sleep(second)
        except Exception as e:
            print(f"Error moving file {file}: {e}")
            break


def init():
    # Достаем config
    data = config.get_config()

    const_path = data["path"]

    if not const_path or const_path == "Выберите папку для работы":
        return "NEED_CONFIG"
    else:

        config_settings = data["config"]

        # Переходим в рабочую папку
        os.chdir(const_path)

        # Берем все названия файлов в рабочей папке
        file_list = os.listdir(path=".")

        # Настройка для папок
        setup_folders = SetupFolders(config_settings, file_list)
        missing_folders = setup_folders.find_missing_folders()

        # Создаем папки
        for dir in missing_folders:
            os.mkdir(dir)

        # Перемещаем файлы в нужные папки в зависимости от расширения
        for c in config_settings:
            dir_name = c["name"]

            category = []
            for type in c["types"]:
                if type["isActive"]:
                    category.append(type["name"])

            for file in file_list:
                extension = file.split(".")[-1].lower()

                if extension in category:
                    if not os.path.exists(f"{dir_name}/{file}"):
                        try_move_file(file, dir_name)
                    else:
                        try_delete_file(file)

        return "SUCCESS"
