from src.db.interface import AbstractEngine

import random
from datetime import datetime

class ListEngine(AbstractEngine):
    def __init__(self):
        super().__init__('lista')


    def create(self, id, product, amount, list_name, user, created_at):
        query = f'''
            INSERT INTO lista_um VALUES(
                {id},
                '{product}',
                {amount},
                '{list_name}',
                '{user}',
                '{created_at}'
            )
        '''
        self.cursor.execute(query)
        self.database.commit()


    def read(self, query):
        result = self.cursor.execute(query)
        result = result.fetchall()
        return result


    def update(self, id):
        query = f"UPDATE lista_um SET product = 'paid' WHERE id = {id}"
        self.cursor.execute(query)
        self.database.commit()


    def delete(self, produto):
        query = f'''
        DELETE from lista_um WHERE product = '{produto}'
        '''
        self.cursor.execute(query)
        self.database.commit()
        return produto
