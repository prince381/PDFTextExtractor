# PDFTextExtractor

A lightweight backend service for extracting text from PDF files using Python.  
The service exposes a simple HTTP API that accepts a PDF file (Base64-encoded) and returns extracted text.

## 🚀 Features

- Extracts text from standard (text-based) PDF documents
- Page-by-page processing using `PyPDF2`
- Optional OCR support for scanned PDFs using `pytesseract` (present but currently disabled)
- REST API built with Flask
- JSON-based input and output
- Docker-ready for containerized deployment

## 🧠 How It Works

1. The client sends a POST request containing a Base64-encoded PDF file.
2. The server decodes the file into an in-memory buffer.
3. Text is extracted page-by-page using `PyPDF2`.
4. Extracted text is normalized to ASCII and returned as JSON.

For scanned PDFs, the code includes an OCR pipeline that:
- Extracts images from each PDF page
- Runs OCR using Tesseract via `pytesseract`
*(This path is currently commented out but fully implemented.)*

## 🧰 Tech Stack

- Python 3
- Flask
- PyPDF2
- Pillow
- pytesseract
- Gunicorn (production-ready WSGI server)

## 📦 Installation

### Clone the repository
```bash
git clone https://github.com/prince381/PDFTextExtractor.git
cd PDFTextExtractor
````

### Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** If you intend to enable OCR, ensure **Tesseract OCR** is installed on your system.

## ▶️ Running the Server

```bash
python app.py
```

The server starts on:

```
http://0.0.0.0:5000
```

## 📡 API Usage

### Health Check

**GET /**

```text
Hello from the pdf text extractor!
```

### Extract Text from PDF

**POST /extractText**

#### Request Body (JSON)

```json
{
  "fileBuffer": "<base64-encoded-pdf>"
}
```

#### Successful Response

```json
{
  "status": "success",
  "data": "Extracted text content..."
}
```

#### Error Response

```json
{
  "status": "failed",
  "error": "Error message"
}
```

## 🐳 Docker (Optional)

The project includes a `Dockerfile` for containerized deployment.

```bash
docker build -t pdf-text-extractor .
docker run -p 5000:5000 pdf-text-extractor
```

## 🔧 Notes & Limitations

* OCR extraction is implemented but disabled by default
* Currently optimized for text-based PDFs
* ASCII normalization is applied to extracted content
* No persistent storage — stateless by design

## 📄 License

MIT License
