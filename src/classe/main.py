from src.classe.list_creator import ListCreator
from src.classe.structure_functions import StructureFunction
from src.db.concrete.list_engine import ListEngine
from src.email import enviar_email

funcoes = StructureFunction
lista = ListCreator
engine = ListEngine
funcoes.initiation()
funcoes.quantidade_tabelas(funcoes.create_list)


def loop():
    while True:
        opcao = funcoes.start()

        if opcao == 1:
            listas = funcoes.tabelas_existentes_str(funcoes.create_list)
            funcoes.tabelas_existentes(listas)
            dicionario = funcoes.dict_list(listas)
            escolha = funcoes.escolhe_lista(dicionario)
            x = funcoes.list_viewer_new(escolha)
            enviar_email(x)
            loop()

        elif opcao == 2:
            listas = funcoes.tabelas_existentes_str(funcoes.create_list)
            funcoes.tabelas_existentes(listas)
            dicionario = funcoes.dict_list(listas)
            escolha = funcoes.escolhe_lista(dicionario)
            add_or_del = funcoes.adicionar_remover_atualizar()

            if add_or_del == 'A':
                funcoes.add_produtos(escolha)
                loop()

            elif add_or_del == 'R':
                funcoes.remover_produtos(escolha)
                loop()

            elif add_or_del == 'U':
                funcoes.update_product_or_amount(escolha)
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
            raise SystemExit

loop()

