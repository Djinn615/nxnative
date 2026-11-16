"""The pinned tool requirements install the zstd module the tools import.

Python 3.14 has compression.zstd. Older Pythons need backports.zstd, which is a different package from zstandard (the one nsz imports).
docs/development.md installs this file into the venv used for every game.
"""
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
TOOLS = REPO / '.github/requirements/tools.txt'


class Requirements(unittest.TestCase):
    def test_backports_zstd_is_pinned_before_python_3_14(self):
        text = TOOLS.read_text()
        line = next(l for l in text.splitlines() if l.startswith('backports.zstd=='))
        self.assertIn('python_version < "3.14"', line)
        self.assertNotIn('zstandard', line)


if __name__ == '__main__':
    unittest.main()
