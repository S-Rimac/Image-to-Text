from PIL import Image
import pytesseract
from docx import Document

# Load the image
image_path = 'image.jpg'
image = Image.open(image_path)

# Extract text from the image using Tesseract
text = pytesseract.image_to_string(image)

# Create a new Word document
doc = Document()

# Add the extracted text to the Word document
doc.add_paragraph(text)

# Save the Word document
output_file = 'output.docx'
doc.save(output_file)

print(f'Saved extracted text to {output_file} successfully!')
