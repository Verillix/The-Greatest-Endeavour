from pyscript import when, display
from js import document,fetch
from io import BytesIO, TextIOWrapper
import base64
import requests
import codecs
import os
from pypdf import PdfReader,PdfWriter
from pyodide.http import open_url
from dotenv import dotenv_values



class StrToBytes:
    def __init__(self, fileobj):
        self.fileobj = fileobj
    def read(self, size):
        return self.fileobj.read(size).encode()
    def readline(self, size=-1):
        return self.fileobj.readline(size).encode()

@when('change', '#upload')
async def processFile(*args):
    pdf = document.getElementById('upload').files.item(0)
    my_bytes = await pdf.arrayBuffer()
    pdf_bytes = my_bytes.to_bytes()
    pdfFile = BytesIO(pdf_bytes)
    for i in range(10):
        display("break")
    display(pdf_bytes)
    reader = PdfReader(pdfFile)
    text = [""]
    for i in reader.pages:
        text.append(i.extract_text())
    
def readCurrent():
    pdf = requests.get("https://raw.githubusercontent.com/Verillix/The-Greatest-Endeavour/2561f1c31ce4d7bc6306e9e7f9283f5a24bfcb2e/The%20Greatest%20Endeavour.pdf")
    pdf = BytesIO(pdf.content)
    reader = PdfReader(pdf)
    display(reader.pages[0].extract_text())

@when("click", selector="#download")
async def downloaded(*args):
    try:
        #key = os.environ["APIKEY"]
        #config = dotenv_values(".env")
        for key, value in os.environ.items():
            display('{}: {}'.format(key, value))
        display(secrets.APIKEY)
    except Exception as error:


        display(error)
