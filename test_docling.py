from docling.document_converter import DocumentConverter

# Create a simple text file to test conversion
with open('test.txt', 'w') as f:
    f.write('Hello, this is a test document for Docling!')

# Convert the document
converter = DocumentConverter()
result = converter.convert('test.txt')
print(result.document.export_to_markdown())
