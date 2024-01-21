from abc import ABC, abstractmethod
from serviceable import Serviceable

class Car(ABC, Serviceable):
    def __init__(self, last_service_date, engine, battery):
        super.__init__
        self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self, isServiceable):
        return self.isServiceable