# test_ansibleplaybooks.py
"""
Tests for AnsiblePlaybooks module.
"""

import unittest
from ansibleplaybooks import AnsiblePlaybooks

class TestAnsiblePlaybooks(unittest.TestCase):
    """Test cases for AnsiblePlaybooks class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AnsiblePlaybooks()
        self.assertIsInstance(instance, AnsiblePlaybooks)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AnsiblePlaybooks()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
