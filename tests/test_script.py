from __future__ import print_function

import jupyter
import os
import unittest

from collections import namedtuple
from jupythemer import jupythemer
from jupythemer.jupythemer import custom_css_filepath


class TestScript(unittest.TestCase):

    def setUp(self):
        self.backup = ''
        with open(custom_css_filepath, 'r') as f:
            self.backup = f.read()

    def tearDown(self):
        with open(custom_css_filepath, 'w') as f:
            f.write(self.backup)

    def test_color(self):
        args = namedtuple('args', ('color', 'layout', 'typography', 'font', 'background', 'show'))
        jupythemer.run(args('neo', None, None, None, None, None))


if __name__ == '__main__':
    print('Test script')
    unittest.main()
