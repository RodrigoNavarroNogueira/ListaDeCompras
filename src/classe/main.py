from src.classe.list_creator import ListCreator
from src.classe.structure_functions import StructureFunction
from src.db.concrete.list_engine import ListEngine
from src.email import enviar_email, receber_email

funcoes = StructureFunction
lista = ListCreator
engine = ListEngine
funcoes.initiation()
funcoes.quantidade_tabelas(funcoes.create_first_list)


def loop():
    while True:
        opcao = funcoes.start()

        if opcao == 1:
            lista_sem_tupla = []
            listas = funcoes.tabelas_existentes_str(funcoes.create_list, lista_sem_tupla)
            lista_sem_tupla = [item for tupla in listas for item in tupla]
            funcoes.tabelas_existentes(listas)
            dicionario = funcoes.dict_list(listas)
            escolha = funcoes.escolhe_lista(dicionario, funcoes.tabelas_existentes, listas)
            if escolha == 0:
                loop()
            x = funcoes.list_viewer_new(escolha)
            y = receber_email(x)
            if y == 1:
                enviar_email(x)
            else:
                loop()

        elif opcao == 2:
            lista_sem_tupla = []
            listas = funcoes.tabelas_existentes_str(funcoes.create_list, lista_sem_tupla)
            lista_sem_tupla = [item for tupla in listas for item in tupla]
            funcoes.tabelas_existentes(listas)
            dicionario = funcoes.dict_list(listas)
            escolha = funcoes.escolhe_lista(dicionario, funcoes.tabelas_existentes, listas)
            if escolha == 0:
                loop()
            add_or_del = funcoes.adicionar_remover_atualizar()

            if add_or_del == 'A':
                funcoes.add_produtos(escolha)
                loop()

            elif add_or_del == 'R':
                funcoes.list_viewer_new(escolha)
                funcoes.remover_produtos(escolha)
                loop()

            elif add_or_del == 'U':
                funcoes.list_viewer_new(escolha)
                funcoes.update_product_or_amount(escolha)
                loop()

        elif opcao == 3:
            lista_sem_tupla = []
            listas = funcoes.tabelas_existentes_str(funcoes.create_list, lista_sem_tupla)
            escolha = funcoes.criar_excluir_renomear()
            lista_sem_tupla = [item for tupla in listas for item in tupla]

            if escolha == 1:
                funcoes.create_list(lista_sem_tupla)
                loop()

            elif escolha == 2:
                listas = funcoes.tabelas_existentes_str(funcoes.create_list, lista_sem_tupla)
                funcoes.tabelas_existentes(listas)
                dicionario = funcoes.dict_list(listas)
                funcoes.delete_list(dicionario, funcoes.tabelas_existentes, listas)
                loop()
                
            elif escolha == 3:
                listas = funcoes.tabelas_existentes_str(funcoes.create_list, lista_sem_tupla)
                funcoes.tabelas_existentes(listas)
                dicionario = funcoes.dict_list(listas)
                escolha = funcoes.escolhe_lista(dicionario, funcoes.tabelas_existentes, listas)
                if escolha == 0:
                    loop()
                else:
                    funcoes.rename_list(escolha)
                    loop()

        elif opcao == 4:
            print('\nFinalizando o programa, até mais!\n')
            raise SystemExit

loop()
