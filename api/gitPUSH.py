# api/update_file.py
from http.server import BaseHTTPRequestHandler
import json, os, base64, requests

GITHUB_API = "https://api.github.com"

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = json.loads(self.rfile.read(length))

        file_path = body['filePath']
        content   = body['content']
        message   = body.get('message', 'Remote update')

        headers = {
            "Authorization": f"Bearer {os.environ.get('GIT_TOKEN')}",
            "Content-Type": "application/json"
        }
        repo    = os.environ.get('GIT_REPO')
        url     = f"{GITHUB_API}/repos/{repo}/contents/{file_path}"

        # Get SHA if file already exists
        existing = requests.get(url, headers=headers)
        sha = existing.json().get('sha') if existing.ok else None

        payload = {
            "message": message,
            "content": base64.b64encode(content.encode()).decode()
        }
        if sha:
            payload["sha"] = sha

        res = requests.put(url, headers=headers, json=payload)
        self._respond(200 if res.ok else 500, {'success': res.ok})

    def _respond(self, status, data):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
