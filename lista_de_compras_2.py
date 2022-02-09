import sys
# corrigindo bugs e diminuindo as linha de codigo
# melhorar o input da visualização de listas
def inicio():
    print('*-' * 30)
    print(f'{" Lista de Compras ":=^60}')
    print('*-' * 30)


def nome_da_primeira_lista():
    global nome_primeira_lista
    nome_primeira_lista = input('Escolha o nome da sua primeira lista:\n').capitalize()


def nome_da_primeira_lista_vazia():
    global nome_primeira_lista
    nome_primeira_lista = 'Vazio'


def nome_da_segunda_lista():
    global nome_segunda_lista
    nome_segunda_lista = input('Escolha o nome da sua segunda lista:\n').capitalize()


def nome_da_segunda_lista_vazia():
    global nome_segunda_lista
    nome_segunda_lista = 'Vazio'


def nome_da_terceira_lista():
    global nome_terceira_lista
    nome_terceira_lista = input('Escolha o nome da sua terceira lista:\n').capitalize()


def nome_da_terceira_lista_vazia():
    global nome_terceira_lista
    nome_terceira_lista = 'Vazio'


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
            break
        else:
            quantidade = int(input('Quantidade?: '))
            dict_1[produto] = quantidade
            print(f'Produto {produto} adicionado com sucesso')


def add_produtos_dois():
    while True:
        produto = input('Digite o produto que deseja adicionar: (Para sair pressione "X") ').capitalize()
        if produto == "X":
            break
        else:
            quantidade = int(input('Quantidade?: '))
            dict_2[produto] = quantidade
            print(f'Produto {produto} adicionado com sucesso')


def add_produtos_tres():
    while True:
        produto = input('Digite o produto que deseja adicionar: (Para sair pressione "X") ').capitalize()
        if produto == "X":
            break
        else:
            quantidade = int(input('Quantidade?: '))
            dict_3[produto] = quantidade
            print(f'Produto {produto} adicionado com sucesso')


def start():
    opcao = int(input("""Selecione a opção que você deseja: 
        [ 1 ] - Visualizar Listas 
        [ 2 ] - Adicionar/Remover Itens na Lista
        [ 3 ] - Criar/Excluir e Renomear uma Lista
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
                start()
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
            f'Escolha uma Lista Vazia para cria-la: (Para excluir uma lista pressione 0 e para renomear pressione o número correspondente)\n(1) - {nome_primeira_lista}\n(2) - {nome_segunda_lista}\n(3) - {nome_terceira_lista}\n'))
        if escolha == 1:
            if nome_primeira_lista != "Vazio":
                certeza = input('Tem certeza que quer renomear essa lista? (S) para SIM e (N) para NÃO:\n').upper()
                if certeza == "S":
                    nome_da_primeira_lista()
                    nome_todas_listas.insert(0, nome_primeira_lista)
                    print(f'Você criou a lista {nome_primeira_lista}!')
                    start()
                else:
                    start()
            else:
                nome_da_primeira_lista()
                print(f'Você criou a lista {nome_primeira_lista}!')
                start()

        elif escolha == 2:
            if nome_segunda_lista != "Vazio":
                certeza = input('Tem certeza que quer renomear essa lista? (S) para SIM e (N) para NÃO:\n').upper()
                if certeza == "S":
                    nome_da_segunda_lista()
                    nome_todas_listas.insert(1, nome_segunda_lista)
                    print(f'Você criou a lista {nome_segunda_lista}!')
                    start()
                else:
                    start()
            else:
                nome_da_segunda_lista()
                print(f'Você criou a lista {nome_segunda_lista}!')
                start()

        elif escolha == 3:
            if nome_terceira_lista != "Vazio":
                certeza = input('Tem certeza que quer renomear essa lista? (S) para SIM e (N) para NÃO:\n').upper()
                if certeza == "S":
                    nome_da_terceira_lista()
                    nome_todas_listas.insert(2, nome_terceira_lista)
                    print(f'Você criou a lista {nome_terceira_lista}!')
                    start()
                else:
                    start()
            else:
                nome_da_terceira_lista()
                print(f'Você criou a lista {nome_terceira_lista}!')
                start()

        elif escolha == 0:
            list_del = int(input(f'Digite o número da lista para exclui-la: (Para CANCELAR pressione 0)\n(1) - {nome_primeira_lista}\n(2) - {nome_segunda_lista}\n(3) - {nome_terceira_lista}\n'))
            if list_del == 1:
                dict_1.clear()
                nome_todas_listas.pop(0)
                print(f'A lista {nome_primeira_lista} foi excluida!')
                create_new_list = input('Deseja criar novamente uma lista agora? (S) Para SIM e (N) Para NÃO:\n').upper()
                if create_new_list == "S":
                    nome_da_primeira_lista()
                    nome_todas_listas.insert(0, nome_primeira_lista)
                    start()
                else:
                    nome_da_primeira_lista_vazia()
                    nome_todas_listas.insert(0, nome_primeira_lista)
                    start()

            if list_del == 2:
                dict_2.clear()
                nome_todas_listas.pop(1)
                print(f'A lista {nome_segunda_lista} foi excluida!')
                create_new_list = input('Deseja criar novamente uma lista agora? (S) Para SIM e (N) Para NÃO:\n').upper()
                if create_new_list == "S":
                    nome_da_segunda_lista()
                    nome_todas_listas.insert(1, nome_segunda_lista)
                    start()
                else:
                    nome_da_segunda_lista_vazia()
                    nome_todas_listas.insert(1, nome_segunda_lista)
                    start()

            if list_del == 3:
                dict_3.clear()
                nome_todas_listas.pop(2)
                print(f'A lista {nome_terceira_lista} foi excluida!')
                create_new_list = input('Deseja criar novamente uma lista agora? (S) Para SIM e (N) Para NÃO:\n').upper()
                if create_new_list == "S":
                    nome_da_terceira_lista()
                    nome_todas_listas.insert(2, nome_terceira_lista)
                    start()
                else:
                    nome_da_terceira_lista_vazia()
                    nome_todas_listas.insert(2, nome_terceira_lista)
                    start()
                if list_del == 0:
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
nome_todas_listas = [nome_primeira_lista, nome_segunda_lista, nome_terceira_lista]
invalid_input = True

while invalid_input:
    start()