import unittest

from main.main import adding

class TestFunctions(unittest.TestCase):
  def test_adding(self):
    self.failUnlessEqual( adding(1,2), 3)

