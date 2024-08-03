from base_test_case import TestChop
from typing import Callable
import unittest

from sub_list import chop

class TestSubListChop(TestChop):

    @property
    def chopper(self) -> Callable:
        return chop 

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSubListChop)
    unittest.TextTestRunner().run(suite)

