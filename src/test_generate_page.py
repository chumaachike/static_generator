import unittest
from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_basic_h1(self):
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_h1_with_extra_spaces(self):
        markdown = "#    Hello World   "
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_h1_with_other_headers(self):
        markdown = "## Subtitle\n# Main Title\n### Another"
        self.assertEqual(extract_title(markdown), "Main Title")

    def test_no_h1(self):
        markdown = "## Subtitle\n### Smaller Title"
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_multiple_h1(self):
        markdown = "# First Title\n# Second Title"
        self.assertEqual(extract_title(markdown), "First Title")

    def test_h1_not_followed_by_space(self):
        markdown = "#HelloWithoutSpace"
        with self.assertRaises(ValueError):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()

