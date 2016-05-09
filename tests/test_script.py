from __future__ import print_function

import os
import jupyter
import unittest
from jupythemer import jupythemer
from jupythemer.jupythemer import custom_css_filepath
from collections import namedtuple


class TestScript(unittest.TestCase):

    def setUp(self):
        self.backup = ''
        with open(custom_css_filepath, 'r') as f:
            self.backup = f.read()

    def tearDown(self):
        with open(custom_css_filepath, 'w') as f:
            f.write(self.backup)

    def test_color(self):
        args = namedtuple('args', ('color', 'layout', 'typography', 'font', 'background'))
        jupythemer.run(args('neo', None, None, None, None))


if __name__ == '__main__':
    print('Test script')
    unittest.main()
