# main.py
from logic import TaskManager
from storage import Storage
from ui import ConsoleUI

def main():
    # Создаем хранилище, которое будет работать с файлом tasks.json
    storage = Storage("tasks.json")
    
    # Передаем хранилище менеджеру
    manager = TaskManager(storage)

    try:
        manager.load() # Пытаемся прочитать файл
    except ValueError as e:
        # Если файл битый, говорим об этом пользователю
        print(f"⚠️ Предупреждение: {e}")
        print("Начинаем с пустого списка дел.\n")

    # Запускаем меню
    ui = ConsoleUI(manager)
    ui.run()

    # Когда вышли из меню (нажали "0"), сохраняем данные
    manager.save()
    print("\n✅ Данные сохранены. До свидания!")

if __name__ == "__main__":
    main()
    