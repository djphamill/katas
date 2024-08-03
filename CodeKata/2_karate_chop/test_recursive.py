from base_test_case import TestChop
from typing import Callable
import unittest

from recursive import chop

class TestRecursiveChop(TestChop):

    @property
    def chopper(self) -> Callable:
        return chop

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRecursiveChop)
    unittest.TextTestRunner().run(suite)

