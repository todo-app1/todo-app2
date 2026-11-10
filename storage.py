# storage.py
import json
import os
from logic import Task

class Storage:
    def __init__(self, path: str = "tasks.json"):
        self.path = path

    def save(self, tasks: list[Task]) -> None:
        data = [task.to_dict() for task in tasks]
        backup_path = f"{self.path}.bak"
        if os.path.exists(self.path):
            try:
                os.replace(self.path, backup_path)
            except OSError:
                pass

        try:
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            if os.path.exists(backup_path):
                os.remove(backup_path)
        except Exception:
            if os.path.exists(backup_path):
                os.replace(backup_path, self.path)
            raise

    def load(self) -> list[Task]:
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as e:
            raise ValueError(f"Файл задач поврежден: {e}") from e

        if not isinstance(data, list):
            raise ValueError("Файл задач поврежден: внутри должен быть список")
        
        return [Task.from_dict(item) for item in data]