from http.server import BaseHTTPRequestHandler
import json, os
from github import Github

class handler(BaseHTTPRequestHandler):
    print(os.environ['GIT_TOKEN'])
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = json.loads(self.rfile.read(length))

        file_path = body['filePath']
        content   = body['content']
        message   = body.get('message', 'Remote update')

        g    = Github(os.environ['GIT_TOKEN'])
        repo = g.get_repo(os.environ['GIT_REPO'])  # e.g. "owner/repo"

        try:
            # Update existing file
            existing = repo.get_contents(file_path)
            repo.update_file(file_path, message, content, existing.sha)
        except Exception:
            # File doesn't exist yet — create it
            repo.create_file(file_path, message, content)

        self._respond(200, {'success': True})

    def _respond(self, status, data):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
