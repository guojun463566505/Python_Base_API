import unittest
# import sys
# sys.path.append('')
from Unittest.test_case03 import TestCase03
from Unittest.test_case02 import TestCase02
from Unittest.test_case01 import TestCase01
case01 = unittest.TestLoader().loadTestsFromTestCase(TestCase01)
case02 = unittest.TestLoader().loadTestsFromTestCase(TestCase02)
case03 = unittest.TestLoader().loadTestsFromTestCase(TestCase03)
print(case01)
suote = unittest.TestSuite([case01, case02, case03])
unittest.TextTestRunner().run(suote)