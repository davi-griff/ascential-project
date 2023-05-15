import os
from functools import lru_cache
import dotenv


class GlobalConfigs:
    """
    Define as variaveis globais de configurações

    FILES_PATH: Local onde estão armazenados os dados. Padrão: no diretorio raiz do projeto na pasta data.
    ENCODING: Codificação dos arquivos json. Padrão: latin
    """

    def __init__(self):

        dotenv.load_dotenv()
        self.FILES_PATH = os.getenv('FILES_PATH', os.path.join(os.getcwd(), 'data'))
        self.ENCODING = os.getenv('ENCODING', 'latin')


@lru_cache
def get_configs():
    """Função de ajuda para alocar configs na memoria lru"""
    return GlobalConfigs()