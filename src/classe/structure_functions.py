from src.db.concrete.list_engine import ListEngine
from src.db.db_structure import DatabaseStructure
import sqlite3
import random
from datetime import datetime

class StructureFunction:
    def initiation():
        print('\n')
        print('*-' * 30)
        print(f'{" Lista de Compras ":=^60}')
        print('*-' * 30, '\n')


    def create_first_list():
        name_list = ''
        while True:
            name_list = input('\nEscolha o nome da sua primeira lista:\n\n').lower().strip()
            if name_list.isnumeric() == True:
                print('\nVocê não pode nomear o nome de uma lista somente com números, tente novamente')
            else:
                break
        db.create_table_lista(name_list)
        return name_list


    def create_list(lista_sem_tupla):
        name_list = ''
        while True:
            name_list = input('\nEscolha o nome da sua lista:\n\n').lower().strip()
            if name_list.isnumeric() == True:
                print('\nVocê não pode nomear o nome de uma lista somente com números, tente novamente')
            else:
                break
        if name_list in lista_sem_tupla:
            print('\nO nome da que você digitou já existe, por favor escolha outro')
        else:
            db.create_table_lista(name_list)
            print('\nLista criada com sucesso!')
            return name_list


    def delete_list(dicionario, tabelas_existentes, listas):
        b = True
        while b is True:
            try:
                num = int(input('\nDigite o número correspondente da lista que você deseja acessar:\nPara retornar ao menu principal, pressione 0\n\n '))
            except ValueError:
                num = 9999
            if num == 0:
                break
            else:
                try:
                    db.drop_table_lista(dicionario[num][0])
                    print(f'\nLista {dicionario[num][0]} removida com sucesso!')
                    b = False
                except KeyError:
                    print('\nVocê não digitou um número de alguma lista')
                    tabelas_existentes(listas)

    def rename_list(escolha):
        new_name = input('\nQual o nome que deseja colocar?\n\n').strip()
        db.rename_lista(escolha, new_name)
        print('\nO nome da lista foi alterada!')


    def start():
        option = 0
        try:
            while option == 0 or option not in [1, 2, 3, 4]:
                option = int(input("""\nSelecione a opção que você deseja:\n 
[ 1 ] - Visualizar Listas 
[ 2 ] - Adicionar/Remover/Atualizar Itens na Lista
[ 3 ] - Criar/Excluir e Renomear uma Lista
[ 4 ] - Fechar o Programa\n\n"""))
                if type(option) is int and option not in [1, 2, 3, 4]:
                    print('\nVocê não digitou uma opção válida')        
        except ValueError:
            print('\nVocê não digitou uma opção válida')
        return option


    def list_viewer_new(escolha):
        print(f'\nNome da lista escolhida: {escolha.title()}\n')
        cursor.execute(f"SELECT * FROM {escolha}")
        x = list(cursor.fetchall())
        if x == []:
            print('Esta lista está vazia!')
            return 'Esta lista está vazia!'
        else:
            count = 0
            result = []
            for produto in x:
                print(f'Produto: {x[count][1]} / Quantidade: {x[count][2]}\n')
                result.append(f'<p>Produto: {x[count][1]} / Quantidade: {x[count][2]}</p>')
                count += 1
            y = '\n'.join(map(str, result))
            return y[3:-2]


    def adicionar_remover_atualizar():
        add_or_del = 0
        while add_or_del == 0 or add_or_del not in 'AUR':
            add_or_del = input(
            """\nDeseja adicionar, atualizar ou remover produtos?
( A ) para Adicionar
( U ) para Atualizar
( R ) para Remover\n\n""").upper().strip()
        return add_or_del


    def add_produtos(escolha):
        while True:
            produto = input('\nDigite o produto que deseja adicionar: (Para sair pressione "X")\n\n').capitalize().strip()

            if produto == "X":
                break

            else:
                quantidade = int(input('\nQuantidade?:\n\n'))
                engine.create(escolha, random.randint(1, 999), produto, quantidade, escolha, 'Rodrigo', datetime.now())
                print(f'\nProduto {produto} adicionado com sucesso')


    def remover_produtos(escolha):
        cursor.execute(f"SELECT * FROM {escolha}")
        x = list(cursor.fetchall())
        if x == []:
            print('\nA lista está vazia, adicione itens para modificá-los')

        else:
            while True:
                produto = input('Digite o produto que deseja excluir: (Para sair pressione "X")\n\n').capitalize().strip()

                if produto == "X":
                    break

                else:
                    engine.delete(escolha, produto)
                    print(f'\nProduto {produto} excluido com \n')

    
    def update_product_or_amount(escolha):
        product_amount = 0
        cursor.execute(f"SELECT * FROM {escolha}")
        x = list(cursor.fetchall())
        if x == []:
            print('\nA lista está vazia, adicione itens para modificá-la')
        else:
            while product_amount == 0 or product_amount not in ['1', '2', '3']:
                product_amount = input('\nDeseja alterar um produto? ou quantidade? (1) Para Produto e (2) Para Quantidade (3) Para Retornar ao Menu\n\n').strip()
                
                if product_amount not in ['1', '2', '3']:
                    print('\nOpção inválida, por favor, escolha entre o produto ou a quantidade\n')

                if product_amount == '1':
                    product_amount = 'product'
                    antigo = input('\nQual produto você deseja atualizar?\n\n').capitalize()
                    if antigo != x[0][1]:
                        print('\nVocê inseriu um produto que não existe na lista, por gentileza verifique a lista novamente\n')
                    else:
                        novo = input('\nQual o nome do produto á ser adicionado?\n').capitalize()
                        engine.update(escolha, product_amount, novo, antigo)

                elif product_amount == '2':
                    product_amount = 'amount'
                    antigo = input('\nQual produto você deseja atualizar a quantidade?\n\n').capitalize()
                    if antigo != x[0][1]:
                        print('\nVocê inseriu um produto que não existe na lista, por gentileza verifique a lista novamente\n')
                    else:
                        novo = int(input('\nQual a quantidade?\n'))
                        engine.update(escolha, product_amount, novo, antigo)

                elif product_amount == '3':
                    break
        

    def criar_excluir_renomear():
        b = True
        while b is True:
            try:
                escolha = int(input(f"""\nEscolha uma opção, para retornar ao menu principal pressione 0:\n
Para criar uma lista pressione 1
Para excluir uma lista pressione 2
Para renomear uma lista pressione 3\n\n"""))
                if escolha in [0, 1, 2, 3]:
                    break
                if type(escolha) is int:
                    print('\nVocê não digitou uma opção válida')
            except ValueError:
                    print('\nVocê não digitou uma opção válida')
        b = False
        return escolha


    def tabelas_existentes(listas):
        print('\n')
        for i, lista in enumerate(listas):
            print(i + 1,'-', lista[0].title())


    def dict_list(listas):
        dicionario = dict(zip(range(1, len(listas) + 1), listas))
        return dicionario


    def tabelas_existentes_str(create_list, lista_sem_tupla):
        cursor.execute('SELECT name FROM sqlite_master WHERE type="table";')
        listas = list(cursor.fetchall())
        if listas == []:
            print('\nNão existe nenhuma lista, será necessário criar sua primeira!')
            create_list(lista_sem_tupla)
            cursor.execute('SELECT name FROM sqlite_master WHERE type="table";')
            listas = list(cursor.fetchall())
        return listas


    def escolhe_lista(dicionario, tabelas_existentes, listas):
        b = True
        while b is True:
            try:
                num = int(input('\nDigite o número correspondente da lista que você deseja acessar:\nPara retornar ao menu principal, pressione 0\n\n '))
            except ValueError:
                num = 9999
            if num == 0:
                escolha = 0
                break
            else:
                try:
                    a = str(dicionario[num])
                    escolha = a[2:-3]
                    b = False
                except KeyError:
                    print('\nVocê não digitou um número de alguma lista')
                    escolha = 0
                    tabelas_existentes(listas)
        return escolha


    def quantidade_tabelas(create_first_list):
        cursor.execute('SELECT name FROM sqlite_master WHERE type="table";')
        if len(cursor.fetchall()) >= 1:
            pass
        else:
            create_first_list()


banco = sqlite3.connect('lista.db')
cursor = banco.cursor()
engine = ListEngine()
db = DatabaseStructure()
