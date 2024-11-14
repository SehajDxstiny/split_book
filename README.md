# PDF Book Chapter Splitter

This Python script splits a PDF book into individual chapters based on the table of contents (TOC). It uses OpenAI's GPT-4 to analyze the TOC and extract chapter titles and page ranges, then splits the book into separate PDF files for each chapter.

## Features
- Extracts the first 15 pages of a PDF to analyze the table of contents.
- Uses GPT-4 to identify chapter titles and their respective page ranges.
- Adjusts page numbers based on the actual start page of Chapter 1 in the PDF.
- Splits the book into individual chapter PDFs and saves them to a specified directory.

## Requirements

- Python 3.6+
- An OpenAI API key (for GPT-4 analysis)
- The following Python packages:
  - `PyPDF2`
  - `openai`
  - `python-dotenv`

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/pdf-chapter-splitter.git
   cd pdf-chapter-splitter
