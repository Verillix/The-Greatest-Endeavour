import os
import json
import base64
import requests
from http.server import BaseHTTPRequestHandler

display("hi!")

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        token = os.environ.get('GIT_TOKEN')
        repo = os.environ.get('GIT_REPO')

        content_length = int(self.headers.get('Content-Length', 0))
        body = json.loads(self.rfile.read(content_length))

        filename = body.get('filename')
        content = base64.b64encode(body.get('content').encode()).decode()

        response = requests.put(
            f'https://api.github.com/repos/{repo}/contents/{filename}',
            headers={'Authorization': f'Bearer {token}'},
            json={'message': f'Upload {filename}', 'content': content}
        )

        self.send_response(response.status_code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(response.content)
    except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(str(e).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
