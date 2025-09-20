import unittest
import os
import sys

# Add the parent directory to the path to find the mcp_tools package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mcp_tools import quizgen_tool

class TestQuizgenTool(unittest.TestCase):

    def test_generate_quiz(self):
        text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
        quiz = quizgen_tool.generate_quiz('test_user', text, num_questions=2)
        self.assertIsInstance(quiz, list)
        self.assertEqual(len(quiz), 2)
        self.assertIn('question', quiz[0])
        self.assertIn('options', quiz[0])
        self.assertIn('answer', quiz[0])
        self.assertEqual(len(quiz[0]['options']), 4)

    def test_generate_quiz_short_text(self):
        text = "Too short."
        result = quizgen_tool.generate_quiz('test_user', text)
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()
