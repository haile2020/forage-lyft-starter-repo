from car import Car

class CarFactory(Car):
  def __init__(self,current_date, last_service_date, current_mileage, last_service_mileage):
    super.__init__(last_service_date)
    self.current_date = current_date
    self.last_service_date = last_service_date
    self.current_mileage =current_mileage
    self.last_service_mileage = last_service_mileage

  def create_colliope(self):
    colliope = CarFactory(self.current_date, self.last_service_date,self.current_mileage,self.last_service_mileage)
    return colliope
  
  def create_glissade(self):
    glissade = CarFactory(self.current_date, self.last_service_date,self.current_mileage,self.last_service_mileage)
    return glissade
  
  def create_palindrome(self):
    palindrome = CarFactory(self.current_date, self.last_service_date,self.current_mileage,self.last_service_mileage)
    return palindrome
  
  def create_rorschach(self):
    rorschach = CarFactory(self.current_date, self.last_service_date,self.current_mileage,self.last_service_mileage)
    return rorschach
  
  def create_thovex(self):
    thovex = CarFactory(self.current_date, self.last_service_date,self.current_mileage,self.last_service_mileage)
    return thovex