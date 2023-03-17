## PDF Text Comparison Tool

This script compares the text content of two PDF files and displays the differences between them. It's a simple and convenient way to check for differences in text without the need for any complicated software.

## Features

Extracts and compares text from two PDF files
Displays added lines in green
Displays removed lines in red
Works with Python 3
Requirements

Python 3.x
PyMuPDF library
Installation

First, make sure you have Python 3 installed on your computer. You can download it from the official website.

Next, install the PyMuPDF library using pip:

```bash
pip install PyMuPDF
```
Usage

Save the script as "compare_pdfs.py". You can use it from the command line by providing two PDF files as arguments:

```bash
python compare_pdfs.py file1.pdf file2.pdf
```
The script will display the differences between the texts of the two PDFs, marking removed lines in red and added lines in green.

Limitations

This script compares text content and does not handle formatting, images, or other non-text elements. The comparison is line by line, so small changes in one line may cause the entire line to be marked as different.

License

This project is open-source and available for anyone to use and modify. Feel free to fork and contribute to the project.

Contributions

Pull requests and contributions are welcome. If you find any bugs or have suggestions for improvements, please open an issue on GitHub.
