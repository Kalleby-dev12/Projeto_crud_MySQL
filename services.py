#Importando biliotecas e módulos
import os
import dotenv
import mysql.connector as mysql
import log_message_db

#Documentação do módulo
"""
services.py
-----------

Descrição:
    Módulo responsável por gerenciar os serviços de integração com o banco de dados
    MySQL, oferecendo funções para conexão e operações CRUD (Create, Read, Update, Delete)
    na tabela 'produtos'. Todas as operações são acompanhadas de mensagens de status
    fornecidas pelo módulo `log_message_db`.

Principais funcionalidades:
    - _create_connection(): cria e valida a conexão com o banco.
    - insert(): insere um novo produto na tabela.
    - select_all(): retorna todos os produtos cadastrados.
    - select_one(): busca um produto específico pelo código de barras.
    - update(): atualiza os dados de um produto existente.
    - delete(): remove um produto da tabela.

Uso:
    Importado em módulos de aplicação que precisam manipular dados de produtos
    no banco de forma segura e organizada, exibindo mensagens de status, erros
    e avisos durante cada operação.
"""


#Carregando as variáveis de ambiente
dotenv.load_dotenv()

def _create_connection():
    #Documentação da função
    """
    Cria uma conexão com o servidor de banco de dados

    Raises:
        mysql.OperationalError: Se houver algum erro ao tentar se conectar com o banco de dados

    Returns:
        MySQLConnectionAbstract|PooledMySQLConnection:
            (MySQLConnectionAbstract) Quando houver uma conexão direta

            (PooledMySQLConnection) Quando houver uma conexão configurada
        
    Example:
        >>> connection = _create_connection()
        [DB.STATUS] Criando conexão com o banco de dados...
        connection = mysql.connect(
            host=os.environ['EXAMPLE'],
            user=os.environ['EXAMPLE'],
            password=os.environ['EXAMPLE'],
            database=os.environ['EXAMPLE']
        )
        [DB.STATUS] Conectado!
    """

    #Código da função
    print(f"{log_message_db.notify_connection_on_creation()}")
    try:
        connection = mysql.connect(
            host=os.environ['MYSQL_DB_HOST'],
            user=os.environ['MYSQL_DB_USER'],
            password=os.environ['MYSQL_DB_PASSWORD'],
            database=os.environ['MYSQL_DB_NAME']
        )
        print()
        print(f"{log_message_db.notify_successful_connection()}")
        print()
        return connection
    
    except mysql.OperationalError as e:
        #capturando possíveis erros
        print(f"{log_message_db.notify_connection_error_db(e)}")



def insert(barcode: str, name: str, price: float, stock: int) -> None:
    #Documentação da função
    """
    Insere um novo produto na tabela 'produtos'.

    Args:
        barcode (str): Código de barras do produto (deve ser único, conter apenas números e ter 13 digitos).
        name (str): Nome do produto.
        price (float): Preço do produto.
        stock (int): Quantidade em estoque.

    Raises:
        mysql.IntegrityError: Se o código de barras já existir na tabela.
        mysql.OperationalError: Se houver falha na conexão com o banco.

    Returns:
        None: A função não retorna nada, apenas insere na tabela os dados do produto 
        e imprime mensagens de status.
    
    Example:
        >>> insert("1234567891234", "Camiseta", 59.90, 10)
        [DB.INFO] Comando executado com sucesso!
        [DB.INFO] 1 linhas modificada
    """

    #Código da função
    #Criando conexão chamando a funcão
    connection = _create_connection()

    with connection:
        #Usando context manager do python para ser responsável por abrir e fechar a conexão automaticamente

        with connection.cursor() as cursor:
            #Usando context manager do python para ser responsável por abrir e fechar o cursor automaticamente

            #Criando código sql com placeholders
            sql_code = """
                INSERT INTO produtos (cod_barras, nome, preco, estoque) 
                VALUES (%s, %s, %s, %s)
            """
            values = (barcode, name, price, stock)
            try:
                print(f"{log_message_db.notify_command_in_execution()}")
                cursor.execute(sql_code, values)
                connection.commit()
                print()
                print(f"{log_message_db.notify_executed_command()}")
                print()

                #Printando quantas linhas da tabela foram modificadas
                print(f"{log_message_db.notify_modified_lines(cursor)}")

            except mysql.IntegrityError:
                #Capturando possível erro, caso o usuário insire um codigo de barras que ja existe na tabela
                print()
                print(f"{log_message_db.notify_integrity_error_db(barcode)}")



def select_all() -> None:
    #Documentação da função
    """
    Seleciona e mostra os dados de todos os produtos da tabela 'produtos'.

    Raises:
        mysql.OperationalError: Se houver falha na conexão com o banco.

    Returns:
        None: A função não retorna nada, apenas mostra todos os dados da tabela
        e imprime mensagens de status.
    
    Example:
        >>> select_all()
        [DB.INFO] Executando o comando...
        "-----------Produto 1-----------"
        "ID: 2"
        "CÓDIGO DE BARRAS: 8765435678765"
        "NOME: Notebook"
        "PREÇO: 3654.76"
        "QUANTIDADE EM ESTOQUE: 110"
        "-----------Produto 2-----------"
        "ID: 3"
        "CÓDIGO DE BARRAS: 8754376890098"
        "NOME: Celular"
        "PREÇO: 1894.55"
        "QUANTIDADE EM ESTOQUE: 67"
        [DB.INFO] Comando executado com sucesso!
        [DB.INFO] 2 linhas retornadas
    """

    #Código da função
    #Criando conexão chamando a funcão
    connection = _create_connection()

    with connection:
        #Usando context manager do python para ser responsável por abrir e fechar a conexão automaticamente

        with connection.cursor() as cursor:
            #Usando context manager do python para ser responsável por abrir e fechar o cursor automaticamente

            #Criando índice, só para melhorar e exibição... ex: "produto 1", "produto 2", "produto 3" e etc
            i = 1

            #Criando código sql
            sql_code = """
                SELECT * FROM produtos
            """
            print(f"{log_message_db.notify_command_in_execution()}")
            cursor.execute(sql_code)

            #Pegando os dados da tabela do banco de dados
            table_datas = cursor.fetchall()
            if table_datas:
                #Caso haja dados, isso correrá
                for column_data in table_datas:
                    #Printando os dados com o índice das tuplas, de acordo com as colunas na tabela
                    print()
                    print(f"-----------Produto {i}-----------")
                    print(f"ID: {column_data[0]}")
                    print(f"CÓDIGO DE BARRAS: {column_data[1]}")
                    print(f"NOME: {column_data[2]}")
                    print(f"PREÇO: {column_data[3]}")
                    print(f"QUANTIDADE EM ESTOQUE: {column_data[4]}")
                    i += 1
                print()
                print(f"{log_message_db.notify_executed_command()}")
            else:
                #Caso não haja nada, isso correrá, pois tentar selecionar dados de uma tabela vazia, não é levantado nenhum erro, só é mostrado que nenhuma linha foi retornada
                print()
                print(f"{log_message_db.notify_executed_command()}")
                print()
                print(f"{log_message_db.notify_warning_empty_db()}")

            #Printando quantas linhas da tabela foram mostradas
            print()
            print(f"{log_message_db.notify_returned_lines(cursor)}")

            

def select_one(barcode_inserted: str) ->None:
    #Documentação da função
    """
    Seleciona e mostra os dados de um único produto da tabela 'produtos'.

    Args:
        barcode_inserted (str): Código de barras do produto a ser selecionado (deve ja existir na tabela, conter apenas números e ter 13 digitos).

    Raises:
        mysql.OperationalError: Se houver falha na conexão com o banco.

    Returns:
        None: A função não retorna nada, apenas mostra os dados do produto escolhido
        e imprime mensagens de status.
    
    Example:
        >>> select_one("7865678987653")
        [DB.INFO] Executando o comando...
        "-----------Produto selecionado-----------"
        "ID: 7"
        "CÓDIGO DE BARRAS: 7865678987653"
        "NOME: Geladeira"
        "PREÇO: 4567.99"
        "QUANTIDADE EM ESTOQUE: 33"
        [DB.INFO] Comando executado com sucesso!
        [DB.INFO] 1 linha retornada
    """
    #Código da função
    #criando conexão chamando a funcão
    connection = _create_connection()

    with connection:
        #Usando context manager do python para ser responsável por abrir e fechar a conexão automaticamente

        with connection.cursor() as cursor:
            #Usando context manager do python para ser responsável por abrir e fechar o cursor automaticamente

            #Criando código sql com placeholders
            sql_code = """
                SELECT * FROM produtos WHERE cod_barras = %s
            """
            value = (barcode_inserted,)

            print(f"{log_message_db.notify_command_in_execution()}")
            cursor.execute(sql_code, value)
            table_data = cursor.fetchone()
            if table_data:
                #Caso haja algum dado, isso ocorrerá
                #Printando os dados de acordo com o índice da tupla
                print()
                print("--------Produto selecionado--------")
                print(f"ID: {table_data[0]}")
                print(f"CÓDIGO DE BARRAS: {table_data[1]}")
                print(f"NOME: {table_data[2]}")
                print(f"PREÇO: {table_data[3]}")
                print(f"QUANTIDADE EM ESTOQUE: {table_data[4]}")
                print()
                print(f"{log_message_db.notify_executed_command()}")
            else:
                #Caso não haja nada, isso correrá, pois tentar selecionar um dado com filtro WHERE, utilizando um valor que ainda não existe em uma coluna, não é levantado nenhum erro, só é mostrado que nenhuma linha foi retornada

                print()
                print(f"{log_message_db.notify_executed_command()}")
                print()
                print(f"{log_message_db.notify_warning_db(barcode_inserted)}")

            #Printando quantas linhas da tabela foram mostradas
            print()
            print(f"{log_message_db.notify_returned_lines(cursor)}")


                
def update(current_barcode: str, new_barcode: str, new_name: str, new_price: float, new_stock: int) -> None:
    #Documentação da função
    """
    Atualiza os dados de um produto já existente na tabela 'produtos'.

    Args:
        current_barcode (str): Código de barras do produto a ser selecionado para atualização (já deve existir na tabela,conter apenas números e ter 13 digitos).
        new_barcode (str): Novo código de barras para esse produto (deve ser único, conter apenas números e ter 13 digitos).
        new_name (str): Novo nome para esse produto.
        new_price (float): Novo preço para esse produto.
        new_stock (int): Nova quantidade em estoque desse produto.

    Raises:
        mysql.IntegrityError: Se o código de barras já existir na tabela.
        mysql.OperationalError: Se houver falha na conexão com o banco.

    Returns:
        None: A função não retorna nada, apenas atualiza a tabela com os novos dados do produto escolhido 
        e imprime mensagens de status.
    
    Example:
        >>> update("7865678476534","0098765478345", "impressora", 1488.90, 31)
        [DB.INFO] Comando executado com sucesso!
        [DB.INFO] 1 linhas modificada
    """

    #Código da função
    #Criando conexão chamando a funcão
    connection = _create_connection()

    with connection:
        #Usando context manager do python para ser responsável por abrir e fechar a conexão automaticamente

        with connection.cursor() as cursor:
            #Usando context manager do python para ser responsável por abrir e fechar o cursor automaticamente

            #Criando código sql com placeholders
            sql_code = """
                UPDATE produtos SET cod_barras = %s, nome = %s, preco = %s, estoque = %s 
                WHERE cod_barras = %s
            """
            values = (new_barcode, new_name, new_price, new_stock, current_barcode)
            try:
                print(f"{log_message_db.notify_command_in_execution()}")
                cursor.execute(sql_code, values)
                connection.commit()
                print()
                print(f"{log_message_db.notify_executed_command()}")
                print()

                if cursor.rowcount == 0:
                    #Verificando se realmente alguma linha foi modificada, pois tentar atualizar um dado com filtro WHERE, utilizando um valor que ainda não existe em uma coluna, não é levantado nenhum erro, só é mostrado que nenhuma linha foi retornada

                    print(f"{log_message_db.notify_warning_db(current_barcode)}")
                    print()

                #Printando quantas linhas da tabela foram modificadas
                print(f"{log_message_db.notify_modified_lines(cursor)}")
            except mysql.IntegrityError:
                #capturando possível erro, caso o usuário insire um codigo de barras que ja existe na tabela

                print()
                print(f"{log_message_db.notify_integrity_error_db(new_barcode)}")



def delete(barcode_inserted: str) -> None:
    #Documentação da função
    """
    Deleta todos os dados de um único produto da tabela 'produtos'.

    Args:
        barcode_inserted (str): Código de barras do produto a ser deletado (já deve existir na tabela, conter apenas números e ter 13 digitos).

    Raises:
        mysql.OperationalError: Se houver falha na conexão com o banco.

    Returns:
        None: A função não retorna nada, apenas deleta da tabela, todos os dados do produto escolhido 
        e imprime mensagens de status.
    
    Example:
        >>> delete("9878567489876")
        [DB.INFO] Comando executado com sucesso!
        [DB.INFO] 1 linhas modificada
    """

    #Código da função
    #Criando conexão chamando a funcão
    connection = _create_connection()

    with connection:
        #Usando context manager do python para ser responsável por abrir e fechar a conexão automaticamente

        with connection.cursor() as cursor:
            #Usando context manager do python para ser responsável por abrir e fechar o cursor automaticamente

            #Criando código sql com placeholders
            sql_code = """
                DELETE FROM produtos WHERE cod_barras = %s
            """
            value = (barcode_inserted,)

            print(f"{log_message_db.notify_command_in_execution()}")
            cursor.execute(sql_code, value)
            connection.commit()
            print()
            print(f"{log_message_db.notify_executed_command()}")
            print()
            if cursor.rowcount == 0:
                #Verificando se realmente alguma linha foi modificada, pois tentar deletar um dado com filtro WHERE, utilizando um valor que ainda não existe em uma coluna, não é levantado nenhum erro, só é mostrado que nenhuma linha foi retornada
                print(f"{log_message_db.notify_warning_db(barcode_inserted)}")
                print()
            
            #Printando quantas linhas da tabela foram modificadas
            print(f"{log_message_db.notify_modified_lines(cursor)}")