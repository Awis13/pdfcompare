import sys
import fitz  # PyMuPDF
import difflib

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def compare_texts(text1, text2):
    d = difflib.Differ()
    diff = list(d.compare(text1.splitlines(), text2.splitlines()))
    return diff

def display_diff(diff):
    for line in diff:
        if line.startswith('- '):
            print('\033[91m' + line + '\033[0m')  # Red color for removed lines
        elif line.startswith('+ '):
            print('\033[92m' + line + '\033[0m')  # Green color for added lines
        else:
            print(line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_pdfs.py file1.pdf file2.pdf")
        sys.exit(1)

    file1, file2 = sys.argv[1], sys.argv[2]

    text1 = extract_text_from_pdf(file1)
    text2 = extract_text_from_pdf(file2)

    diff = compare_texts(text1, text2)
    display_diff(diff)
