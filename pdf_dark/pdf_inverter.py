import fitz  # PyMuPDF
from PIL import Image, ImageOps
import os
import sys

def invert_pdf_colors(input_pdf, output_pdf):
    try:
        # Check if input file exists
        if not os.path.exists(input_pdf):
            raise FileNotFoundError(f"Input file '{input_pdf}' not found")

        # Check if input file is PDF
        if not input_pdf.lower().endswith('.pdf'):
            raise ValueError(f"Input file '{input_pdf}' must be a PDF file")

        # Open and process the PDF
        doc = fitz.open(input_pdf)
        print(f"Processing {len(doc)} pages...")

        for page_number in range(len(doc)):
            print(f"Inverting page {page_number + 1}/{len(doc)}")
            pix = doc[page_number].get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            inverted_img = ImageOps.invert(img)  # Invert colors
            pix = fitz.Pixmap(doc, page_number, inverted_img.tobytes("raw", "RGB"))
            doc[page_number].insert_image(doc[page_number].rect, pixmap=pix)

        print(f"Saving inverted PDF to '{output_pdf}'...")
        doc.save(output_pdf)
        doc.close()
        print("Done!")
        return True

    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def main():
    if len(sys.argv) > 2:
        input_pdf = sys.argv[1]
        output_pdf = sys.argv[2]
    else:
        input_pdf = input("Enter input PDF path (or press Enter for 'input.pdf'): ").strip() or "input.pdf"
        output_pdf = input("Enter output PDF path (or press Enter for 'dark_mode.pdf'): ").strip() or "dark_mode.pdf"

    success = invert_pdf_colors(input_pdf, output_pdf)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()