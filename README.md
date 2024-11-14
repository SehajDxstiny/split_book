
```md
# PDF Book Chapter Splitter

This Python script splits a PDF book into individual chapters based on the table of contents (TOC). It uses OpenAI's GPT-4 to analyze the TOC and extract chapter titles and page ranges, then splits the book into separate PDF files for each chapter.

## Features

- Extracts the first 15 pages of a PDF to analyze the table of contents.
- Uses GPT-4 to identify chapter titles and their respective page ranges.
- Adjusts page numbers based on the actual start page of Chapter 1 in the PDF.
- Splits the book into individual chapter PDFs and saves them to a specified directory.

## Requirements

- **Python**: 3.6+
- **OpenAI API Key**: Required for GPT-4 analysis
- **Python Packages**:
  - `PyPDF2`
  - `openai`
  - `python-dotenv`

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/pdf-chapter-splitter.git
cd pdf-chapter-splitter
```

### 2. Create a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up OpenAI API key

Create a `.env` file in the root directory of the project and add your OpenAI API key:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

The script takes a PDF file as input, analyzes its table of contents, and splits the book into individual chapters.

### Command-line Arguments

```bash
python3 splitter.py <pdf_path> <actual_page> <listed_page> [--output-dir <output_dir>]
```

- `<pdf_path>`: Path to the input PDF file.
- `<actual_page>`: The actual page number where Chapter 1 starts in the PDF.
- `<listed_page>`: The page number where Chapter 1 is listed to start in the table of contents.
- `--output-dir`: (Optional) Directory where chapter PDFs will be saved. If not provided, a folder named `book_chapters` will be created in the same directory as the input PDF.

### Example

```bash
python3 splitter.py book.pdf 19 3 --output-dir ./chapters
```

In this example:
- The script will extract chapters from `book.pdf`.
- Chapter 1 actually starts on page 19 in the PDF, but it is listed as starting on page 3 in the table of contents.
- The split chapters will be saved in the `./chapters` directory.

### Output

The script will create separate PDF files for each chapter in the specified output directory. Each file will be named using the format:

```
<start_page>-<chapter_title>.pdf
```

For example:

```
19-Chapter_One.pdf
35-Chapter_Two.pdf
```

## How It Works

1. **Extract First Pages**: The script extracts the first 15 pages of the PDF, which typically includes the table of contents.
2. **Analyze TOC with GPT**: It sends these pages to GPT-4 to analyze and extract chapter titles and their corresponding page ranges.
3. **Adjust Page Numbers**: Since books often have discrepancies between listed and actual page numbers, you provide both, and the script adjusts accordingly.
4. **Split Chapters**: Finally, it splits the book into individual chapter PDFs based on these adjusted page ranges.

## Error Handling

If any errors occur during execution (e.g., invalid file paths or issues with GPT analysis), they will be printed to the console along with an appropriate error message.

## Project Structure

```
pdf-chapter-splitter/
│
├── splitter.py           # Main Python script for splitting PDFs into chapters
├── requirements.txt      # Required Python packages
├── README.md             # Project documentation (this file)
└── .env                  # File storing OpenAI API key (not included in repo)
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.
---

### Author

Sehaj + Gpt4

``` 
