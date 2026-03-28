import os
import sys

def run_test():
    # 1. Создаем файл "отпечаток" в той же папке
    filename = "youwashacked.txt"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("You was hacked! Это учебный тест безопасности.")
        print(f"Файл {filename} успешно создан.")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")

    # 2. Самоудаление
    # Получаем путь к текущему запущенному скрипту
    current_file = sys.argv[0]
    
    print("Запускаю процесс самоудаления...")
    try:
        # Команда ОС на удаление файла
        os.remove(current_file)
        print("Скрипт успешно удалился.")
    except Exception as e:
        print(f"Не удалось удалить файл (возможно, нет прав): {e}")

if __name__ == "__main__":
    run_test()
