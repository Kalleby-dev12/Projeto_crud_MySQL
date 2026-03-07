#Importando outros módulos
import os
import subprocess
from datetime import datetime

#Documentação do módulo
"""
utils.py
--------

Descrição:
    Módulo utilitário responsável por fornecer funções auxiliares para
    formatação de logs e interação com o terminal. Ele centraliza recursos
    usados por outros módulos do sistema.

Principais funcionalidades:
    - show_moment(): gera o horário atual formatado com milissegundos.
    - color_to_*(): aplica cores ANSI (verde, vermelho, amarelo, ciano) ao texto.
    - _reset_color(): restaura a cor padrão do terminal.
    - clear(): limpa o terminal de forma compatível com Windows, Linux e Mac.

Uso:
    Importado por módulos de log e validação para exibir mensagens
    com timestamp e cores, além de manter o terminal limpo e organizado.
"""


def show_moment() -> str:
    #Documentação da função
    """
    Retorna o horário atual da máquina no formato HH:MM:SS.mmm.

    Returns:
        str: Horário atual com precisão em milissegundos.

    Example:
        >>> show_moment()
        '[15:58:23.123]'
    """

    #Código da função
    moment = datetime.now().strftime("[%H:%M:%S.%f")[:-3] + "]"
    return f"{color_to_cyan(moment)} ->"



def _reset_color() -> str:
    #Documentação da função
    """
    Retorna o código ANSI para resetar a cor do texto no terminal.

    Returns:
        str: Código ANSI que restaura a cor padrão do terminal.

    Example:
        >>> print(_reset_color())
        '\033[0m'
    """

    #Código da função
    return "\033[0m"



def color_to_green (text:str) -> str:
    #Documentação da função
    """
    Pinta o texto recebido de verde utilizando códigos ANSI.

    Args:
        text (str): Texto a ser colorido.

    Returns:
        str: Texto formatado em verde.

    Example:
        >>> print(color_to_green("[INFO]"))
        [INFO]  # exibido em verde no terminal
    """
    #Código da função
    GREEN = "\033[32m"
    return f"{GREEN}{text}{_reset_color()}"



def color_to_red (text:str) -> str:
    #Documentação da função
    """
    Pinta o texto recebido de vermelho utilizando códigos ANSI.

    Args:
        text (str): Texto a ser colorido.

    Returns:
        str: Texto formatado em vermelho.

    Example:
        >>> print(color_to_red("[ERROR]"))
        [ERROR]  # exibido em vermelho no terminal
    """
    #Código da função
    RED = "\033[31m"
    return f"{RED}{text}{_reset_color()}"



def color_to_yellow (text:str) -> str:
    #Documentação da função
    """
    Pinta o texto recebido de amarelo utilizando códigos ANSI.

    Args:
        text (str): Texto a ser colorido.

    Returns:
        str: Texto formatado em amarelo.

    Example:
        >>> print(color_to_yellow("[WARNING]"))
        [WARNING]  # exibido em amarelo no terminal
    """

    #Código da função
    YELLOW = "\033[33m"
    return f"{YELLOW}{text}{_reset_color()}"

def color_to_cyan (text:str) -> str:
    #Documentação da função
    """
    Pinta o texto recebido de ciano utilizando códigos ANSI.

    Args:
        text (str): Texto a ser colorido.

    Returns:
        str: Texto formatado em ciano.

    Example:
        >>> print(color_to_blue("[08:40:21.325]"))
        [08:40:21.325]  # exibido em ciano no terminal
    """

    #Código da função
    CYAN = "\033[36m"
    return f"{CYAN}{text}{_reset_color()}"



def clear() -> None:
    #Documentação da função
    """
    Limpa o terminal, adaptando o comando conforme o sistema operacional.

    - Windows: usa 'cls'
    - Linux/Mac: usa 'clear'

    Returns:
        None: A função não retorna nada, só limpa o terminal

    Example:
        >>> clear()
        # Terminal é limpo
    """

    #Código da função
    comand = "cls" if os.name == "nt" else "clear" 
    subprocess.run(comand, shell=True)

