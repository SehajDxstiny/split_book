#!/usr/bin/env python3

import os
import re
import argparse
from PyPDF2 import PdfReader, PdfWriter
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai_api = os.getenv('OPENAI_API_KEY')

def extract_first_pages(input_pdf, output_pdf, num_pages=15):
  """Extract first n pages from PDF and save to a new file."""
  reader = PdfReader(input_pdf)
  writer = PdfWriter()

  pages_to_extract = min(num_pages, len(reader.pages))

  for page_num in range(pages_to_extract):
    writer.add_page(reader.pages[page_num])

  with open(output_pdf, 'wb') as output_file:
    writer.write(output_file)

def extract_text_from_pdf(pdf_path):
  reader = PdfReader(pdf_path)
  return ''.join([page.extract_text() + '\n' for page in reader.pages])

def analyze_contents_with_gpt(text):
  client = OpenAI(api_key=openai_api)

  prompt = f"""
    Analyze the following text from a book's contents page and extract chapter information.
    Return the result in the exact format of a Python list of tuples:
    [("Chapter Title", start_page, end_page), ...]
    Only return the Python list, no additional text.

    Text:
    {text}
  """

  response = client.chat.completions.create(
    messages=[
      {"role": "system", "content": "You are a helpful assistant that analyzes book contents pages and returns structured data."},
      {"role": "user", "content": prompt}
    ],
    model="gpt-4",
    temperature=0.2
  )

  return eval(response.choices[0].message.content.strip())

def split_book_by_chapters(input_pdf, chapter_info, output_dir):
  reader = PdfReader(input_pdf)

  os.makedirs(output_dir, exist_ok=True)

  for chapter_title, start_page, end_page in chapter_info:
    writer = PdfWriter()

    end_page = len(reader.pages) if end_page == "End" else end_page

    for page_num in range(start_page - 1, end_page):
      writer.add_page(reader.pages[page_num])

    safe_title = re.sub(r'[^\w\s-]', '', chapter_title)
    output_file = os.path.join(output_dir, f"{start_page}-{safe_title}.pdf")

    with open(output_file, 'wb') as output:
      writer.write(output)

def adjust_chapter_info(chapter_info, actual_first_chapter_page, listed_first_chapter_page):
  offset = actual_first_chapter_page - listed_first_chapter_page

  adjusted_info = []
  for chapter_title, start_page, end_page in chapter_info:
    adjusted_start = start_page + offset if isinstance(start_page, int) else offset + 1
    adjusted_end = end_page + offset if isinstance(end_page, int) else "End"
    
    adjusted_info.append((chapter_title, adjusted_start, adjusted_end))

  return adjusted_info

def main():
  parser = argparse.ArgumentParser(description='Split PDF book into chapters using GPT analysis')
  
  parser.add_argument('pdf_path', type=str, help='Path to the PDF file')
  parser.add_argument('actual_page', type=int, help='Actual page number where Chapter 1 starts in PDF')
  parser.add_argument('listed_page', type=int, help='Page number where Chapter 1 is listed to start in contents')
  
  parser.add_argument('--output-dir', type=str, default=None,
                      help='Output directory for chapter files (default: creates "book_chapters" in same directory as PDF)')

  args = parser.parse_args()

  pdf_path = os.path.abspath(args.pdf_path)
  
  output_dir = os.path.abspath(args.output_dir) if args.output_dir else os.path.join(os.path.dirname(pdf_path), 'book_chapters')
  
  temp_pdf = os.path.join(os.path.dirname(pdf_path), "first_15_pages.pdf")

  try:
    extract_first_pages(pdf_path, temp_pdf)
    
    contents_text = extract_text_from_pdf(temp_pdf)
    
    chapter_info = analyze_contents_with_gpt(contents_text)
    
    adjusted_chapter_info = adjust_chapter_info(chapter_info, args.actual_page, args.listed_page)
    
    split_book_by_chapters(pdf_path, adjusted_chapter_info, output_dir)
    
    print(f"Book successfully split into chapters in directory: {output_dir}")

  except Exception as e:
    print(f"An error occurred: {str(e)}")

  finally:
    if os.path.exists(temp_pdf):
      os.remove(temp_pdf)

if __name__ == "__main__":
  main()