Error Handling and Edge Cases
=============================

This section explains the error handling and edge cases in the **Command-Line File Processing Tool**. The program is designed to handle various input errors and edge cases gracefully, ensuring a robust user experience.

1. **File Not Found**
   - If the user provides a file path that does not exist, the program raises a `FileNotFoundError`.
   - Example:

     ```
     python text_processor.py -f nonexistent_file.txt -wc
     ```

     Output:

     ```
     FileNotFoundError: The file nonexistent_file.txt does not exist.
     ```

   The program checks for the file's existence before attempting to perform any operations. If the file does not exist, an appropriate error message is shown.

2. **Missing Required Arguments**
   - If the user fails to provide the `--file` or `-f` argument (which is required), the `argparse` module will automatically display an error message and show the correct usage of the tool.
   - Example:

     ```
     python text_processor.py -wc
     ```

     Output:

     ```
     usage: text_processor.py [-h] -f FILE [-wc] [-cc] [-lc] [-find FIND]
     text_processor.py: error: the following arguments are required: -f/--file
     ```

   This prevents the tool from executing without the necessary input.

3. **Searching for a Word That Doesn't Exist**
   - When the user attempts to find a word that is not present in the text file, the program will simply return `0`, indicating that the word does not occur in the file.
   - Example:

     ```
     python text_processor.py -f sample.txt -find "nonexistent"
     ```

     Output:

     ```
     The word 'nonexistent' occurs 0 times.
     ```

4. **Replacing a Word That Doesn't Exist**
   - If the user tries to replace a word that is not found in the text, the program will still create a new file, but no changes will be made to the content.
   - Example:

     ```
     python text_processor.py -f sample.txt -r "nonexistent" "newword"
     ```

     Output:

     ```
     Replaced 'nonexistent' with 'newword' and saved to updated_sample.txt.
     ```

     The user will receive a message indicating that the word has been replaced, but if the word is not found in the original text, no actual changes occur in the new file.

5. **Edge Case: Empty File**
   - If the input file is empty, the program will return `0` for word count, character count, and line count.
   - Example:

     ```
     python text_processor.py -f empty_file.txt -wc -cc -lc
     ```

     Output:

     ```
     Word Count: 0
     Character Count: 0
     Line Count: 0
     ```

     An empty file does not cause the program to crash, and the output is appropriately adjusted for the lack of content.

6. **Edge Case: Replacing Words with Special Characters**
   - The tool supports replacing words even when special characters are included. For instance, replacing `"old_word!"` with `"new_word"` works seamlessly.
   - Example:

     ```
     python text_processor.py -f sample.txt -r "old_word!" "new_word"
     ```

     The program will replace the word while keeping punctuation intact.

7. **Edge Case: Non-Text File (Binary or Unreadable File)**
   - If the user tries to process a non-text file (e.g., a binary file), the program will raise an appropriate error when attempting to read the file.
   - Example:

     ```
     python text_processor.py -f image.jpg -wc
     ```

     Output:

     ```
     UnicodeDecodeError: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte
     ```

     In this case, the user must ensure the input file is a valid text file.

8. **Edge Case: Large Files**
   - The program is designed to handle large text files efficiently. However, performance may be slower with extremely large files. It is recommended to test the tool with large files and optimize it as necessary (e.g., using streaming approaches for very large files).

9. **Handling Multiple Flags Simultaneously**
   - The tool is capable of handling multiple operations in a single execution, as demonstrated by the following example:

     ```
     python text_processor.py -f sample.txt -wc -cc -lc -find "example" -r "old" "new"
     ```

     Output:

     ```
     Word Count: 1200
     Character Count: 7200
     Line Count: 150
     The word "example" occurs 5 times.
     Replaced 'old' with 'new' and saved to updated_sample.txt.
     ```

     The order of operations follows the order of arguments passed to the program.


---


