# logic.py
import datetime

class Task:
    def __init__(self, title: str, deadline: str, done: bool = False):
        clean_title = title.strip()
        if not clean_title:
            raise ValueError("Название дела не может быть пустым")
        
        try:
            datetime.datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Срок должен быть в формате ГГГГ-ММ-ДД (например, 2026-11-10)")
        
        self.title = clean_title
        self.deadline = deadline
        self.done = done

    def __str__(self):
        status = "x" if self.done else " "
        return f"[{status}] {self.title} (срок: {self.deadline})"

    def to_dict(self) -> dict:
        return {"title": self.title, "deadline": self.deadline, "done": self.done}

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(data["title"], data["deadline"], data.get("done", False))

    # Метод для теста test_mark_done
    def mark_done(self) -> None:
        self.done = True


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

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def remove_task(self, index: int) -> None:
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            raise ValueError(f"Задача с индексом {index} не найдена")

    # Метод для менеджера (удаляет по индексу)
    def mark_done(self, index: int) -> None:
        if 0 <= index < len(self.tasks):
            self.tasks[index].done = True
        else:
            raise ValueError(f"Задача с индексом {index} не найдена")

    def get_all(self):
        return list(self.tasks)

    def get_pending(self):
        return [t for t in self.tasks if not t.done]

    def count(self):
        return len(self.tasks)

    # Метод для задания 4.1 (сортировка)
    def get_sorted_by_deadline(self):
        return sorted(self.tasks, key=lambda t: t.deadline)