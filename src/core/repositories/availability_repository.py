from abc import ABC, abstractmethod


class AvailabilityRepository(ABC):

    @abstractmethod
    def get_data(self):
        pass
