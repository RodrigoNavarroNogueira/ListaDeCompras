from src.classe.list_creator import ListCreator
from src.classe.structure_functions import StructureFunction
from src.db.concrete.list_engine import ListEngine

funcoes = StructureFunction
lista = ListCreator
engine = ListEngine
funcoes.initiation()
tables = funcoes.tabelas_existentes()
# adicionar uma condição nessa funcao caso tenha itens na lista das tabelas 
list_name = funcoes.create_list()


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
            escolha = funcoes.criar_excluir_renomear()

            if escolha == 0:
                funcoes.create_list()
                loop()

            elif escolha == 1:
                funcoes.delete_list()
                loop()
                
            elif escolha == 2:
                funcoes.rename_list()
                loop()

        elif opcao == 4:
            print('Finalizando programa, até mais!')
            break

loop()
