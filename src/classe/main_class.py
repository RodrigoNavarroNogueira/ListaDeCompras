from datetime import datetime

import sqlite3

from src.classe.list_creator import ListCreator
from src.classe.structure_functions import StructureFunction

funcoes = StructureFunction
lista = ListCreator
funcoes.initiation()
list_name = funcoes.name_list()
option = funcoes.start()


if option == 1:
    funcoes.list_viewer(list_name)
    funcoes.start()

elif option == 2:
    print('chegou')
    funcoes.lista_para_manipular(list_name)
    add = funcoes.adicionar_ou_remover()

    if add == 'A':
        print('chegou')
        #add_produtos()
