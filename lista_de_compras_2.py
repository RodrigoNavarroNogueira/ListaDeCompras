import sys


# python -m lista_de_compras_2


def inicio():
    print('*-' * 30)
    print(f'{" Lista de Compras ":=^60}')
    print('*-' * 30)


def nome_da_primeira_lista():
    global nome_primeira_lista
    nome_primeira_lista = input('Escolha o nome da sua primeira lista:\n').capitalize()


def nome_da_segunda_lista():
    global nome_segunda_lista
    nome_segunda_lista = input('Escolha o nome da sua segunda lista:\n').capitalize()


def nome_da_terceira_lista():
    global nome_terceira_lista
    nome_terceira_lista = input('Escolha o nome da sua terceira lista:\n').capitalize()


def visualizador_de_listas():
    lista = int(input('Qual lista você deseja visualizar?'))
    if lista == 1:
        print(nome_primeira_lista)
        if dict_1 == {}:
            print('A lista está vazia')
        else:
            print(dict_1)
    if lista == 2:
        print(nome_segunda_lista)
        if dict_2 == {}:
            print('A lista está vazia')
        else:
            print(dict_2)
    if lista == 3:
        print(nome_terceira_lista)
        if dict_3 == {}:
            print('A lista está vazia')
        else:
            print(dict_3)


def add_produtos():
    while True:
        produto = input('Digite o produto que deseja adicionar: (Para sair pressione "X") ').capitalize()

        if produto == "X":
            start()

        else:
            quantidade = int(input('Quantidade?: '))

            dict_1[produto] = quantidade
            print(f'Produto {produto} adicionado com sucesso')


def add_produtos_dois():
    while True:
        produto = input('Digite o produto que deseja adicionar: (Para sair pressione "X") ').capitalize()

        if produto == "X":
            start()

        else:
            quantidade = int(input('Quantidade?: '))

            dict_2[produto] = quantidade
            print(f'Produto {produto} adicionado com sucesso')


def add_produtos_tres():
    while True:
        produto = input('Digite o produto que deseja adicionar: (Para sair pressione "X") ').capitalize()

        if produto == "X":
            start()

        else:
            quantidade = int(input('Quantidade?: '))

            dict_3[produto] = quantidade
            print(f'Produto {produto} adicionado com sucesso')


def start():
    opcao = int(input("""Selecione a opção que você deseja: 
        [ 1 ] - Visualizar Listas 
        [ 2 ] - Adicionar/Remover Itens na Lista
        [ 3 ] - Criar/Excluir uma Lista
        [ 4 ] - Fechar o Programa\n\n"""))

    if opcao == 1:
        visualizador_de_listas()
        start()

    elif opcao == 2:
        add = int(input(
            f'Qual lista você deseja acessar? (1) - {nome_primeira_lista} (2) - {nome_segunda_lista} (3) - {nome_terceira_lista}\n'))

        if add == 1:
            add_or_del = input(
                'Deseja adicionar ou Remover produtos? ( A ) para Adicionar e ( R ) para Remover ').upper()

            if add_or_del == "A":
                add_produtos()

            else:
                while True:
                    produto = input('Digite o produto que deseja excluir: (Para sair pressione "X") ').capitalize()

                    if produto == "X":
                        start()

                    else:
                        del dict_1[produto]
                        print(f'Produto {produto} excluido com sucesso')

        if add == 2:
            add_or_del = input(
                'Deseja adicionar ou Remover produtos? ( A ) para Adicionar e ( R ) para Remover ').upper()

            if add_or_del == "A":
                add_produtos_dois()

            else:
                while True:
                    produto = input('Digite o produto que deseja excluir: (Para sair pressione "X") ').capitalize()

                    if produto == "X":
                        start()

                    else:
                        del dict_2[produto]
                        print(f'Produto {produto} excluido com sucesso')

        if add == 3:
            add_or_del = input(
                'Deseja adicionar ou Remover produtos? ( A ) para Adicionar e ( R ) para Remover ').upper()

            if add_or_del == "A":
                add_produtos_tres()

            else:
                while True:
                    produto = input('Digite o produto que deseja excluir: (Para sair pressione "X") ').capitalize()

                    if produto == "X":
                        start()

                    else:
                        del dict_3[produto]
                        print(f'Produto {produto} excluido com sucesso')

    elif opcao == 3:
        escolha = int(input(
            f'Escolha uma lista vazia para cria-la: (1) - {nome_primeira_lista.capitalize()}\n (2) - {nome_segunda_lista.capitalize()}\n (3) - {nome_terceira_lista.capitalize()}\n'))
        if escolha == 1:
            print(f'Você já criou a lista {nome_primeira_lista}!')
            start()

        elif escolha == 2:
            nome_da_segunda_lista()
            print(f'Você criou a lista {nome_segunda_lista}!')
            start()

        elif escolha == 3:
            nome_da_terceira_lista()
            print(f'Você criou a lista {nome_terceira_lista}!')
            start()

    elif opcao == 4:
        print('Finalizando programa, até mais!')
        sys.exit()


nome_da_primeira_lista()
inicio()
dict_1 = dict()
dict_2 = dict()
dict_3 = dict()

nome_segunda_lista = 'Vazio'
nome_terceira_lista = 'Vazio'
invalid_input = True

while invalid_input:
    start()
    