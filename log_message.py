#Importações de outro módulo
from utils import show_moment,color_to_green,color_to_red,color_to_yellow,clear

#Documentação do módulo
"""
log_message.py
--------------

Descrição:
    Módulo responsável por exibir mensagens de log no terminal com timestamp
    e cores ANSI, destacando erros, avisos e informações do sistema.

Principais funcionalidades:
    - notify_*(): funções que exibem mensagens específicas de erro, aviso ou status.
    - show_moment(): gera o horário atual formatado para logs.
    - clear(): limpa o terminal antes de mostrar novas mensagens.
    - color_to_*(): aplica cores ANSI (verde, vermelho, amarelo, ciano) ao texto.

Uso:
    Importado em módulos de validação e operações de banco de dados para
    fornecer feedback claro e visual ao usuário durante a execução.
"""



def notify_value_error() -> str:
    #Documentação da função
    """
    Retorna uma mensagem de erro para valores inválidos.

    Returns:
        str: Mensagem formatada com timestamp e indicador de erro.

    Example:
        >>> print(notify_value_error())
        [16:05:23.123] [ERROR]: Valor inválido
        - É permitido somente a entrada de números nesse campo
        Por gentileza, tente novamente
    """
    clear()
    msg = "- É permitido somente a entrada de números nesse campo\n" \
    "Por gentileza, tente novamente\n\n"
    return f"{show_moment()} {color_to_red('[ERROR]')}: Valor inválido\n{msg}"



def notify_options_warning(n1: int, n2: int) -> str:
    #Documentação da função
    """
    Retorna uma mensagem de aviso quando o usuário escolhe uma opção inválida
    em um menu interativo.

    Args:
        n1 (int): Valor mínimo permitido.
        n2 (int): Valor máximo permitido.

    Returns:
        str: Mensagem formatada com timestamp e aviso.

    Example:
        >>> print(notify_options_warning(1, 4))
        [16:05:23.123] [WARNING]: Por gentileza, escolha uma opção válida (1 a 4)
    """

    #Código da função
    clear()
    return f"{show_moment()} {color_to_yellow('[WARNING]')}: Por gentileza, escolha uma opção válida ({n1} a {n2})\n"



def notify_options_warning_submenu() -> str:
    #Documentação da função
    """
    Retorna uma mensagem de aviso quando o usuário escolhe uma opção inválida em um submenu interativo.

    Returns:
        str: Mensagem formatada com timestamp e aviso.

    Example:
        >>> print(notify_options_warning(s, n))
        [16:05:23.123] [WARNING]: Por gentileza, escolha uma opção válida ("s" ou "n")
    """

    #Código da função
    clear()
    return f"{show_moment()} {color_to_yellow('[WARNING]')}: Por gentileza, escolha uma opção válida (s ou n)\n"



def notify_insertion() -> str:
    #Documentação da função
    """
    Retorna uma mensagem indicando que o sistema está se preparando
    para inserir dados no banco.

    Returns:
        str: Mensagem formatada com timestamp e status.

    Example:
        >>> print(notify_insertion())
        [16:05:23.123] [INFO] Preparando para inserir dados...
    """

    #Código da função
    clear()
    return f"{show_moment()} {color_to_green('[INFO]')}: Preparando para inserir dados..."



def notify_selection() -> str:
    #Documentação da função
    """
    Retorna uma mensagem indicando que o sistema está se preparando
    para selecionar dados no banco.

    Returns:
        str: Mensagem formatada com timestamp e status.

    Example:
        >>> print(notify_selection())
        [16:05:23.123] [INFO]: Preparando para selecionar os dados...
    """

    #Código da função
    clear()
    return f"{show_moment()} {color_to_green('[INFO]')}: Preparando para selecionar os dados..."



def notify_change() -> str:
    #Documentação da função
    """
    Retorna uma mensagem indicando que o sistema está se preparando
    para alterar dados no banco.

    Returns:
        str: Mensagem formatada com timestamp e status.

    Example:
        >>> print(notify_change())
        [16:05:23.123] [INFO]: Preparando para alterar os dados...
    """

    #Código da função
    clear()
    return f"{show_moment()} {color_to_green('[INFO]')}: Preparando para alterar os dados..."



def notify_deletion() -> str:
    #Documentação da função
    """
    Retorna uma mensagem indicando que o sistema está se preparando
    para deletar dados no banco.

    Returns:
        str: Mensagem formatada com timestamp e status.

    Example:
        >>> print(notify_deletion())
        [16:05:23.123] [INFO]: Preparando para deletar os dados...
    """

    #Código da função
    clear()
    return f"{show_moment()} {color_to_green('[INFO]')}: Preparando para deletar os dados..."



def notify_barcode_error_number() -> str:
    #Documentação da função
    """
    Retorna uma mensagem de erro quando o código de barras informado
    não contém apenas números inteiros.

    Returns:
        str: Mensagem formatada com timestamp e descrição do erro.

    Example:
        >>> print(notify_barcode_error_number())
        [16:05:23.123] [ERROR]: Valor inválido
        - Só é possível selecionar pelo código de barras, inserindo números inteiros
        Por gentileza, tente novamente
    """

    #Código da função
    clear()
    msg = (
        "- Só é possivel selecionar pelo código de barras, inserindo números inteiros\n"
        "Por gentileza, tente novamente\n\n"
    )
    return f"{show_moment()} {color_to_red('[ERROR]')}: Valor inválido\n{msg}"



def notify_barcode_error_len(barcode: str) -> str:
    #Documentação da função
    """
    Retorna uma mensagem de erro quando o código de barras informado
    não possui o tamanho esperado (13 dígitos).

    Args:
        barcode (str): Código de barras informado pelo usuário.

    Returns:
        str: Mensagem formatada com timestamp e descrição do erro.

    Example:
        >>> print(notify_barcode_error_len("12345"))
        [16:05:23.123] [ERROR]: Valor inválido
        - O código de barras precisa ter 13 dígitos
        - Você digitou 5
        Por gentileza, tente novamente
    """

    #Código da função
    clear()
    msg = (
        "- O código de barras precisa ter 13 digitos\n"
        f"- Você digitou {len(barcode)}\n"
        "Por gentileza, tente novamente\n\n"
    )
    return f"{show_moment()} {color_to_red('[ERROR]')}: Valor inválido\n{msg}"



def notify_field_requirement() -> str:
    #Documentação da função
    """
    Retorna uma mensagem de erro quando um campo obrigatório não é preenchido.

    Returns:
        str: Mensagem formatada com timestamp e descrição do erro.

    Example:
        >>> print(notify_field_requirement())
        [16:05:23.123] [ERROR]: Valor inválido
        - Esse campo é obrigatório
        Por gentileza, tente novamente
    """

    #Código da função
    clear()
    msg = (
        "- Esse campo é obrigatório\n"
        "Por gentileza, tente novamente\n\n"
    )
    return f"{show_moment()} {color_to_red('[ERROR]')}: Valor inválido\n{msg}"



def notify_price_error() -> str:
    #Documentação da função
    """
    Retorna uma mensagem de erro quando o preço informado não é um número
    flutuante válido (float).

    Returns:
        str: Mensagem formatada com timestamp e descrição do erro.

    Example:
        >>> print(notify_float_error("abc"))
        [16:05:23.123] [ERROR]: Valor inválido
        - Só é permitido números no campo de preço
        Por gentileza, tente novamente
    """

    #Código da função
    clear()
    msg = (
        "- Só é permitido números no campo de preço\n"
        "Por gentileza, tente novamente\n\n"
    )
    return f"{show_moment()} {color_to_red('[ERROR]')}: Valor inválido\n{msg}"



def notify_stock_error() -> str:
    #Documentação da função
    """
    Retorna uma mensagem de erro quando o valor informado para o campo
    de estoque não é um número inteiro válido.

    Returns:
        str: Mensagem formatada com timestamp e descrição do erro.

    Example:
        >>> print(notify_stock_error())
        [16:05:23.123] [ERROR]: Valor inválido
        - Só é permitido números inteiros no campo de estoque
        Por gentileza, tente novamente
    """

    #Código da função
    clear()
    msg = (
        "- Só é permitido números inteiros no campo de estoque\n"
        "Por gentileza, tente novamente\n\n"
    )
    return f"{show_moment()} {color_to_red('[ERROR]')}: Valor inválido\n{msg}"



def notify_barcode_error_not_numeric() -> str:
    #Documentação da função
    """
    Retorna uma mensagem de erro quando o código de barras informado
    contém caracteres não numéricos.

    Returns:
        str: Mensagem formatada com timestamp e descrição do erro.

    Example:
        >>> print(notify_barcode_error_not_numeric())
        [16:05:23.123] [ERROR]: Valor inválido
        - Só é permitido números inteiros no campo de código de barras
        Por gentileza, tente novamente
    """

    #Código da função
    clear()
    msg = (
        "- Só é permitido números inteiros no campo de código de barras\n"
        "Por gentileza, tente novamente\n\n"
    )
    return f"{show_moment()} {color_to_red('[ERROR]')}: Valor inválido\n{msg}"

def notify_character_error() -> str:
    #Documentação da função
    """
    Retorna uma mensagem de erro quando conter carcteres especiais no nome informado

    Returns:
        str: Mensagem formatada com timestamp e descrição do erro.

    Example:
        >>> print(notify_character_error())
        [16:05:23.123] [ERROR]: Valor inválido
        - Não é permitido caracteres especiais no campo de nome
        Por gentileza, tente novamente
    """

    #Código da função
    clear()
    msg = (
        "- Não é permitido caracteres especiais no campo de nome\n"
        "Por gentileza, tente novamente\n\n"
    )
    return f"{show_moment()} {color_to_red('[ERROR]')}: Valor inválido\n{msg}"

def notify_returning_menu() -> str:
    #Documentação da função
    """
    Retorna uma mensagem indicando que o sistema está retornando ao menu principal.

    Returns:
        str: Mensagem formatada com timestamp e status.

    Example:
        >>> print(notify_insertion())
        [16:05:23.123] [INFO] Retornando ao menu principal...
    """

    #Código da função
    clear()
    return f"{show_moment()} {color_to_green('[INFO]')}: Retornando ao menu principal...\n"