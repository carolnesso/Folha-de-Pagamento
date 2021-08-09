#from tkinter.constants import NONE
from caste import *
import collections

employee_list = collections.deque()

def add_Employee():

    name = input('Enter a name:\n')
    address = input('Now, enter an address:\n')
    type = input('Enter the employment contract type:\n')
    payment_day = None
    way_of_receiving = input('Enter payment method:\n')
    syndicate = input('Do you belong to the union?\n')

    id = employee_list.__len__()

    if syndicate == 'Sim' or syndicate == 'sim':
        syndicate = True

    else: syndicate = False

    print('Seu numero de empregado será:\n',id)

    if type == 'Horista' or type == 'horista':
        employee = Hourly(name, address, type, payment_day, way_of_receiving, syndicate, id, 0, -10)

    if type == 'Assalariado' or type == 'assalariado':
        employee = Salaried(name, address, type, payment_day, way_of_receiving, syndicate, id, 0)

    if type == 'Comissionado' or type == 'comissionado':
        employee = Commissioned(name, address, type, payment_day, way_of_receiving, syndicate, id, 0)

    employee_list.append(employee)

