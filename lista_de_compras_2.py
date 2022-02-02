import sys
# python -m projeto_lista


def inicio():
    print('*-' * 30)
    print(f'{" Lista de Compras ":=^60}')
    print('*-' * 30)


def dicionario_um():
    global dict_1
    dict_1 = dict()


def dicionario_dois():
    global dict_2
    dict_2 = dict()


def nome_da_primeira_lista():
    global nome_primeira_lista
    nome_primeira_lista = input('Escolha o nome da sua primeira lista:\n').capitalize()


def nome_da_segunda_lista():
    global nome_segunda_lista
    nome_segunda_lista = input('Escolha o nome da sua segunda lista:\n').capitalize()


def visualizador_de_listas():
    print(lista_atual)
    if dict_atual == {}:
        print('A lista está vazia')
    else:
        print(dict_atual)
        start()


def add_produtos():
    while True:
        produto = input('Digite o produto que deseja adicionar: (Para sair pressione "X") ').capitalize()

        if produto == "X":
            start()

        else:
            quantidade = int(input('Quantidade?: '))

            dict_1[produto] = quantidade
            print(f'Produto {produto} adicionado com sucesso')


def alterador_lista_um(lista_atual):
	lista_atual = nome_primeira_lista
	return lista_atual
    

def alterador_lista_dois(lista_atual):
	lista_atual = nome_segunda_lista
	return lista_atual


def alterador_dict_um(dict_atual):
    dict_atual = dict_1
    return dict_atual


def alterador_dict_dois(dict_atual):
    dict_atual = dict_2
    return dict_atual


def start():
    opcao = int(input("""Selecione a opção que você deseja: 
        [ 1 ] - Visualizar lista 
        [ 2 ] - Adicionar/remover itens na lista
        [ 4 ] - Ver todas as listas
        [ 3 ] - Fechar o programa\n\n"""))


    if opcao == 1:
        visualizador_de_listas()

    elif opcao == 2:
        add_or_del = input('Deseja adicionar ou Remover produtos? ( A ) para Adicionar e ( R ) para Remover ').upper()

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

    elif opcao == 3:
        print('Finalizando programa, até mais!')
        sys.exit()

    elif opcao == 4:
        escolha = int(input(f'Escolha qual lista deseja selecionar: 0 - Criar uma lista nova 1 - {nome_primeira_lista.capitalize()} 2 - {nome_segunda_lista.capitalize()}'))
        if escolha == 1:
            lista_atual = ''
            dict_atual = []
            lista_atual = alterador_lista_um(lista_atual)
            dict_atual = alterador_dict_um(dict_atual)
            print(f'Agora você está na lista {nome_primeira_lista}')
            start()

        elif escolha == 2:
            nome_da_segunda_lista()
            lista_atual = ''
            dict_atual = []
            lista_atual = alterador_lista_dois(lista_atual)
            dict_atual = alterador_dict_dois(dict_atual)
            print(f'Agora você está na lista {nome_segunda_lista}')
            start()


dicionario_um()
dicionario_dois()
nome_da_primeira_lista()
inicio()

dict_atual = {}
lista_atual = nome_primeira_lista
nome_segunda_lista = 'vazio'
dict_2 = {}
invalid_input = True

while invalid_input:
    start()
