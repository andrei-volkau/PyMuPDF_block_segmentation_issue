import fitz
import pprint


if __name__ == '__main__':
    filename = 'sample_pdf__not_working.pdf'
    doc = fitz.open(filename)
    for page in doc:
        for b in page.getText("blocks"):
            print("Block", b[-2])
            print(b[4])
            print("-" * 50)