#Importações de outro módulo
from utils import show_moment,color_to_green,color_to_red,color_to_yellow

#Documentação do módulo
"""
log_message_db.py
-----------------

Descrição:
    Módulo responsável por exibir mensagens de log relacionadas ao banco de dados.
    Ele fornece feedback visual e informativo sobre conexões, execução de comandos
    SQL e possíveis erros ou avisos durante operações.

Principais funcionalidades:
    - notify_connection_error_db(): informa falhas de conexão.
    - notify_integrity_error_db(): alerta sobre códigos de barras duplicados.
    - notify_warning_empty_db(): avisa quando a tabela está vazia.
    - notify_warning_db(): avisa quando não encontra produto pelo código de barras.
    - notify_connection_on_creation(): indica criação de conexão.
    - notify_successful_connection(): confirma conexão estabelecida.
    - notify_command_in_execution(): indica execução de comando SQL.
    - notify_executed_command(): confirma comando executado com sucesso.
    - notify_modified_lines(): mostra quantas linhas foram modificadas.
    - notify_returned_lines(): mostra quantas linhas foram retornadas.

Uso:
    Importado em módulos que interagem com o banco de dados para fornecer
    mensagens claras, com timestamp e cores ANSI, ajudando na depuração
    e acompanhamento das operações.
"""


def notify_connection_error_db(error: Exception) -> str:
    #Documentação da função
    """
    Retorna uma mensagem de erro de conexão com o banco de dados.

    Args:
        error (Exception): Exceção capturada durante a tentativa de conexão.

    Returns:
        str: Mensagem formatada com timestamp e descrição do erro.

    Example:
        >>> print(notify_connection_error_db('Timeout'))
        [16:05:23.123] [DB.ERROR]: Não foi possível se conectar ao banco de dados
        (Timeout)
    """

    #Código da função
    return f"{show_moment()} {color_to_red('[DB.ERROR]')}: Não foi possível se conectar ao banco de dados\n({error})"



def notify_integrity_error_db(barcode: str) -> str:
    #Documentação da função
    """
    Retorna uma mensagem de erro de integridade ao tentar inserir um produto
    com código de barras já existente.

    Args:
        barcode (str): Código de barras duplicado.

    Returns:
        str: Mensagem formatada com timestamp e descrição do erro.

    Example:
        >>> print(notify_integrity_error_db('9878765456765'))
        [16:05:23.123] [DB.ERROR]: Já existe um produto cadastrado com o código de barras: '9878765456765'
    """

    #Código da função
    return f"{show_moment()} {color_to_red('[DB.ERROR]')}: Já existe um produto cadastrado com o código de barras: '{barcode}'"



def notify_warning_empty_db() -> str:
    #Documentação da função
    """
    Retorna uma mensagem de aviso quando a tabela do banco está vazia.

    Returns:
        str: Mensagem formatada com timestamp e indicador de aviso.

    Example:
        >>> print(notify_warning_empty_db())
        [16:05:23.123] [DB.WARNING]: Não há dados na tabela
    """

    #Código da função
    return f"{show_moment()} {color_to_yellow('[DB.WARNING]')}: Não há dados na tabela"



def notify_warning_db(barcode_inserted: str) -> str:
    #Documentação da função
    """
    Retorna uma mensagem de aviso quando não é possível encontrar um produto
    pelo código de barras informado.

    Args:
        barcode_inserted (str): Código de barras buscado.

    Returns:
        str: Mensagem formatada com timestamp e indicador de aviso.

    Example:
        >>> print(notify_warning_db('7676765678765'))
        [16:05:23.123] [DB.WARNING]: Não foi possível encontrar o produto que contém o código de barras: '7676765678765'
    """

    #Código da função
    return f"{show_moment()} {color_to_yellow('[DB.WARNING]')}: Não foi possível encontrar o produto que contém o código de barras: '{barcode_inserted}'"



def notify_connection_on_creation() -> str:
    #Documentação da função
    """
    Retorna uma mensagem indicando que a conexão com o banco está sendo criada.

    Returns:
        str: Mensagem formatada com timestamp e status.

    Example:
        >>> print(notify_connection_on_creation())
        [16:05:23.123] [DB.STATUS]: Criando conexão com o banco de dados...
    """

    #Código da função
    return f"{show_moment()} {color_to_green('[DB.STATUS]')}: Criando conexão com o banco de dados..."



def notify_successful_connection() -> str:
    #Documentação da função
    """
    Retorna uma mensagem indicando que a conexão com o banco foi estabelecida.

    Returns:
        str: Mensagem formatada com timestamp e status.

    Example:
        >>> print(notify_successful_connection())
        [16:05:23.123] [DB.STATUS]: Conectado!
    """

    #Cógigo da função
    return f"{show_moment()} {color_to_green('[DB.STATUS]')}: Conectado!"



def notify_command_in_execution() -> str:
    #Documentação da função
    """
    Retorna uma mensagem indicando que um comando SQL está em execução.

    Returns:
        str: Mensagem formatada com timestamp e status.

    Example:
        >>> print(notify_command_in_execution())
        [16:05:23.123] [DB.INFO]: Executando o comando...
    """

    #Código da função
    return f"{show_moment()} {color_to_green('[DB.INFO]')}: Executando o comando..."



def notify_executed_command() -> str:
    #Documentação da função
    """
    Retorna uma mensagem indicando que um comando SQL foi executado.

    Returns:
        str: Mensagem formatada com timestamp e status.

    Example:
        >>> print(notify_executed_command())
        [16:05:23.123] [DB.INFO]: Comando executado!
    """

    #Código da função
    return f"{show_moment()} {color_to_green('[DB.INFO]')}: Comando executado!"



def notify_modified_lines(cursor) -> str:
    #Documentação da função
    """
    Retorna uma mensagem indicando quantas linhas foram modificadas
    após a execução de um comando SQL.

    Args:
        cursor (mysql.connector.cursor.MySQLCursor): Cursor após execução do comando.

    Returns:
        str: Mensagem formatada com timestamp e número de linhas modificadas.

    Example:
        >>> notify_modified_lines(cursor)
        [16:05:23.123] [DB.INFO]: 1 Linha modificada
    """

    #Código da função
    return f"{show_moment()} {color_to_green('[DB.INFO]')}: {cursor.rowcount} Linha modificada"



def notify_returned_lines(cursor) -> str:
    #Documentação da função
    """
    Retorna uma mensagem indicando quantas linhas foram retornadas
    após a execução de um comando SQL.

    Args:
        cursor (mysql.connector.cursor.MySQLCursor): Cursor após execução do comando.

    Returns:
        str: Mensagem formatada com timestamp e número de linhas retornadas.

    Example:
        >>> notify_returned_lines(cursor)
        [16:05:23.123] [DB.INFO]: 5 linhas retornadas
    """

    #Código da função
    return f"{show_moment()} {color_to_green('[DB.INFO]')}: {cursor.rowcount} linhas retornadas"