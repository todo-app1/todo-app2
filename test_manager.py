# test_manager.py
import unittest
from logic import Task, TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.manager.add_task(Task("Хлеб", "2025-11-01"))
        self.manager.add_task(Task("Цветы", "2025-11-03"))

    def test_add_and_count(self):
        self.assertEqual(self.manager.count(), 2)

    def test_get_all_returns_copy(self):
        tasks = self.manager.get_all()
        tasks.pop()
        self.assertEqual(self.manager.count(), 2)

    def test_mark_done_and_get_pending(self):
        self.manager.mark_done(0)
        pending = self.manager.get_pending()
        self.assertEqual([t.title for t in pending], ["Цветы"])

    def test_remove_existing(self):
        self.manager.remove_task(0)
        self.assertEqual(self.manager.count(), 1)

    def test_remove_missing_raises(self):
        with self.assertRaises(ValueError):
            self.manager.remove_task(99)

    def test_mark_done_missing_raises(self):
        with self.assertRaises(ValueError):
            self.manager.mark_done(99)

    def test_get_sorted_by_deadline(self):
        self.manager.add_task(Task("Раньше", "2025-10-01"))
        result = self.manager.get_sorted_by_deadline()
        self.assertEqual([t.title for t in result], ["Раньше", "Хлеб", "Цветы"])

if __name__ == "__main__":
    unittest.main()