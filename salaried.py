from employee import *

class Salaried(Employee):

    def __init__(self, name, address, type, payment_day, way_of_receiving, syndicate, id, monthly_salary):
        self.__monthly_salary = monthly_salary

        super().__init__(name, address, type, payment_day, way_of_receiving, syndicate, id)