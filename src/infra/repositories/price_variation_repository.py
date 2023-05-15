import logging
import os
from src.infra.utils import file_reader
from src.core.repositories import PriceVariationRepository
from src.infra.configs import get_configs
from src.core.errors import NoDataFound, JSONMalformed
import pandas
import json

CONFIG = get_configs()


class PriceVariationRepositoryFile(PriceVariationRepository):

    def get_data(self) -> pandas.DataFrame:
        list_of_jsons = []
        if len(os.listdir(CONFIG.FILES_PATH)) > 0:
            for file in os.listdir(CONFIG.FILES_PATH):
                if '.json' in file:
                    try:
                        jsons = file_reader(os.path.join(CONFIG.FILES_PATH, file), 'priceVariation', ['idRetailerSKU','priceVariation'])
                        if len(jsons) > 0:
                            list_of_jsons.extend(jsons)
                    except Exception as e:
                        logging.error(f"Erro ao realizar a leitura do json: {file}. Erro:{e}")
                        raise JSONMalformed(file)

            logging.info(f"Jsons processados em PriceVariationRepository: {len(list_of_jsons)}")
            df = pandas.read_json(json.dumps(list_of_jsons), orient='records')
            return df
        else:
            raise NoDataFound
