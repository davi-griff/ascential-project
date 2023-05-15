import os
import json
import logging
from src.core.errors import JSONMalformed


def file_reader(file_path: str, key_lookup: str, columns: list[str], encoding: str = 'latin'):
    with open(os.path.join(file_path), 'r', encoding=encoding, errors='replace') as f:
        jsons = []
        try:
            data = f.read()
            data_json = json.loads(data)
            if key_lookup in data_json['assortment'][0]:
                for unit_data in data_json['assortment']:
                    selected_json = {}
                    for column in columns:
                        selected_json[column] = unit_data[column]
                    jsons.append(selected_json)
            return jsons
        except Exception as e:
            logging.error(f"Erro ao realizar a leitura do arquivo: {file_path}. Erro:{e}")
            raise JSONMalformed(file_path)
