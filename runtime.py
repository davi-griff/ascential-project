import logging
from src.core.usecases import PriceVariation, Availability
from src.infra.repositories import PriceVariationRepositoryFile, AvailabilityRepositoryFile


level = logging.DEBUG
fmt = '[%(levelname)s] - %(module)s - %(asctime)s - %(message)s'
logging.basicConfig(level=level, format=fmt, handlers=[logging.StreamHandler()])


def main():
    "Execução do processo"

    # Extração dos dados de PriceVariation
    logging.info('Iniciando processamento de PriceVariation')
    PriceVariation(PriceVariationRepositoryFile()).load()
    logging.info('PriceVariation finalizado')

    logging.info('Iniciando processamento de Availability')
    Availability(AvailabilityRepositoryFile()).load()
    logging.info('Availability finalizado')



if __name__ == "__main__":
    main()
