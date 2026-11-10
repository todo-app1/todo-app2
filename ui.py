# ui.py
from logic import Task  # <-- ЭТОЙ СТРОКИ ТЕБЕ НЕ ХВАТАЛО РАНЬШЕ

class ConsoleUI:
    def __init__(self, manager):
        self.manager = manager

    def run(self):
        while True:
            print("\n--- Список дел ---")
            all_tasks = self.manager.get_all()
            if not all_tasks:
                print("Список пуст.")
            else:
                for i, task in enumerate(all_tasks):
                    print(f"{i + 1}. {task}")
            
            print("\nМеню:")
            print("1. Добавить дело")
            print("2. Выполнить дело")
            print("3. Удалить дело")
            print("0. Выход")

            choice = input("Выберите действие: ")

            if choice == "1":
                title = input("Название дела: ")
                deadline = input("Срок (ГГГГ-ММ-ДД): ")
                try:
                    task = Task(title, deadline)
                    self.manager.add_task(task)
                    print("Дело добавлено.")
                except ValueError as e:
                    print(f"Ошибка: {e}")

            elif choice == "2":
                try:
                    num = int(input("Введите номер дела: ")) - 1
                    self.manager.mark_done(num)
                    print("Дело отмечено как выполненное.")
                except (ValueError, IndexError):
                    print("Неверный номер дела.")

            elif choice == "3":
                try:
                    num = int(input("Введите номер дела: ")) - 1
                    self.manager.remove_task(num)
                    print("Дело удалено.")
                except (ValueError, IndexError):
                    print("Неверный номер дела.")

            elif choice == "0":
                break

            else:
                print("Неверный выбор. Попробуйте снова.")