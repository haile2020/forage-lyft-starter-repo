from battery import Battery
from datetime import datetime

class SplindlerBattery(Battery):
  def __init__(self, last_service_date, current_date):
    super().__init__(last_service_date)
    self.last_service_date =last_service_date
    self.current_date =current_date
  
  def needs_service(self):
    isServiceable = datetime.year - self.last_service_date  >= 2
    if isServiceable:
      return True
    else:
      return False
  
