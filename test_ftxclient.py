# test_ftxclient.py
"""
Tests for FTXClient module.
"""

import unittest
from ftxclient import FTXClient

class TestFTXClient(unittest.TestCase):
    """Test cases for FTXClient class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FTXClient()
        self.assertIsInstance(instance, FTXClient)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FTXClient()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
