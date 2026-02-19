from pyscript import when, display
from js import document,fetch,URL,Blob
from io import BytesIO, TextIOWrapper
import base64
import requests
import codecs
import os
from pypdf import PdfReader,PdfWriter
from pyodide.http import open_url
from dotenv import load_dotenv
from pyodide.ffi import to_js
import json
import asyncio

texURL = 'https://raw.githubusercontent.com/Verillix/The-Greatest-Endeavour/refs/heads/main/The%20Greatest%20Endeavour.tex'
pdfURL = 'https://raw.githubusercontent.com/Verillix/The-Greatest-Endeavour/refs/heads/main/The%20Greatest%20Endeavour.pdf'

def download_file(data, filename):
    blob = Blob.new([data], {"type": "application/x-tex"})
    url = URL.createObjectURL(blob)
    
    a = document.createElement('a')
    a.href = url
    a.download = filename
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)

@when('change', '#upload')
async def push_file(content, filename):
    response = await fetch(
        'https://your-vercel-app.vercel.app/api/push',
        method='POST',
        headers=to_js({'Content-Type': 'application/json'}),
        body=json.dumps({'filename': filename, 'content': content})
    )
    print('Done!' if response.ok else 'Failed!')
    asyncio.ensure_future(push_file(your_content, "myfile.tex"))
#async def processTex(*args):
    #oldTex = await fetch(texURL)
    #oldText = await oldTex.text()
    #newTex = document.getElementById('upload').files.item(0)
    #newText = await newTex.text()
    
    
    
    

@when('click', '#downloadTex')
async def downloadTex():
    response = await fetch(texURL)
    responseText = await response.text()
    #download_file(responseText, "The Greatest Endeavour.tex")
    response = await fetch('https://the-greatest-endeavour.vercel.app/api/apiGET')
    token = await response.text()  # raw text
    print(token)


@when('click', '#downloadPDF')
async def downloadPDF():
    filename = "The Greatest Endeavour.pdf"
    a = document.createElement('a')
    a.href = pdfURL
    a.download = filename
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)




#Process uploaded PDF
'''
async def processPDF(*args):
    pdf = document.getElementById('upload').files.item(0)
    my_bytes = await pdf.arrayBuffer()
    pdf_bytes = my_bytes.to_bytes()
    pdfFile = BytesIO(pdf_bytes)
    reader = PdfReader(pdfFile)
    text = [""]
    for i in reader.pages:
        text.append(i.extract_text())
'''
#Read Current PDF
'''
def readCurrent():
    pdf = requests.get("https://raw.githubusercontent.com/Verillix/The-Greatest-Endeavour/refs/heads/main/The%20Greatest%20Endeavour.pdf")
    pdf = BytesIO(pdf.content)
    reader = PdfReader(pdf)
    display(reader.pages[0].extract_text())
'''




























































