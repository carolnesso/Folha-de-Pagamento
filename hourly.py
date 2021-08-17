from employee import *

class Hourly(Employee):

    def __init__(self, name, address, type, payment_day, way_of_receiving, syndicate, id, hourly_wage, timecard):
        self.__hourly_wage = hourly_wage
        self.__timecard = timecard
        super().__init__(name, address, type, payment_day, way_of_receiving, syndicate, id)

    @property
    def hourly_wage(self):
        return self.__hourly_wage

    @property
    def timecard(self):
        return self.__timecard


    @hourly_wage.setter
    def hourly_wage(self, valid_hourly_wage):
        while type(valid_hourly_wage) != float:
            valid_hourly_wage = float(input('Insert a valid hourly wage, without letters.\n'))

        self.__hourly_wage = valid_hourly_wage

    @timecard.setter
    def timecard(self, valid_timecard):
        while type(valid_timecard) != float:
            valid_timecard = float(input('Insert a valid timecard, without letters.\n'))
            
        self.__timecard = valid_timecard