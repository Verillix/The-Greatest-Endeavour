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
from parsel import Selector

texURL = 'https://github.com/Verillix/The-Greatest-Endeavour/tree/c48eee33166b79868bd92c364868b6d64cfb0019/LaTeX'
pdfURL = 'https://raw.githubusercontent.com/Verillix/The-Greatest-Endeavour/refs/heads/main/The%20Greatest%20Endeavour.pdf'
headers = {
        'Access-Control-Allow-Origin' : '*',
        'Access-Control-Allow-Methods' : 'POST, OPTIONS',
        'Access-Control-Allow-Headers' : 'Content-Type, Authorization'
}

def download_TexFile(data, filename):
    #blob = Blob.new([data], {"type": "application/dir"})
    #url = URL.createObjectURL(blob)
    
    a = document.createElement('a')
    a.href = texURL
    a.download = filename
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)

@when('change', '#upload')
async def processTex(*args):
    content = document.getElementById('upload').files.item(0)
    content = await content.text()
    filename = document.getElementById('upload').files.item(0).name
    print(filename)  

@when('click','#uploadToGit')
async def push_file(content, filename):
    try:
        requests.post('https://the-greatest-endeavour.vercel.app/api/gitPUSH.py', json={
        'filePath' : filename,
        'content': content,
        'message': 'Update config'
        }, headers = headers)
    except Exception as error:
        print(error)

@when('click', '#downloadTex')
async def downloadTex():
        requests.get(texURL, headers=headers)
        selector = Selector(text=text)
        for i in selector.css(".//@href"):
          print(i)    
        #download_TexFile(texURL, "LaTeX.dir")
@when('click', '#downloadPDF')
async def downloadPDF():
    filename = "The Greatest Endeavour.pdf"
    a = document.createElement('a')
    a.href = pdfURL
    a.download = filename
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(pdfURL)

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
















































































