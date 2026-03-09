#Importações de outro módulo
import string
from log_message import notify_barcode_error_len, notify_field_requirement, notify_price_error, notify_stock_error,notify_barcode_error_not_numeric, notify_value_error, notify_character_error, notify_returning_menu, notify_options_warning_submenu

#Documentação do módulo
"""
validation.py
--------------

Descrição:
    Módulo responsável por validar entradas fornecidas pelo usuário em menus
    e formulários do sistema. Ele garante que os dados sejam preenchidos de
    forma correta e consistente antes de serem processados.

Principais funcionalidades:
    - validate_option_number(): valida opções numéricas em menus.
    - validate_barcode(): valida códigos de barras (não vazio, numérico e com 13 dígitos).
    - validate_name(): valida campos de nome (não vazio).
    - validate_price(): valida preços (não vazio e número flutuante).
    - validate_stock(): valida estoque (não vazio e número inteiro).

Uso:
    Importado em módulos de interação com o usuário e operações de banco de dados
    para assegurar que os valores digitados sejam válidos, exibindo mensagens
    de erro apropriadas via `log_message`.
"""



def validate_option_number(value:str):
    #Documentação da função
    """
    Valida a opção numérica informada pelo usuário em menus.

    Regras de validação:
    - Tenta converter o valor para inteiro.
    - Se não for possível, exibe `notify_value_error` e lança `ValueError`.

    Args:
        value (str): Valor digitado pelo usuário.

    Returns:
        int: Número inteiro válido.

    Raises:
        ValueError: Se o valor não puder ser convertido para inteiro.

    Example:
        >>> validate_option_number("3")
        3

        >>> validate_option_number("abc")
        [ERROR]: Valor inválido
        - É permitido somente a entrada de números nesse campo
        Por gentileza, tente novamente
        ValueError
    """

    #Código da função
    try:
        return int(value)
    except ValueError:
        print(f"{notify_value_error()}")
        raise ValueError
    

def validate_option_letter(value:str):
    #Documentação da função
    """
    Valida a opção informada pelo usuário em submenus.

    Regras de validação:
    - Verifica se o valor inserido foi foi sim ou não
    - Se não for nenhum dos dois exibe `notify_options_warning_submenu` e lança `ValueError`.

    Args:
        value (str): Valor digitado pelo usuário.

    Returns:
        str: Valor válido.

    Raises:
        ValueError: Se o valor não for sim ou não.
        Exception: Se o usuário não quiser continuar com a execução

    Example:
        >>> validate_option_letter("s")
        "s"

        >>> validate_option_letter("n")
        [16:05:23.123] [INFO] Retornando ao menu principal...
        Exception

        >>> validate_option_letter("abc")
        [16:05:23.123] [WARNING]: Por gentileza, escolha uma opção válida ("s" ou "n")
        ValueError
    """

    #Código da função
    if value.lower() == "s":
        return value
    if value.lower() == "n":
        print(f"{notify_returning_menu()}")
        raise Exception
    print(f"{notify_options_warning_submenu()}")
    raise ValueError
    


def validate_barcode(barcode: str):
    #Documentação da função
    """
    Valida o código de barras informado pelo usuário.

    Regras de validação:
    - Não pode ser vazio → dispara `notify_field_requirement`.
    - Deve conter apenas números → dispara `notify_barcode_error_not_numeric`.
    - Deve ter exatamente 13 dígitos → dispara `notify_barcode_error_len`.

    Args:
        barcode (str): Código de barras digitado.

    Returns:
        str: O código de barras válido.

    Raises:
        ValueError: Se alguma das regras acima não for atendida.

    Example:
        >>> validate_barcode("7891234567890")
        '7891234567890'

        >>> validate_barcode("")
        [ERROR]: Valor inválido
        - Esse campo é obrigatório
        Por gentileza, tente novamente
        ValueError

        >>> validate_barcode("ABC123")
        [ERROR]: Valor inválido
        - Só é permitido números inteiros no campo de código de barras
        Por gentileza, tente novamente
        ValueError

        >>> validate_barcode("12345")
        [ERROR]: Valor inválido
        - O código de barras precisa ter 13 dígitos
        - Você digitou 5
        Por gentileza, tente novamente
        ValueError
    """

    #Código da função
    if not barcode:
        print(F"{notify_field_requirement()}")
        raise ValueError
    try:
        _int_barcode = int(barcode)
    except ValueError:
        print(f"{notify_barcode_error_not_numeric()}")
        raise ValueError
    if len(barcode) != 13:
        print(f"{notify_barcode_error_len(barcode)}")
        raise ValueError
    return barcode
    


def validate_name(input_name: str):
    #Documentação da função
    """
    Valida o nome informado pelo usuário.

    Regras de validação:
    - Não pode ser vazio → dispara `notify_field_requirement`.
    - Não pode conter caracteres especiais → dispara `notify_character_error`.

    Args:
        input_name (str): Nome digitado pelo usuário.

    Returns:
        str: O nome válido informado.

    Raises:
        ValueError: Se alguma regra acima não for 
        atendida.

    Example:
        >>> validate_name("Coca Cola 2L")
        'Coca Cola 2L'

        >>> validate_name("")
        [ERROR]: Valor inválido
        - Esse campo é obrigatório
        Por gentileza, tente novamente
        ValueError
        
        >>> validate_name("produto#$%")
        [ERROR]: Valor inválido
        - Não é permitido caracteres especiais no campo de nome
        Por gentileza, tente novamente
        ValueError
    """

    #Código da função
    if not input_name:
        print(f"{notify_field_requirement()}")
        raise ValueError
    if any(char in string.punctuation for char in input_name):
        print(f"{notify_character_error()}")
        raise ValueError
    return input_name
    


def validate_price(input_price : str):
    #Documentação da função
    """
    Valida o preço informado pelo usuário.

    Regras de validação:
    - Não pode ser vazio → dispara `notify_field_requirement`.
    - Deve ser um número int ou flutuante válido → dispara `notify_price_error`.

    Args:
        input_price (str): Valor digitado no campo de preço.

    Returns:
        float: Preço convertido para número flutuante.

    Raises:
        ValueError: Se o campo estiver vazio ou não puder ser convertido para float.

    Example:
        >>> validate_price("19.99")
        19.99

        >>> validate_price("")
        [ERROR]: Valor inválido
        - Esse campo é obrigatório
        Por gentileza, tente novamente
        ValueError

        >>> validate_price("abc")
        [ERROR]: Valor inválido
        - Só é permitido números no campo de preço
        Por gentileza, tente novamente
        ValueError
    """

    #Código da função
    if not input_price:
        print(F"{notify_field_requirement()}")
        raise ValueError
    try:
        return float(input_price)
    except ValueError:
        print(f"{notify_price_error()}")
        raise ValueError
    


def validate_stock(input_stock: str):
    #Documentação da função
    """
    Valida a quantidade em estoque informada pelo usuário.

    Regras de validação:
    - Não pode ser vazio → dispara `notify_field_requirement`.
    - Deve ser um número inteiro válido → dispara `notify_stock_error`.

    Args:
        input_stock (str): Valor digitado no campo de estoque.

    Returns:
        int: Quantidade de estoque convertida para inteiro.

    Raises:
        ValueError: Se o campo estiver vazio ou não puder ser convertido para inteiro.

    Example:
        >>> validate_stock("10")
        10

        >>> validate_stock("")
        [ERROR]: Valor inválido
        - Esse campo é obrigatório
        Por gentileza, tente novamente
        ValueError

        >>> validate_stock("abc")
        [ERROR]: Valor inválido
        - Só é permitido números inteiros no campo de estoque
        Por gentileza, tente novamente
        ValueError
    """

    #Código da função
    if not input_stock:
        print(f"{notify_field_requirement()}")
        raise ValueError
    try:
        return int(input_stock)
    except ValueError:
        print(f"{notify_stock_error()}")
        raise ValueError