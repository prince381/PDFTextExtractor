import sys, os, io, json, base64
from PyPDF2 import PdfReader
import pytesseract
from PIL import Image
from flask import Flask, request, jsonify

app = Flask(__name__)

def extractContent(arrayBuffer):
    pdf = PdfReader(arrayBuffer)
    content = ""
    for i in range(0, len(pdf.pages)):
        text = pdf.pages[i].extract_text()
        if len(text) > 0:
            content += text + "\n"
    return content.encode('ascii', 'ignore').decode('ascii')

def extractScannedDocContent(arrayBuffer):
    pdf = PdfReader(arrayBuffer)
    content = ""
    for i in range(0, len(pdf.pages)):
        images = pdf.pages[i].images
        for j in range(0, len(images)):
            imageData = images[j].data
            image = Image.open(io.BytesIO(imageData))
            content += pytesseract.image_to_string(image) + "\n"
    return content.encode('ascii', 'ignore').decode('ascii')

def getTextContent(data):
    try:
        base64String = data['fileBuffer']
        bufferData = base64.b64decode(base64String)
        bufferData = io.BytesIO(bufferData)
        normalText = extractContent(bufferData)
        if len(normalText) > 300:
            return normalText
        else:
            scannedContent = extractScannedDocContent(bufferData)
            return scannedContent
    except Exception as e:
        raise Exception(str(e))
    

@app.route('/')
def index():
    return "Hello from the pdf text extractor!"

@app.route('/extractText', methods=['POST'])
def extractText():
    try:
        data = request.get_json()
        textContent = getTextContent(data)
        print(textContent)
        return jsonify({'status': 'success', 'data': textContent})
    except Exception as e:
        return jsonify({'status': 'failed', 'error': str(e)})

if __name__ == "__main__":
    app.run()
