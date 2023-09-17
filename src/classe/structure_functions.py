from src.db.concrete.list_engine import ListEngine
from src.db.db_structure import DatabaseStructure
import sqlite3
import random
from datetime import datetime

class StructureFunction:
    def initiation():
        print('*-' * 30)
        print(f'{" Lista de Compras ":=^60}')
        print('*-' * 30, '\n')


    def create_first_list():
        name_list = input('Escolha o nome da sua primeira lista:\n').lower().strip()
        db.create_table_lista(name_list)
        return name_list


    def create_list():
        name_list = input('Escolha o nome da sua lista:\n').lower().strip()
        db.create_table_lista(name_list)
        return name_list


    def delete_list(dicionario):
        num = int(input('Digite o número correspondente da lista que você deseja excluir:\n'))
        db.drop_table_lista(dicionario[num][0])
        print(f'Lista {dicionario[num][0]} removida com sucesso!')


    def rename_list():
        name_list = input('Qual o nome da lista que você deseja renomear?\n').strip()
        new_name = input('Qual o nome que deseja colocar?\n').strip()
        db.rename_lista(name_list, new_name)
        print('O nome da lista foi alterada!')


    def start():
        option = 0
        while option == 0 or option not in [1,2,3,4]:
            option = int(input("""\nSelecione a opção que você deseja: 
        [ 1 ] - Visualizar Listas 
        [ 2 ] - Adicionar/Remover/Atualizar Itens na Lista
        [ 3 ] - Criar/Excluir e Renomear uma Lista
        [ 4 ] - Fechar o Programa\n\n"""))
        return option


    def list_viewer(escolha):
        print(f'Nome da lista escolhida: {escolha}\n')
        cursor.execute(f"SELECT * FROM {escolha}")
        x = str(cursor.fetchall())
        if x == "[]":
            print('Esta lista está vazia!\n')
        else:
            print(x)


    def list_viewer_new(escolha):
        print(f'Nome da lista escolhida: {escolha}\n')
        cursor.execute(f"SELECT * FROM {escolha}")
        x = list(cursor.fetchall())
        if x == []:
            return 'Esta lista está vazia!\n'
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
            """Deseja adicionar, atualizar ou remover produtos?
            ( A ) para Adicionar
            ( U ) para Atualizar
            ( R ) para Remover\n""").upper().strip()
        return add_or_del


    def add_produtos(escolha):
        while True:
            produto = input('Digite o produto que deseja adicionar: (Para sair pressione "X") ').capitalize().strip()

            if produto == "X":
                break

            else:
                quantidade = int(input('Quantidade?: '))
                engine.create(escolha, random.randint(1, 999), produto, quantidade, escolha, 'Rodrigo', datetime.now())
                print(f'Produto {produto} adicionado com sucesso')


    def remover_produtos(escolha):
        while True:
            produto = input('Digite o produto que deseja excluir: (Para sair pressione "X") ').capitalize().strip()

            if produto == "X":
                break

            else:
                engine.delete(escolha, produto)
                print(f'Produto {produto} excluido com sucesso')

    
    def update_product_or_amount(escolha):
        product_amount = input('Deseja alterar um produto? ou quantidade?\n').strip()
        if product_amount == 'produto':
            product_amount = 'product'
            antigo = input('Qual produto você deseja atualizar?\n').capitalize()
            novo = input('Qual o nome do produto á ser adicionado?\n').capitalize()
            engine.update(escolha, product_amount, novo, antigo)

        elif product_amount == 'quantidade':
            product_amount = 'amount'
            antigo = input('Qual produto você deseja atualizar a quantidade?\n').capitalize()
            novo = int(input('Qual a quantidade?\n'))
            engine.update(escolha, product_amount, novo, antigo)


    def criar_excluir_renomear():
        b = True
        while b is True:
            try:
                escolha = int(input(f"""\nEscolha uma opção, para retornar ao menu principal pressione 3:
                Para criar uma lista pressione 0
                Para excluir uma lista pressione 1
                Para renomear uma lista pressione 2\n\n"""))
                if escolha in [0, 1, 2, 3]:
                    break
            except ValueError:
                    print('\nVocê não digitou uma opção válida')
        b = False
        return escolha


    def tabelas_existentes(listas):
        print('\n')
        for i, lista in enumerate(listas):
            print(i + 1, lista[0])


    def dict_list(listas):
        dicionario = dict(zip(range(1, len(listas) + 1), listas))
        return dicionario


    def tabelas_existentes_str(create_list):
        cursor.execute('SELECT name FROM sqlite_master WHERE type="table";')
        listas = list(cursor.fetchall())
        if listas == []:
            print('Não existe nenhuma lista, será necessário criar sua primeira!')
            create_list()
            cursor.execute('SELECT name FROM sqlite_master WHERE type="table";')
            listas = list(cursor.fetchall())
        return listas


    def escolhe_lista(dicionario):
        b = True
        while b is True:
            num = int(input('\n Digite o número correspondente da lista que você deseja acessar:\n Para retornar ao menu principal, pressione 0\n\n '))
            if num == 0:
                escolha = 0
                break
            else:
                try:
                    a = str(dicionario[num])
                    escolha = a[2:-3]
                    b = False
                except KeyError:
                    print('Você não digitou um número de alguma lista')
                    escolha = 0
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
