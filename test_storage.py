# test_storage.py
import os
import tempfile
import unittest
from logic import Task
from storage import Storage

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.tmpdir.name, "tasks.json")
        self.storage = Storage(self.path)

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_missing_file_returns_empty(self):
        self.assertEqual(self.storage.load(), [])

    def test_save_and_load_roundtrip(self):
        tasks = [Task("Хлеб", "2025-11-01", True), Task("Цветы", "2025-11-03")]
        self.storage.save(tasks)
        loaded = self.storage.load()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].title, "Хлеб")
        self.assertTrue(loaded[0].done)
        self.assertFalse(loaded[1].done)

    def test_corrupted_file_raises(self):
        with open(self.path, "w", encoding="utf-8") as f:
            f.write("{это не json")
        with self.assertRaises(ValueError):
            self.storage.load()

    def test_not_a_list_raises(self):
        with open(self.path, "w", encoding="utf-8") as f:
            f.write('{"title": "вместо списка — словарь"}')
        with self.assertRaises(ValueError):
            self.storage.load()

if __name__ == "__main__":
    unittest.main()