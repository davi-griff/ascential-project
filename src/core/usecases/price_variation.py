import datetime
import logging
from src.core.repositories import PriceVariationRepository
import pandas
import json
from src import PROJECT_ROOT_DIR


class PriceVariation:

    def __init__(self, price_variation_repository: PriceVariationRepository):
        self.price_repository = price_variation_repository

    def __extract(self):

        return self.price_repository.get_data()

    def __transform(self):

        raw_df = self.__extract()

        raw_df['absolutePriceVariation'] = raw_df['priceVariation'].apply(lambda x: abs(x))
        df_formated = raw_df[['idRetailerSKU', 'absolutePriceVariation', 'priceVariation']].sort_values(
            by='absolutePriceVariation',
            ascending=False)

        bigger_skus = []
        bigger_variations = []

        for row in df_formated.iterrows():
            sku = row[1].idRetailerSKU
            if sku not in bigger_skus:
                bigger_skus.append(sku)
                bigger_variations.append({
                    "idRetailerSKU": sku,
                    "absolutePriceVariation": row[1].absolutePriceVariation,
                    "priceVariation": row[1].priceVariation
                })

            if len(bigger_variations) == 10:
                price_variation_dataframe = pandas.read_json(json.dumps(bigger_variations), orient='records')
                return price_variation_dataframe

        price_variation_dataframe = pandas.read_json(json.dumps(bigger_variations), orient='records')
        return price_variation_dataframe

    def load(self):

        data = self.__transform()
        logging.info(f"Salvando arquivo com dados processados em {PROJECT_ROOT_DIR}/processed_data/price-variation-{datetime.datetime.now().strftime('%d-%m-%y')}")
        data.to_csv(f"{PROJECT_ROOT_DIR}/processed_data/price-variation-{datetime.datetime.now().strftime('%d-%m-%y')}",
                    index=False, sep='|')
