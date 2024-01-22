from tire.tire import Tire

class CarriganTire(Tire):
  def __init__(self, wearSensors):
    super().__init__(wearSensors)
    self.wearSensors = wearSensors

  def needs_service(self):
    for val in self.wearSensors:
      if val >= 0.9:
        return True
      else:
        return False