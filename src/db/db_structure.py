from src.db.interface import AbstractEngine


class DatabaseStructure(AbstractEngine):
    def __init__(self):
        super().__init__('lista')


    def create_table_lista(self):
            self.cursor.execute(
                '''
                CREATE TABLE lista_um(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    list_name VARCHAR,
                    product VARCHAR,
                    amount INT,
                    user VARCHAR,
                    created DATETIME
                )
                '''
            )
            self.database.commit()



    def drop_table_lista(self):
        query = 'DROP TABLE lista_um;'
        self.cursor.execute(query)
        self.database.commit()
