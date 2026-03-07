#Importando módulos
from services import insert, select_one, select_all, update, delete
from utils import clear
import log_message
import validation

#Documentação do módulo
"""
main.py
-------

Descrição:
    Módulo principal da aplicação. Responsável por executar o menu interativo
    que permite ao usuário gerenciar os dados da tabela 'produtos' no banco
    de dados. Ele integra os módulos `services`, `validation`, `log_message`
    e `utils` para oferecer uma experiência completa de inserção, seleção,
    edição e exclusão de registros.

Principais funcionalidades:
    - Exibe menu interativo com opções de CRUD.
    - Valida entradas do usuário utilizando `validation`.
    - Executa operações no banco de dados via `services`.
    - Exibe mensagens de status, erros e avisos com `log_message`.
    - Mantém o terminal limpo e organizado com `utils.clear()`.

Uso:
    Executado diretamente para iniciar o sistema de gerenciamento de produtos.
    O usuário interage com o menu digitando opções e fornecendo os dados
    necessários para cada operação.
"""


#Criando loop infinito para o menu interativo
while True:
    print("-----Gerenciador de dados-----")
    print()
    print("Lista de comandos (1 a 4):")
    print(
        "1 - Inserir dados na tabela\n" \
        "2 - Selecionar dados da tabela\n" \
        "3 - Editar dados da tabela\n" \
        "4 - Deletar dados da tabela\n"
        )
    
    try:
        #Recebendo e verificando a escolha do usuário
        input_choice = input("Digite uma opção: ")
        verified_input_choice = validation.validate_option_number(input_choice)
    except ValueError:
        #Caso o dado seja inválido, exibe uma mensagem de erro e volta ao menu
        continue

    if verified_input_choice == 1:
        #Caso o usuário escolha inserir, executa as ações necessárias
        clear()
        try:
            #Recebendo e verificando os campos necessários para a inserção
            barcode_to_insert = input("Digite o código de barras do produto\n"
            "([INFO] Precisa ter 13 dígitos com números): ")
            verified_barcode_insert = validation.validate_barcode(barcode_to_insert)
            print()

            name_to_insert = input("Digite o nome do produto: ")
            verified_name_insert = validation.validate_name(name_to_insert)

            print()

            price_to_insert = input("Digite o preço do produto: ")
            verified_price_insert = validation.validate_price(price_to_insert)

            print()

            stock_to_insert = input("Digite a quantidade em estoque: ")
            verified_stock_insert = validation.validate_stock(stock_to_insert)

        except ValueError:
            #Se algo der como inválido, exibe uma mensagem de erro e volta ao menu
            continue

        #Caso tudo ocorra bem, exibe notificação e executa a inserção dos dados
        print(f"{log_message.notify_insertion()}")
        print()
        insert(verified_barcode_insert,verified_name_insert, verified_price_insert, verified_stock_insert)
        print()
        continue

    elif verified_input_choice == 2:
        #Caso o usuário escolha selecionar, executa as ações necessárias
        clear()

        #Criando segundo menu interativo
        print("Você deseja selecionar todos os dados da tabela ou somente um em específico?")
        print(
            "1 - Selecionar todos os dados\n" \
            "2 - Selecionar apenas um dado\n"
        )

        try:
            #Recebendo e verificando a escolha do usuário
            selected_method = input("Digite uma opção: ")
            verified_selected_method = validation.validate_option_number(selected_method)
        except ValueError:
            #Caso o dado seja inválido, exibe uma mensagem de erro e volta ao menu
            continue

        if verified_selected_method == 1:
            #Caso o usuário escolha selecionar tudo, executa a seleção de tudo
            print(f"{log_message.notify_selection()}")
            print()
            select_all()
            print()
            continue

        elif verified_selected_method == 2:
            #Caso o usuário escolha selecionar apenas um, executa as ações necessárias
            clear()
            try:
                #Recebendo e verificando o campo necessário para a seleção
                barcode_to_select = input("Digite o código de barras do produto que deseja selecionar\n"
                "([INFO] Precisa ter 13 dígitos com números): ")
                verified_barcode_select = validation.validate_barcode(barcode_to_select)
            except ValueError:
                #Caso o dado seja inválido, exibe uma mensagem de erro e volta ao menu
                continue

            #Caso tudo ocorra bem, exibe notificação e executa a seleção dos dados
            print(f"{log_message.notify_selection()}")
            print()
            select_one(verified_barcode_select)
            print()
            continue
    
        else:
            #Caso o usuário escolha uma opção que não existe no segundo menu, exibe notificação e volta ao menu inicial
            print(f"{log_message.notify_options_warning(1,2)}")
            print()
            continue
    
    elif verified_input_choice == 3:
        #Caso o usuário escolha editar, executa as ações necessárias
        clear()
        
        try:
            #Recebendo e verificando os campos necessários para a edição
            current_barcode = input("Digite o código de barras do produto que deseja alterar\n"
            "([INFO] Precisa ter 13 dígitos com números): ")
            verified_current_barcode = validation.validate_barcode(current_barcode)
            print()

            barcode_to_update = input("Digite o novo código de barras do produto: ")
            verified_barcode_update = validation.validate_barcode(barcode_to_update)
            print()

            name_to_update = input("Digite o novo nome do produto: ")
            verified_name_update = validation.validate_name(name_to_update)
            print()

            price_to_update = input("Digite o novo preço do produto: ")
            verified_price_update = validation.validate_price(price_to_update)
            print()

            stock_to_update = input("Digite a nova quantidade em estoque: ")
            verified_stock_update = validation.validate_stock(stock_to_update)

        except ValueError:
            #Se algo der como inválido, exibe uma mensagem de erro e volta ao menu
            continue

        #Caso tudo ocorra bem, exibe notificação e executa a edição dos dados
        print(f"{log_message.notify_change()}")
        print()
        update(verified_current_barcode, verified_barcode_update, verified_name_update, verified_price_update, verified_stock_update)
        print()
        continue

    elif verified_input_choice == 4:
        #Caso o usuário escolha deletar, executa as ações necessárias
        clear()
        try:
            #Recebendo e verificando o campo necessário para a deleção
            barcode_to_delete = input("Digite o código de barras do produto que deseja deletar\n"
            "([INFO] Precisa ter 13 dígitos com números): ")
            verified_barcode_delete = validation.validate_barcode(barcode_to_delete)

        except ValueError:
            #Caso o dado seja inválido, exibe uma mensagem de erro e volta ao menu
            continue

        #Caso tudo ocorra bem, exibe notificação e executa a deleção dos dados
        print(f"{log_message.notify_deletion()}")
        print()
        delete(verified_barcode_delete)
        print()
        continue

    else:
        #Caso o usuário escolha uma opção que não existe no menu inicial, exibe notificação e volta novamente ao mesmo
        print(f"{log_message.notify_options_warning(1,4)}")
        continue