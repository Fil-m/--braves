import sys
try:
    from PyPDF2 import PdfReader
    reader = PdfReader("test_print.pdf")
    print(f"Total pages: {len(reader.pages)}")
except Exception as e:
    print(f"Error: {e}")
