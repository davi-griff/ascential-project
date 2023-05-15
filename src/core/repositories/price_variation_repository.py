from abc import ABC, abstractmethod


class PriceVariationRepository(ABC):

    @abstractmethod
    def get_data(self):
        pass
