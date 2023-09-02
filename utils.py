import json
from database import Database, Note
def extract_route(request):
    string = ''
    start = False
    contagem = 0
    for i in request:
        if i == '/'and contagem == 0:
            start = True
            contagem = 1
        
        elif i == ' ':
            start = False

        elif start:
            string += i
    return string

def read_file(path):
    with open(path, mode ='r+b') as file:
        return(file.read())

def load_data():
    db = Database('banco')
    notes = db.get_all()
    return notes
def load_template(arquivo):
    with open(f'templates/{arquivo}', mode ='r') as file:
        return(f'{file.read()}')
    
def write_database(titulo, conteudo):
    db = Database('banco')
    db.add(Note(title = titulo, content = conteudo))

def build_response(body='', code = 200, reason = 'OK', headers = ''):
    final = f'HTTP/1.1 {code} {reason}'
    if headers:
        final += "\n" + headers
    
    final += "\n\n" + body
    return final.encode()