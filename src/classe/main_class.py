from src.classe.list_creator import ListCreator
from src.classe.structure_functions import StructureFunction
from src.db.concrete.list_engine import ListEngine

funcoes = StructureFunction
lista = ListCreator
engine = ListEngine()
funcoes.initiation()
list_name = funcoes.name_list()
option = funcoes.start()

if option == 1:
    funcoes.list_viewer(list_name)
    funcoes.start()

elif option == 2:
    funcoes.lista_para_manipular(list_name)
    escolha = funcoes.adicionar_remover_atualizar()

    if escolha == 'A':
        funcoes.add_produtos(list_name)
        funcoes.start()

    elif escolha == 'R':
        funcoes.remover_produtos()
        funcoes.start()

    elif escolha == 'U':
        ...
