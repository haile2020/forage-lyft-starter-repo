from abc import ABC

class Tire(ABC):
  def __init__(self, wearSensors):
    super().__init__()
    self.wearSensors = wearSensors
  def needs_service(self):
    pass