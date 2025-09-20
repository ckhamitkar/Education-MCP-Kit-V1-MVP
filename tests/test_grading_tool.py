import unittest
import os
import sys

# Add the parent directory to the path to find the mcp_tools package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mcp_tools import grading_tool

class TestGradingTool(unittest.TestCase):

    def test_grade_short_answer(self):
        rubric = {
            'clarity': {'keyword': 'clear', 'points': 2},
            'evidence': {'keyword': 'supported', 'points': 3}
        }
        answer = "The argument is clear and supported by evidence."
        result = grading_tool.grade_short_answer('test_user', answer, rubric)
        self.assertEqual(result['score'], 5)

    def test_grade_short_answer_partial(self):
        rubric = {
            'clarity': {'keyword': 'clear', 'points': 2},
            'evidence': {'keyword': 'supported', 'points': 3}
        }
        answer = "The argument is clear."
        result = grading_tool.grade_short_answer('test_user', answer, rubric)
        self.assertEqual(result['score'], 2)

if __name__ == '__main__':
    unittest.main()
