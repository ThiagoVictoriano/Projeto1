from utils import load_data, load_template, write_database, build_response
from database import Database, Note
import urllib.parse

db = Database('banco')

def delete(id):
    db.delete(id)
    response = build_response(code=303, reason='See Other', headers='Location: /')
    return response

def erro404():
    response = build_response(code=404, reason='Not Found')
    return response + load_template('404.html').encode()
 
def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            if chave_valor[0][0] == 't':
                titulo_esquisito = chave_valor[7:]
                titulo = urllib.parse.unquote_plus(titulo_esquisito)
            else:
                detalhe_esquisito = chave_valor[9:]
                detalhe = urllib.parse.unquote_plus(detalhe_esquisito)
        write_database(titulo, detalhe)
        response = build_response(code=303, reason='See Other', headers='Location: /')
    
    else:
        response = build_response()

    note_template = load_template('components/note.html')
    lista_dados =  load_data()
    notes_li = [
            note_template.format(title=dados.title, details=dados.content, id=dados.id)
            for dados in lista_dados
            ]

    notes = '\n'.join(notes_li)
    return response + load_template('index.html').format(notes=notes).encode()

def edit(request, id):
    dados =  db.get_note(id) 
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            if chave_valor[0][0] == 'T':
                titulo_esquisito = chave_valor[7:]
                titulo = urllib.parse.unquote_plus(titulo_esquisito)
            else:
                detalhe_esquisito = chave_valor[9:]
                detalhe = urllib.parse.unquote_plus(detalhe_esquisito)
        db.update(Note(id, titulo, detalhe))
        response = build_response(code=303, reason='See Other', headers='Location: /')
        note_template = load_template('components/note.html')
        lista_dados =  load_data()
        notes_li = [
                note_template.format(title=dados.title, details=dados.content, id=dados.id)
                for dados in lista_dados
                ]

        notes = '\n'.join(notes_li)

        return response + load_template('index.html').format(notes=notes).encode()
    
    else:
        response = build_response()

        return response + load_template('edit.html').format(title=dados.title, details=dados.content, id=dados.id).encode()
