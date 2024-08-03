from base_test_case import TestChop
from typing import Callable
import unittest

from iterative import chop

class TestIterativeChop(TestChop):

    @property
    def chopper(self) -> Callable:
        return chop 

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIterativeChop)
    unittest.TextTestRunner().run(suite)
