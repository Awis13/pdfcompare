import sys
import fitz  # PyMuPDF
import difflib

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to compare two texts and return a list of differences
def compare_texts(text1, text2):
    d = difflib.Differ()
    diff = list(d.compare(text1.splitlines(), text2.splitlines()))
    return diff

# Function to display the differences in a readable format
def display_diff(diff):
    for line in diff:
        if line.startswith('- '):
            print('\033[91m' + line + '\033[0m')  # Red color for removed lines
        elif line.startswith('+ '):
            print('\033[92m' + line + '\033[0m')  # Green color for added lines
        else:
            print(line)

# Main function
if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python compare_pdfs.py file1.pdf file2.pdf")
        sys.exit(1)

    # Get the file paths from command line arguments
    file1, file2 = sys.argv[1], sys.argv[2]

    # Extract text from the PDF files
    text1 = extract_text_from_pdf(file1)
    text2 = extract_text_from_pdf(file2)

    # Compare the extracted texts
    diff = compare_texts(text1, text2)

    # Display the differences
    display_diff(diff)
