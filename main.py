# main.py
from ui import ConsoleUI
from logic import TaskManager
from storage import Storage

def main():
    storage = Storage("tasks.json")
    manager = TaskManager(storage)
    
    try:
        manager.load()
    except ValueError as e:
        print(f"⚠️ Предупреждение: {e}")
        print("Начинаем с пустого списка дел.\n")

    ui = ConsoleUI(manager)
    ui.run()

    manager.save()
    print("\n✅ Данные сохранены. До свидания!")

if __name__ == "__main__":
    main()