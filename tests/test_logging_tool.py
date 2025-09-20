import unittest
import os
import json
import sys

# Add the parent directory to the path to find the mcp_tools package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mcp_tools import logging_tool

class TestLoggingTool(unittest.TestCase):

    def setUp(self):
        self.log_file = logging_tool.LOG_FILE
        # Ensure the logs directory exists
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_action(self):
        logging_tool.log_action('test_user', 'test_action', {'detail': 'test'})
        self.assertTrue(os.path.exists(self.log_file))
        with open(self.log_file, 'r') as f:
            log_entry = json.loads(f.readline())
            self.assertEqual(log_entry['user'], 'test_user')
            self.assertEqual(log_entry['action'], 'test_action')

    def tearDown(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

if __name__ == '__main__':
    unittest.main()
