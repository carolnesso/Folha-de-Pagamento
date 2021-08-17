from employee import *

class Salaried(Employee):

    def __init__(self, name, address, type, payment_day, way_of_receiving, syndicate, id, monthly_salary):
        self.__monthly_salary = monthly_salary

        super().__init__(name, address, type, payment_day, way_of_receiving, syndicate, id)


@property
def monthly_salary(self):
    return self.__monthly_salary

@monthly_salary.setter
def monthly_salary(self, valid_salary):
    self.__monthly_salary = valid_salary