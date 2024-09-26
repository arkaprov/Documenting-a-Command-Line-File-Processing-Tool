# src/text_processor.py

import argparse
import os


def count_words(file_path: str) -> int:
    """
    Count the total number of words in a file.

    Parameters:
        file_path (str): Path to the input text file.

    Returns:
        int: The total number of words in the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, 'r') as f:
        text = f.read()

    return len(text.split())


def count_chars(file_path: str) -> int:
    """
    Count the total number of characters in a file.

    Parameters:
        file_path (str): Path to the input text file.

    Returns:
        int: The total number of characters in the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, 'r') as f:
        text = f.read()

    return len(text)


def count_lines(file_path: str) -> int:
    """
    Count the total number of lines in a file.

    Parameters:
        file_path (str): Path to the input text file.

    Returns:
        int: The total number of lines in the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, 'r') as f:
        lines = f.readlines()

    return len(lines)


def find_word(file_path: str, word: str) -> int:
    """
    Find the frequency of a word in a file.

    Parameters:
        file_path (str): Path to the input text file.
        word (str): The word to search for.

    Returns:
        int: The frequency of the word in the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, 'r') as f:
        text = f.read()

    return text.split().count(word)


def replace_word(file_path: str, old_word: str, new_word: str, output_file: str):
    """
    Replace all occurrences of a word in a file and save to a new file.

    Parameters:
        file_path (str): Path to the input text file.
        old_word (str): The word to replace.
        new_word (str): The word to replace with.
        output_file (str): The path to the output file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, 'r') as f:
        text = f.read()

    new_text = text.replace(old_word, new_word)

    with open(output_file, 'w') as f:
        f.write(new_text)

    print(f"Replaced '{old_word}' with '{new_word}' and saved to {output_file}.")


def main():
    parser = argparse.ArgumentParser(description="Process a text file with various options.")
    parser.add_argument("-f", "--file", required=True, help="The path to the input text file.")
    parser.add_argument("-wc", "--word-count", action="store_true", help="Count the total number of words.")
    parser.add_argument("-cc", "--char-count", action="store_true", help="Count the total number of characters.")
    parser.add_argument("-lc", "--line-count", action="store_true", help="Count the total number of lines.")
    parser.add_argument("-find", "--find", help="Find a word in the file and display its frequency.")
    parser.add_argument("-r", "--replace", nargs=2, metavar=('old_word', 'new_word'),
                        help="Replace a word with another word. Example: -r old new")

    args = parser.parse_args()

    file_path = args.file

    if args.word_count:
        print(f"Word Count: {count_words(file_path)}")

    if args.char_count:
        print(f"Character Count: {count_chars(file_path)}")

    if args.line_count:
        print(f"Line Count: {count_lines(file_path)}")

    if args.find:
        print(f"The word '{args.find}' occurs {find_word(file_path, args.find)} times.")

    if args.replace:
        old_word, new_word = args.replace
        replace_word(file_path, old_word, new_word, "updated_" + os.path.basename(file_path))


if __name__ == "__main__":
    main()
