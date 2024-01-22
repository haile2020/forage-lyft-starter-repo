from tire.tire import Tire


class OctopprimeTire(Tire):
  def __init__(self, wearSensors):
    super().__init__(wearSensors)
    self.wearSensors = wearSensors

  def needs_service(self):
    sum = 0
    for val in self.wearSensors:
      sum += val
      if sum >= 3:
        return True
      else:
        return False