class ListCreator:
    def __init__(self, list_name, product, amount, user):
        self.list_name = list_name
        self.product = product
        self.amount = amount
        self.user = user


    def __str__(self):
        return f'''
        Nome da lista: {self.list_name}
        Produtos: {self.product}
        Quantidade: {self.amount}
        Usuário: {self.user}
        '''
