from salaried import *

class Commissioned(Salaried):

    def __init__(self, name, address, type, payment_day, way_of_receiving, syndicate, id, monthly_salary, commission_fee):
        self.__commission_fee = commission_fee

        super().__init__(name, address, type, payment_day, way_of_receiving, syndicate, id, monthly_salary)