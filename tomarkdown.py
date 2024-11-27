from docling.document_converter import DocumentConverter
import re
import os

def convert_to_markdown(pdf_path):
    # Extract author and year from filename
    basename = os.path.basename(pdf_path)
    match = re.search(r'(.*?) et al\. - (\d{4})', basename)
    author = match.group(1) if match else "Unknown"
    year = match.group(2) if match else "Unknown"
    
    # Convert document
    converter = DocumentConverter()
    result = converter.convert(pdf_path)
    
    # Generate markdown content
    markdown_content = result.document.export_to_markdown()
    
    # Create output filename
    output_filename = f"{author}_{year}.md"
    
    # Write to file
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    return output_filename

if __name__ == "__main__":
    source = "/Users/ravitejvenkataswamy/Zotero/storage/BS4WCUBA/Choi et al. - 2019 - Effect of Ceria Abrasive Synthesized by Supercritical Hydrothermal Method for Chemical Mechanical Pl.pdf"
    output_file = convert_to_markdown(source)
    print(f"Markdown file created: {output_file}")
