#from os import name
from employee import *
from hourly import *
from salaried import *
from commissioned import *

"""class Employee:
    def __init__(self, name, address, type, payment_day, way_of_receiving, syndicate, id):
        self.__name = name
        self.__address = address
        self.__type = type
        self.__payment_day = payment_day
        self.__way_of_receiving = way_of_receiving
        self.__syndicate = syndicate
        self.__id = id
"""


#hourly wage == taxa por hora
"""class Hourly(Employee):

    def __init__(self, name, address, type, payment_day, way_of_receiving, syndicate, id, hourly_wage, timecard):
        self.__hourly_wage = hourly_wage
        self.__timecard = timecard
        
        super().__init__(name, address, type, payment_day, way_of_receiving, syndicate, id)"""

def set_Hourly_Employee(self, new_name, new_address, last_payment_day, new_way_of_receiving, syndicate_status, employee_id, new_hourly_wage, timecard):
    self.__name = new_name
    self.__address = new_address
    self.__payment_day = last_payment_day
    self.__way_of_receiving = new_way_of_receiving
    self.__syndicate = syndicate_status
    self.__id = employee_id
    self.__hourly_wage = new_hourly_wage
    self.__timecard = timecard

        #return self.__id, self.__name, self.__address, self.__payment_day, self.__way_of_receiving, self.__syndicate
            


"""class Salaried(Employee):

    def __init__(self, name, address, type, payment_day, way_of_receiving, syndicate, id, monthly_salary):
        self.__monthly_salary = monthly_salary

        super().__init__(name, address, type, payment_day, way_of_receiving, syndicate, id)
"""

def set_Salaried_Employee(self, new_name, new_address, last_payment_day, new_way_of_receiving, syndicate_status, employee_id):
    self.__name = new_name
    self.__address = new_address
    self.__payment_day = last_payment_day
    self.__way_of_receiving = new_way_of_receiving
    self.__syndicate = syndicate_status
    self.__id = employee_id

    return self.__id, self.__name, self.__address, self.__payment_day, self.__way_of_receiving, self.__syndicate


"""class Commissioned(Salaried):

    def __init__(self, name, address, type, payment_day, way_of_receiving, syndicate, id, monthly_salary, commission_fee):
        self.__commission_fee = commission_fee

        super().__init__(name, address, type, payment_day, way_of_receiving, syndicate, id, monthly_salary)
"""

def set_Commissioned_Employee(self, new_name, new_address, last_payment_day, new_way_of_receiving, syndicate_status, employee_id):
    self.__name = new_name
    self.__address = new_address
    self.__payment_day = last_payment_day
    self.__way_of_receiving = new_way_of_receiving
    self.__syndicate = syndicate_status
    self.__id = employee_id


    return self.__id, self.__name, self.__address, self.__payment_day, self.__way_of_receiving, self.__syndicate

#Getter
"""@property
def name(self):
    return self.__name"""


#Setter
"""@name.setter
def name(self, real_name):
    if isinstance(real_name, str):
        real_name = float(real_name.replace())
    self.__name = real_name"""
