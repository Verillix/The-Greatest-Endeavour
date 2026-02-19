import os
from http.server import BaseHTTPRequestHandler
import base64

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        github_token = os.environ.get('GIT_TOKEN')
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.end_headers()
