import fitz
import pprint


if __name__ == '__main__':
    filename = 'sample_page.pdf'
    doc = fitz.open(filename)
    for page in doc:
        blocks = page.getText("dict")
        with open('blocks.txt', 'w') as blocks_file:
            blocks_file.write(pprint.pformat(blocks))