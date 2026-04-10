from pyscript import when, display
from js import document,fetch,URL,Blob
from io import BytesIO, TextIOWrapper
import base64
import requests
import codecs
import os
from pypdf import PdfReader,PdfWriter
from pyodide.http import pyfetch
from dotenv import load_dotenv
from pyodide.ffi import to_js
import json
import asyncio

texURL = 'https://corsproxy.io/?url=https://github.com/Verillix/The-Greatest-Endeavour/tree/c48eee33166b79868bd92c364868b6d64cfb0019/LaTeX'
pdfURL = 'https://raw.githubusercontent.com/Verillix/The-Greatest-Endeavour/refs/heads/main/The%20Greatest%20Endeavour.pdf'
headers = {
        'Access-Control-Allow-Origin' : '*',
        'Access-Control-Allow-Methods' : 'POST, OPTIONS',
        'Access-Control-Allow-Headers' : 'Content-Type, Authorization'
}

def download_Tex_File(data, filename):
    blob = Blob.new([data], {"type": "application/x-tex"})
    url = URL.createObjectURL(blob)
    
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
        response = await pyfetch("//api.github.com/repos/Verillix/The-Greatest-Endeavour/contents/LaTeX?ref=c48eee33166b79868bd92c364868b6d64cfb0019")
        text = json.loads(json.loads(json.dumps(await response.text)))
        print("PLEASE WORK")
        print(text)
        print(test['name'])
        #data = json.loads(text)
        #print(data)
        #download_Tex_File(content,data.get("name"))
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
















































































