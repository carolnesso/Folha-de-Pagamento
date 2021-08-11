from employee import *

class Hourly(Employee):

    def __init__(self, name, address, type, payment_day, way_of_receiving, syndicate, id, hourly_wage, timecard):
        self.__hourly_wage = hourly_wage
        self.__timecard = timecard
        
        super().__init__(name, address, type, payment_day, way_of_receiving, syndicate, id)