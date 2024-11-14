
# PDF Book Chapter Splitter

This Python script splits a PDF book into individual chapters based on the table of contents (TOC). It uses OpenAI's GPT-4 to analyze the TOC and extract chapter titles and page ranges, then splits the book into separate PDF files for each chapter.

## Usage

The script takes a PDF file as input, analyzes its table of contents, and splits the book into individual chapters.

### Command-line Arguments

```bash
python3 split_chapterwise.py <pdf_path> <actual_page> <listed_page> [--output-dir <output_dir>]
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


## License

This project is licensed under the MIT License.

---

### Author

Sehaj + Gpt4 
