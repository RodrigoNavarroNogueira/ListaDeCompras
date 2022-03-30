from src.classe.list_creator import ListCreator
from src.classe.structure_functions import StructureFunction
from src.db.concrete.list_engine import ListEngine

funcoes = StructureFunction
lista = ListCreator
engine = ListEngine
funcoes.initiation()
list_name = funcoes.name_list()


def loop():
    while True:
        opcao = funcoes.start()

        if opcao == 1:
            funcoes.list_viewer(list_name)
            loop()

        elif opcao == 2:
            funcoes.lista_para_manipular(list_name)
            escolha = funcoes.adicionar_remover_atualizar()

            if escolha == 'A':
                funcoes.add_produtos(list_name)
                loop()

            elif escolha == 'R':
                funcoes.remover_produtos()
                loop()

            elif escolha == 'U':
                funcoes.update_product_or_amount()
                loop()

        elif opcao == 3:
            escolha = funcoes.escolha_da_lista(list_name)

            if escolha == 1:
                funcoes.name_list()
                loop()

loop()
