# Setup Instructions

To fix the ModuleNotFoundError, please follow these steps:

1. First, install Poetry if not already installed:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. After installing Poetry, run these commands in the project directory:
```bash
# Install all dependencies
poetry install

# Activate the virtual environment
poetry shell
```

3. Once the virtual environment is activated, you can run your script:
```bash
python convert_pdf.py
```

This will ensure all required dependencies, including 'filetype', are properly installed in the project's virtual environment.
