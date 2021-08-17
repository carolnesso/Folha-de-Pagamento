#from os import name
from employee import *
from hourly import *
from salaried import *
from commissioned import *

@property
def name(self):
    return self.__name

def address(self):
    return self.__address

def type(self):
    return self.__type

def last_payment_day(self):
    return self.__lasty_payment_day

def way_of_receiving(self):
    return self.__way_of_receiving

def syndicate(self):
    return self.__syndicate

def id(self):
    return self.__id


@name.setter
def name(self, valid_name):
    while valid_name != str:
        valid_name = input('Insert a valid name, without numbers.\n')
    
    self.__name = valid_name

@address.setter
def address(self, valid_address):
    while valid_address != str:
        valid_address = input('Insert a valid address:\n')

    self.__address = valid_address

@type.setter
def type(self, valided_type):
    self.__type = valided_type

@last_payment_day.setter
def last_payment_day(self, last_updated_date):
    self.__last_payment_day = last_updated_date


@way_of_receiving.setter
def way_of_receving(self, valid_way_of_receiving):
    while valid_way_of_receiving != str:
        valid_way_of_receiving = input('Please, insert a valid way of receiving, like Depósito em conta; Cheque em mãos; Envio do cheque pelos correios.\n')
    
    self.__way_of_receiving = valid_way_of_receiving

@syndicate.setter
def syndicate(self, boolean):
    self.__syndicate = boolean

@id.setter
def id(self, i):
    #i will be the count of the list, in this case, where we find the employee
    self.__id = i
    









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
