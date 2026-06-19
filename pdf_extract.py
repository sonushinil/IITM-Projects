#!/usr/bin/env python3
"""Extract text from PDF using pypdf (lightweight)."""
import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except Exception as e:
    raise


def extract(pdf_path, out_txt):
    reader = PdfReader(str(pdf_path))
    texts = []
    for page in reader.pages:
        texts.append(page.extract_text() or "")
    out_txt.parent.mkdir(parents=True, exist_ok=True)
    out_txt.write_text("\n\n".join(texts), encoding='utf-8')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: pdf_extract.py <pdf_path> [out_txt]')
        sys.exit(2)
    pdf_path = Path(sys.argv[1])
    out_txt = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('outputs') / (pdf_path.stem + '.txt')
    extract(pdf_path, out_txt)
    print(f'Extracted text to: {out_txt}')
