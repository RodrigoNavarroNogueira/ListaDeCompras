from src.db.interface import AbstractEngine

class ListEngine(AbstractEngine):
    def __init__(self):
        super().__init__('lista')


    def create(self, register_id, list_name, product, amount, created_at):
        query = f'''
            INSERT INTO invoice VALUES(
                {register_id},
                '{list_name}',
                '{product}',
                {amount},
                '{created_at}'
            )
        '''
        self.cursor.execute(query)
        self.database.commit()


    def read(self, query):
        result = self.cursor.execute(query)
        result = result.fetchall()
        return result


    def update(self, invoice_id):
        query = f"UPDATE invoice SET status = 'paid' WHERE id = {invoice_id}"
        self.cursor.execute(query)
        self.database.commit()


    def delete(self, invoice_id):
        query = f'''
            DELETE FROM invoice
            WHERE id = {invoice_id}
        '''
        self.cursor.execute(query)
        self.database.commit()
        return invoice_id
