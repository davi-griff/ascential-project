import datetime
import logging
from src.core.repositories import AvailabilityRepository
import pandas
import json
from src import PROJECT_ROOT_DIR


class Availability:

    def __init__(self, availability_repository: AvailabilityRepository):
        self.availability_repository = availability_repository

    def __extract(self):

        return self.availability_repository.get_data()

    def __transform(self):

        raw_df = self.__extract()

        raw_df = raw_df.groupby(['idRetailerSKU'], as_index=False)['available'].apply(lambda x: (~x).sum())
        raw_df = raw_df.rename(columns={'available': 'countFalse'})
        raw_df = raw_df.sort_values(by='countFalse', ascending=False)

        bigger_skus = []
        bigger_availability = []
        for row in raw_df.iterrows():
            sku = row[1].idRetailerSKU
            if sku not in bigger_skus:
                bigger_skus.append(sku)
                bigger_availability.append({
                    "idRetailerSKU": int(sku),
                    "countFalse": int(row[1].countFalse)})
            if len(bigger_availability) == 10:
                availability_dataframe = pandas.read_json(json.dumps(bigger_availability), orient='records')
                return availability_dataframe

    def load(self):

        data = self.__transform()
        logging.info(f"Salvando arquivo com dados processados em {PROJECT_ROOT_DIR}/processed_data/availability-{datetime.datetime.now().strftime('%d-%m-%y')}")
        data.to_csv(f"{PROJECT_ROOT_DIR}/processed_data/availability-{datetime.datetime.now().strftime('%d-%m-%y')}",
                    index=False, sep='|')