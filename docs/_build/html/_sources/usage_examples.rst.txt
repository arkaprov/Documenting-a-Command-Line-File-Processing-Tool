Usage Example
=============

This section provides an example of how to use the `text_processor.py` command-line tool, including screenshots of the input command and the corresponding output.

Example: Processing a Text File
-------------------------------

In this example, we will run the `text_processor.py` command with multiple flags to process a text file named `sample.txt`.

**Command Input:**

To process the text file and display the word count, character count, and find/replace words, you would run the following command in your terminal:

.. code-block:: bash

    python src/text_processor.py -f sample.txt -wc -cc -find "example" -r "old" "new"

.. image:: _static/input.jpg
   :alt: Command to process the text file
   :align: center
   :width: 70%

**Command Output:**

The expected output after running the command will display the results of the operations performed on the text file:

.. image:: _static/output.jpg
   :alt: Output showing word count and other results
   :align: center
   :width: 70%

The output should look like this.

