from src.db.interface import AbstractEngine

import random
from datetime import datetime

class ListEngine(AbstractEngine):
    def __init__(self):
        super().__init__('lista')


    def create(self, name_list, id, product, amount, list_name, user, created_at):
        query = f'''
            INSERT INTO {name_list} VALUES(
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


    def update(self, product_amount, novo, antigo):
        if product_amount == 'product':
            query = f"UPDATE lista_um SET {product_amount} = '{novo}' WHERE {product_amount} = '{antigo}'"
            self.cursor.execute(query)
            self.database.commit()
            print('O produto foi alterado!')

        elif product_amount == 'amount':
            query = f"UPDATE lista_um SET {product_amount} = {novo} WHERE product = '{antigo}'"
            self.cursor.execute(query)
            self.database.commit()
            print('A quantidade foi alterada!')


    def delete(self, produto):
        query = f'''
        DELETE from lista_um WHERE product = '{produto}'
        '''
        self.cursor.execute(query)
        self.database.commit()
        return produto
