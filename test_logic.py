# test_logic.py
import unittest
from logic import Task

class TestTask(unittest.TestCase):
    def test_default_not_done(self):
        task = Task("Дело", "2025-11-01")
        self.assertFalse(task.done)

    def test_mark_done(self):
        task = Task("Дело", "2025-11-01")
        task.mark_done()
        self.assertTrue(task.done)

    def test_title_is_stripped(self):
        task = Task("  Хлеб  ", "2025-11-01")
        self.assertEqual(task.title, "Хлеб")

    def test_empty_title_raises(self):
        with self.assertRaises(ValueError):
            Task("", "2025-11-01")

    def test_spaces_only_title_raises(self):
        with self.assertRaises(ValueError):
            Task("   ", "2025-11-01")

if __name__ == "__main__":
    unittest.main()