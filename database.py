import sqlite3

class Database:
    def __init__(self, name):
        self.conn = sqlite3.connect(name + '.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY, 
                          title STRING,
                          content STRING NOT NULL)''')
    
    def add(self, note):
        self.conn.execute(f"INSERT INTO note (title, content) VALUES ('{note.title}','{note.content}')")
        self.conn.commit()
    
    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        lista_notes = [Note(linha[0], linha[1], linha[2]) for linha in cursor]

        return(lista_notes)
    
    def get_note(self, id):
        cursor = self.conn.execute(f'''SELECT title, content FROM note WHERE id = '{id}' ''')
        note = [Note(id=id, title=title, content=content) for title, content in cursor.fetchall()]
        if len(note) > 0:
            return note[0]
        return None
        
    def update(self, entry):
        self.conn.execute(f"UPDATE note SET title = '{entry.title}', content = '{entry.content}'  WHERE id = '{entry.id}'")
        self.conn.commit()
    
    def delete(self, note_id):
        self.conn.execute(f"DELETE FROM note WHERE id = '{note_id}'")
        self.conn.commit()
        
class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content