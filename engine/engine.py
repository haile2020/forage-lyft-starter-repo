from car import Car

class Engine(Car):
  def __init__(self, isServiceable):
    super.__init__()
    self.isServiceable = isServiceable

  def needs_service(self):
    return self.isServiceable
    