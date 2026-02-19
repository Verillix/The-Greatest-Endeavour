import os
from http.server import BaseHTTPRequestHandler
import base64
from github import Github
from github import InputGitTreeElement

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        github_token = os.environ.get('API_KEY')
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()  
        try:
            user = "Verillix"
            password = github_token
            g = Github(user,password)
            repo = g.get_user().get_repo('The Greatest Endeavour') # repo name
            commit_message = 'python commit'
            master_ref = repo.get_git_ref('heads/master')
            master_sha = master_ref.object.sha
            base_tree = repo.get_git_tree(master_sha)
        except Exception as error:
            self.wfile.write(error.encode())
        '''
        element_list = list()
        for i, entry in enumerate(file_list):
            with open(entry) as input_file:
                data = input_file.read()
            if entry.endswith('.png'): # images must be encoded
                data = base64.b64encode(data)
            element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
            element_list.append(element)
        
        tree = repo.create_git_tree(element_list, base_tree)
        parent = repo.get_git_commit(master_sha)
        commit = repo.create_git_commit(commit_message, tree, [parent])
        master_ref.edit(commit.sha)
        '''
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.end_headers()
