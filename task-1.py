# Завдання 1

# Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії 
# та сортує в піддиректорії, назви яких базуються на розширенні файлів.

# Також візьміть до уваги наступні умови:

# 1. Парсинг аргументів. Скрипт має приймати два аргументи командного рядка: шлях до вихідної директорії 
# та шлях до директорії призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).

# 2. Рекурсивне читання директорій:

# Має бути написана функція, яка приймає шлях до директорії як аргумент.
# Функція має перебирати всі елементи у директорії.
# Якщо елемент є директорією, функція повинна викликати саму себе рекурсивно для цієї директорії.
# Якщо елемент є файлом, він має бути доступним для копіювання.

# 3. Копіювання файлів:

# Для кожного типу файлів має бути створений новий шлях у вихідній директорії, використовуючи розширення файлу для назви піддиректорії.
# Файл з відповідним типом має бути скопійований у відповідну піддиректорію.

# 4. Обробка винятків. Код має правильно обробляти винятки, наприклад, помилки доступу до файлів або директорій.

from pathlib import Path
import shutil
import argparse
import os


def copy_files(source, destination):
    if not destination.exists():
        print("Destination folder was created in the current directory")
        destination.mkdir()

    for current_path in source.iterdir():
        if current_path.is_dir():
            copy_files(current_path, destination)
        else:
            has_access = check_access(current_path)
            is_new_folder_path = create_folder_by_extension(current_path, destination)
            if has_access and is_new_folder_path:
                copy_path = check_dublicates(current_path, is_new_folder_path)

                shutil.copy(current_path, copy_path)


def create_folder_by_extension(file_path, destination_folder):
    file_extension = file_path.suffix.lower()

    if file_extension:
        folder_path = destination_folder.joinpath(file_extension[1:])

        if not folder_path.exists():
            folder_path.mkdir()

        return folder_path

    return None


def check_access(file_path):
    try:
        # Check access to read / write / execite current file
        os.access(file_path, os.R_OK | os.W_OK | os.X_OK)
        return True

    except Exception as e:
        print(f"No access rights: {e}")
        return False


def check_dublicates(file_path, destination_folder):
    file_name = file_path.stem
    file_extension = file_path.suffix

    copy_path = destination_folder / f"{file_name}{file_extension}"

    index = 1
    while copy_path.exists():
        unique_name = f"{file_name}_copy_{index}"
        copy_path = destination_folder / f"{unique_name}{file_extension}"
        index += 1

    return copy_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copying files")

    parser.add_argument(
        "--source",
        default=Path.cwd(),
        type=Path,
        help="The path to the source directory",
        required=False,
    )
    parser.add_argument(
        "--destination",
        default=Path("./dist"),
        type=Path,
        help="The path to the destination directory",
        required=False,
    )

    args = parser.parse_args()

    copy_files(args.source, args.destination)
    print("Copying is complete 🎉")
    