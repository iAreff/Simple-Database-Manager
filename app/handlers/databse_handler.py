import sqlite3

class database_handler:

    def __init__(self,file_name:str) -> None:
        self.file_name = file_name
        self.path = "app/db/"

    def database(self,tables:str):
        try:
            self.db = sqlite3.connect(f"{self.path}{self.file_name}")
            cursorobj = self.db.cursor()
            cursorobj.execute(f"CREATE TABLE employees({tables})")
            self.db.commit()
        except:
            pass
    def add_record(self,values:str):
        cursorobj = self.db.cursor()
        cursorobj.execute(f"INSERT INTO employees VALUES({values})")
        self.db.commit()

    def remove_record(self,data:list):
        pass

    def select_record(self,data:list):
        pass
    
    def close(self,data:list):
        self.db.close()