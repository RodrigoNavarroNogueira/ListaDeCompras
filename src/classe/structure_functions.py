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


    def name_list():
        name_list = input('Escolha o nome da sua lista:\n').lower()
        db.create_table_lista(name_list)
        all_list.append(name_list)
        print(all_list)
        return name_list


    def delete_list():
        name_list = input('Qual o nome da lista que você deseja excluir?')
        db.drop_table_lista(name_list)
        print(f'Lista {name_list} removida com sucesso!')
        return name_list


    def start():
        option = 0
        while option == 0 or option not in [1,2,3,4]:
            option = int(input("""\nSelecione a opção que você deseja: 
        [ 1 ] - Visualizar Listas 
        [ 2 ] - Adicionar/Remover Itens na Lista
        [ 3 ] - Criar/Excluir e Renomear uma Lista
        [ 4 ] - Fechar o Programa\n\n"""))
        return option


    def list_viewer(name_list):
        print(f'Nome da lista escolhida: {name_list}')
        cursor.execute(f"SELECT * FROM {name_list}")
        print(cursor.fetchall())


    def lista_para_manipular(name_list):
        add = 0
        while add == 0 or add not in [1,2,3]:
            add = int(input(f"""Qual lista você deseja acessar?
        (1) - {name_list}\n"""))


    def adicionar_remover_atualizar():
        add_or_del = 0
        while add_or_del == 0 or add_or_del not in 'AUR':
            add_or_del = input(
            """Deseja adicionar, atualizar ou remover produtos?
            ( A ) para Adicionar
            ( U ) para Atualizar
            ( R ) para Remover """).upper()
        return add_or_del


    def add_produtos(name_list):
        while True:
            produto = input('Digite o produto que deseja adicionar: (Para sair pressione "X") ').capitalize()

            if produto == "X":
                break

            else:
                quantidade = int(input('Quantidade?: '))
                engine.create(name_list, random.randint(1, 999), produto, quantidade, name_list, 'Rodrigo', datetime.now())
                print(f'Produto {produto} adicionado com sucesso')


    def remover_produtos():
        while True:
            produto = input('Digite o produto que deseja excluir: (Para sair pressione "X") ').capitalize()

            if produto == "X":
                break

            else:
                engine.delete(produto)
                print(f'Produto {produto} excluido com sucesso')

    
    def update_product_or_amount():
        product_amount = input('Deseja alterar um produto? ou quantidade?\n')
        if product_amount == 'product':
            antigo = input('Qual produto você deseja atualizar?\n')
            novo = input('Qual o nome do produto?\n')
            engine.update(product_amount, novo, antigo)

        elif product_amount == 'amount':
            antigo = input('Qual produto você deseja atualizar a quantidade?\n')
            novo = int(input('Qual a quantidade?\n'))
            engine.update(product_amount, novo, antigo)


    def criar_excluir_renomear():
        escolha = int(input(f"""Escolha uma opção:
        Para criar uma lista pressione 0
        Para excluir uma lista pressione 1
        Para renomear uma lista pressione 2\n"""))
        return escolha


    def tabelas_existentes():
        cursor.execute('SELECT name FROM sqlite_master WHERE type="table";')
        print(cursor.fetchall())
        

banco = sqlite3.connect('lista.db')
cursor = banco.cursor()
engine = ListEngine()
db = DatabaseStructure()
all_list = list()
