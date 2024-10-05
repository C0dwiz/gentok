import secrets
import platform
import hashlib
import os

def generate_token(name):
    """
    Генерирует новый токен и сохраняет его в файл <name>.pkib.

    :param name: Имя файла для сохранения токена (str)
    :return: Сгенерированный токен (str)
    """
    random_bytes = secrets.token_bytes(32)
    random_token = secrets.token_hex(32)

    system_info = platform.system() + platform.node() + platform.version()

    combined_info = random_token + system_info

    hash_object = hashlib.sha256(combined_info.encode())
    final_token = hash_object.hexdigest()

    save_token(final_token, name)

    return final_token

def save_token(token, name):
    """
    Сохраняет токен в файл <name>.pkib.

    :param token: Токен для сохранения (str)
    :param name: Имя файла для сохранения токена (str)
    """
    filename = f"{name}.pkib"
    with open(filename, 'w') as f:
        f.write(token)

def load_token(name):
    """
    Загружает токен из файла <name>.pkib.

    :param name: Имя файла (str)
    :return: Токен из файла (str)
    :raises FileNotFoundError: Если файл не найден
    """
    filename = f"{name}.pkib"
    with open(filename, 'r') as f:
        return f.read().strip()

def check_token(name, input_token):
    """
    Проверяет, соответствует ли введенный токен токену в указанном файле.

    :param name: Имя файла (str)
    :param input_token: Токен, введенный пользователем (str)
    :return: True, если токены совпадают, иначе False
    """
    try:
        saved_token = load_token(name)
        return saved_token == input_token
    except FileNotFoundError:
        print(f"File {name}.pkib not found.")
        return False