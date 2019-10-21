import os
import unittest

from plugins.field_removal import TWI101, checker

from .utils import tokenize_and_invoke_checker

TESTCASE_FILENAME = os.path.join(os.path.dirname(__file__), 'test_cases/field_removal.py')


class FieldRemovalPluginTestCase(unittest.TestCase):
    def testChecker(self):
        items = tokenize_and_invoke_checker(TESTCASE_FILENAME, checker)

        self.assertEqual(len(items), 6)
        self.assertEqual(items[0], f'13:19: {TWI101}')
        self.assertEqual(items[1], f'17:19: {TWI101}')
        self.assertEqual(items[2], f'19:8: {TWI101}')
        self.assertEqual(items[3], f'23:19: {TWI101}')
        self.assertEqual(items[4], f'28:19: {TWI101}')
        self.assertEqual(items[5], f'39:37: {TWI101}')
