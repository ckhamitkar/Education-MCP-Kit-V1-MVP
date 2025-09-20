import unittest
import os
import sys

# Add the parent directory to the path to find the mcp_tools package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mcp_tools import classroom_tool

class TestClassroomTool(unittest.TestCase):

    def test_get_assignments(self):
        assignments = classroom_tool.get_assignments('test_user')
        self.assertIsInstance(assignments, list)
        self.assertGreater(len(assignments), 0)
        self.assertIn('id', assignments[0])

    def test_get_students(self):
        students = classroom_tool.get_students('test_user', 'course1')
        self.assertIsInstance(students, list)
        self.assertGreater(len(students), 0)
        self.assertIn('id', students[0])

    def test_post_grade(self):
        result = classroom_tool.post_grade('test_user', 'assign1', 'stud1', 95.5, 'Good job')
        self.assertEqual(result['status'], 'success')

if __name__ == '__main__':
    unittest.main()
