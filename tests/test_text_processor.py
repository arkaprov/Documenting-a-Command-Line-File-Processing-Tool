import unittest
import sys
import os

# Add the src/ directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from text_processor import count_words, count_chars, count_lines, find_word, replace_word


class TestTextProcessor(unittest.TestCase):

    def setUp(self):
        """Setup a mock text file in memory for testing."""
        self.text = """This is an example file.
        It contains several words, and it is used for testing.
        The word 'example' appears multiple times, and the word 'old' should be replaced."""
        self.file_path = 'sample.txt'

        # Writing the text to a mock file
        with open(self.file_path, 'w') as f:
            f.write(self.text)

    def tearDown(self):
        """Remove the mock text file after the test."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_count_words(self):
        """Test word count function."""
        result = count_words(self.file_path)
        self.assertEqual(result, 28)  # Correct word count

    def test_count_chars(self):
        """Test character count function."""
        result = count_chars(self.file_path)
        self.assertEqual(result, len(self.text))

    def test_count_lines(self):
        """Test line count function."""
        result = count_lines(self.file_path)
        self.assertEqual(result, 3)  # 3 lines in the text

    def test_find_word(self):
        """Test finding a word in the text."""
        result = find_word(self.file_path, 'example')
        self.assertEqual(result, 1)  # 'example' occurs 1 time

    def test_replace_word(self):
        """Test replacing a word in the text."""
        output_file = 'updated_sample.txt'
        replace_word(self.file_path, 'old', 'new', output_file)

        # Check if 'old' has been replaced with 'new' in the output file
        with open(output_file, 'r') as f:
            updated_text = f.read()

        self.assertNotIn('old', updated_text)
        self.assertIn('new', updated_text)

        # Clean up the output file
        if os.path.exists(output_file):
            os.remove(output_file)


if __name__ == '__main__':
    unittest.main()
