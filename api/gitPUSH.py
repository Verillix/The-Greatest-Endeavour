import os
import base64
import requests
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            token = os.environ.get('GITHUB_TOKEN')
            repo = os.environ.get('GITHUB_REPO')

            content_length = int(self.headers.get('Content-Length', 0))
            content = self.rfile.read(content_length).decode('utf-8')
            encoded = base64.b64encode(content.encode()).decode()

            response = requests.put(
                f'https://api.github.com/repos/{repo}/contents/upload.tex',
                headers={'Authorization': f'Bearer {token}'},
                json={'message': 'Upload file', 'content': encoded}
            )

            self.send_response(response.status_code)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response.content)

        except Exception as e:
            self.send_response(500)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(str(e).encode())
