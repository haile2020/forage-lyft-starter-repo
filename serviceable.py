class Serviceable():
  def __init__(self, isServiceable):
    self.isServiceable = isServiceable

  def needs_service(self):
    return self.isServiceable