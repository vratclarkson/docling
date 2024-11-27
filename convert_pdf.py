from docling.document_converter import DocumentConverter
import os

def main():
    source = "/Users/ravitejvenkataswamy/Zotero/storage/G4BDSGYX/Pirson et al. - 2023 - The Environmental Footprint of IC Production Revi.pdf"
    
    # Check if source file exists
    if not os.path.exists(source):
        print(f"Error: Source file not found at {source}")
        return
    
    print(f"Converting PDF file: {source}")
    
    try:
        converter = DocumentConverter()
        print("Created DocumentConverter instance")
        
        result = converter.convert(source)
        print("Successfully converted document")
        
        md_output = result.document.export_to_markdown()
        print("Generated markdown output")
        
        output_file = "output.md"
        with open(output_file, "w") as f:
            f.write(md_output)
        print(f"Successfully wrote markdown to {output_file}")
        
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        raise

if __name__ == "__main__":
    main()
