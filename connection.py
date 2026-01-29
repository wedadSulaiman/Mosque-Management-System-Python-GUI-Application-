#connection.py code:
import sqlite3
class MosqueDB:
    def __init__(self):    
        db_path = "MosqueDatabase.db"
        
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Mosque (
                ID INTEGER PRIMARY KEY,
                Name TEXT,
                Type TEXT,
                Address TEXT,
                Coordinates TEXT,
                Imam_Name TEXT
            )
        ''')
        self.connection.commit()

    def exists(self, ID):
        self.cursor.execute("SELECT 1 FROM Mosque WHERE ID=?", (ID,))
        return self.cursor.fetchone() is not None

    def insert(self, ID, name, type_, address, coordinates, imam_name):
        self.cursor.execute(
            "INSERT INTO Mosque (ID, Name, Type, Address, Coordinates, Imam_Name) VALUES (?,?,?,?,?,?)",
            (ID, name, type_, address, coordinates, imam_name)
        )
        self.connection.commit()
        return True 
    
    def __del__(self):
     self.connection.close()

   

        