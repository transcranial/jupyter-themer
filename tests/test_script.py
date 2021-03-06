from __future__ import print_function

import jupyter
import os
import unittest

import tempfile
from collections import namedtuple
from jupythemer import jupythemer
from jupythemer.jupythemer import custom_css_filepath

neo_css = '''/*
    Adapted for jupyter-themer from https://github.com/codemirror
*/

/* neo theme for codemirror */

/* Color scheme */

.CodeMirror {
  background-color:#ffffff;
  color:#2e383c;
  line-height:1.4375;
}
.CodeMirror span.cm-comment { color:#75787b; }
.CodeMirror span.cm-keyword, .CodeMirror span.cm-property { color:#1d75b3; }
.CodeMirror span.cm-atom,.CodeMirror span.cm-number { color:#75438a; }
.CodeMirror span.cm-node,.CodeMirror span.cm-tag { color:#9c3328; }
.CodeMirror span.cm-string { color:#b35e14; }
.CodeMirror span.cm-variable,.CodeMirror span.cm-qualifier { color:#047d65; }


/* Editor styling */

.CodeMirror pre {
  padding:0;
}

.CodeMirror .CodeMirror-gutters {
  border:none;
  border-right:10px solid transparent;
  background-color:transparent;
}

.CodeMirror .CodeMirror-linenumber {
  padding:0;
  color:#e0e2e5;
}

.CodeMirror .CodeMirror-guttermarker { color: #1d75b3; }
.CodeMirror .CodeMirror-guttermarker-subtle { color: #e0e2e5; }

.CodeMirror .CodeMirror-cursor {
  width: auto;
  border: 0;
  background: rgba(155,157,162,0.37);
  z-index: 1;
}

'''


class TestScript(unittest.TestCase):

    def setUp(self):
        self.backup = ''
        if os.path.isfile(custom_css_filepath):
            self.fn = custom_css_filepath
        else:
            _, self.fn = tempfile.mkstemp()

        with open(self.fn, 'r') as f:
            self.backup = f.read()

    def tearDown(self):
        with open(self.fn, 'w') as f:
            f.write(self.backup)

    def test_color(self):
        args = namedtuple('args', ('color', 'layout', 'typography', 'font', 'background', 'show', 'css_path'))
        jupythemer.run(args('neo', None, None, None, None, None, self.fn))
        with open(self.fn, 'r') as f:
            content = f.read()
        print(content)
        self.assertEqual(content, neo_css)


class TestScriptCustomPath(unittest.TestCase):

    def setUp(self):
        _, self.fn = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.fn)

    def test_color(self):
        args = namedtuple('args', ('color', 'layout', 'typography', 'font', 'background', 'show', 'css_path'))

        with open(self.fn, 'r') as f:
            content = f.read()

        self.assertEqual(content, '')

        jupythemer.run(args('neo', None, None, None, None, None, self.fn))
        with open(self.fn, 'r') as f:
            content = f.read()

        self.assertEqual(content, neo_css)


if __name__ == '__main__':
    print('Test script')
    unittest.main()
