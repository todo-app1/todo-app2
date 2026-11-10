# logic.py
import datetime

class Task:
    def __init__(self, title: str, deadline: str, done: bool = False):
        # Проверка названия
        if not title.strip():
            raise ValueError("Название дела не может быть пустым")
        
        # Задание 4.2: Проверка даты
        try:
            datetime.datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Срок должен быть в формате ГГГГ-ММ-ДД (например, 2026-11-10)")
        
        self.title = title
        self.deadline = deadline
        self.done = done

    def __str__(self):
        status = "x" if self.done else " "
        return f"[{status}] {self.title} (срок: {self.deadline})"

    # Задание 1.1: Превращаем объект в словарь
    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "deadline": self.deadline,
            "done": self.done
        }

    # Задание 1.1: Собираем объект из словаря
    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(data["title"], data["deadline"], data.get("done", False))


class TaskManager:
    def __init__(self, storage=None):
        self.storage = storage
        self.tasks: list[Task] = []

    def load(self):
        if self.storage:
            self.tasks = self.storage.load()

    def save(self):
        if self.storage:
            self.storage.save(self.get_all())

    # --- Методы управления (из лаб №5) ---
    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
        # Задание 4.1* (Автосохранение): раскомментируй строку ниже, если нужно
        # self.save()

    def remove_task(self, index: int) -> None:
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            # self.save()

    def mark_done(self, index: int) -> None:
        if 0 <= index < len(self.tasks):
            self.tasks[index].done = True
            # self.save()

    def get_all(self):
        return self.tasks

    def get_pending(self):
        return [t for t in self.tasks if not t.done]

    def count(self):
        return len(self.tasks)