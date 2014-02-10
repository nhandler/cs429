import unittest
import test_menu

suite = unittest.TestSuite((test_menu.suite()))

runner = unittest.TextTestRunner()
runner.run(suite)
