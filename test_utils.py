import os
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from utils import clean_string, parse_id_range, parse_lines, read_input


class TestUtils(unittest.TestCase):
    def test_clean_string(self):
        self.assertEqual(clean_string("  hello world  "), "hello world")
        self.assertEqual(clean_string("  \n  hello  \n  "), "hello")
        self.assertEqual(clean_string("\n    indented\n    text\n"), "indented\ntext")

    def test_parse_id_range(self):
        self.assertEqual(parse_id_range("1-5"), range(1, 6))
        self.assertEqual(parse_id_range("10-12"), range(10, 13))
        self.assertEqual(parse_id_range("5-5"), range(5, 6))

    def test_parse_lines(self):
        self.assertEqual(parse_lines(int, "1\n2\n3"), [1, 2, 3])
        self.assertEqual(parse_lines(str.upper, "hello\nworld"), ["HELLO", "WORLD"])

    def test_read_input(self):
        with TemporaryDirectory() as tmpdir:
            resources_dir = Path(tmpdir) / "resources"
            resources_dir.mkdir()
            test_file = resources_dir / "1.txt"
            test_file.write_text("test content", "utf8")

            # Temporarily change working directory for this test
            original_cwd = os.getcwd()
            try:
                os.chdir(tmpdir)
                content = read_input(1)
                self.assertEqual(content, "test content")
            finally:
                os.chdir(original_cwd)
