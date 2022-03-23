import sqlite3

class StructureFunction:
    def initiation():
        print('*-' * 30)
        print(f'{" Lista de Compras ":=^60}')
        print('*-' * 30, '\n')


    def name_list():
        name_list = input('Escolha o nome da sua lista:\n').capitalize()
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


    def list_viewer(list_name):
        print(f'Nome da lista escolhida: {list_name}')
        cursor.execute("SELECT * FROM lista_um")
        print(cursor.fetchall())


    def lista_para_manipular(list_name):
        add = 0
        while add == 0 or add not in [1,2,3]:
            add = int(input(f"""Qual lista você deseja acessar?
        (1) - {list_name}\n"""))


    def adicionar_ou_remover():
        add_or_del = 0
        while add_or_del == 0 or add_or_del not in 'AR':
            add_or_del = input(
            'Deseja adicionar ou Remover produtos? ( A ) para Adicionar e ( R ) para Remover ').upper()
        return add_or_del





banco = sqlite3.connect('lista.db')
cursor = banco.cursor()