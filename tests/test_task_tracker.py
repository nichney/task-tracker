import unittest
from unittest.mock import patch, mock_open
import json
import time
from task_tracker import on_add, on_update, on_delete, mark_in_progress, mark_done, open_tasks

class TestTaskTracker(unittest.TestCase):
    
    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    def test_add_task(self, mock_file):
        args = type('', (), {"text": ["Test", "Task"]})()
        with patch("json.load", return_value=[]), patch("json.dump") as mock_json_dump:
            on_add(args)
            mock_json_dump.assert_called_once()
    
    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([{"id": 1, "description": "Old Task", "status": "todo", "createdAt": time.time(), "updatedAt": time.time()}]))
    def test_update_task(self, mock_file):
        args = type('', (), {"id": 1, "text": ["Updated", "Task"]})()
        with patch("json.load", return_value=[{"id": 1, "description": "Old Task", "status": "todo", "createdAt": time.time(), "updatedAt": time.time()}]), patch("json.dump") as mock_json_dump:
            on_update(args)
            mock_json_dump.assert_called_once()
    
    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([{"id": 1, "description": "Task to delete", "status": "todo", "createdAt": time.time(), "updatedAt": time.time()}]))
    def test_delete_task(self, mock_file):
        args = type('', (), {"id": 1})()
        with patch("json.load", return_value=[{"id": 1, "description": "Task to delete", "status": "todo", "createdAt": time.time(), "updatedAt": time.time()}]), patch("json.dump") as mock_json_dump:
            on_delete(args)
            mock_json_dump.assert_called_once()
    
    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([{"id": 1, "description": "Task", "status": "todo", "createdAt": time.time(), "updatedAt": time.time()}]))
    def test_mark_in_progress(self, mock_file):
        args = type('', (), {"id": 1})()
        with patch("json.load", return_value=[{"id": 1, "description": "Task", "status": "todo", "createdAt": time.time(), "updatedAt": time.time()}]), patch("json.dump") as mock_json_dump:
            mark_in_progress(args)
            mock_json_dump.assert_called_once()
    
    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([{"id": 1, "description": "Task", "status": "in-progress", "createdAt": time.time(), "updatedAt": time.time()}]))
    def test_mark_done(self, mock_file):
        args = type('', (), {"id": 1})()
        with patch("json.load", return_value=[{"id": 1, "description": "Task", "status": "in-progress", "createdAt": time.time(), "updatedAt": time.time()}]), patch("json.dump") as mock_json_dump:
            mark_done(args)
            mock_json_dump.assert_called_once()
    
if __name__ == "__main__":
    unittest.main()

