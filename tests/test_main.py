import unittest

from main.main import adding

class TestFunctions(unittest.TestCase):
  def test_adding(self):
    self.failUnlessEqual( adding(1,2), 3)

  def test_split_general_frames(self):
    second_sample = "9-9-9-9-9-9-9-9-9-9-"
    third_sample = "5/5/5/5/5/5/5/5/5/5/5"

    frames = []
    for var in range (0,9):
      frames[0]=second_sample[var]+second_sample[var+1]
      var = var + 1



