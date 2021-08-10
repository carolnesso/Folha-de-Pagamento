from tkinter.constants import NONE
from caste import *
import collections

def Manegers_Menu():

    action = ""
            
    while action != "0":
            print('\nHello Manager !\nWhich action you wanna do?\n\n1 - Edit employee attributes\n2 - Timecard\n3 - Syndicate\n4 - Sales\n5 - Undo/Redo\n6 - Show employess\n0 - Exit')
            action = input('\n')

            if action == '1':
                #edit_employee_atributs()
                pass

            if action == '2':
                #timecard
                pass

            if action == '3':
                #syndicate
                pass

            if action == '4':
                #sales
                pass

            if action == '5':
                #undo_redo
                pass

            if action == '6':
                Print_Employees(employee_list)


employee_list = []

def Add_Employee():

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

    print('Seu numero de empregado será:', id)

    if type == 'Horista' or type == 'horista':
        hourly_wage = input('Now, enter the work/hour value:')
        employee = Hourly(name, address, type, payment_day, way_of_receiving, syndicate, id, hourly_wage, -10)

    if type == 'Assalariado' or type == 'assalariado':
        monthly_salary = input('Now, enter the salary amount:')
        employee = Salaried(name, address, type, payment_day, way_of_receiving, syndicate, id, monthly_salary)

    if type == 'Comissionado' or type == 'comissionado':
        commission_fee = input('Now, enter the commission fee value:')
        employee = Commissioned(name, address, type, payment_day, way_of_receiving, syndicate, id, commission_fee)

    employee_list.append(employee)

def Print_Employees(employee_list):

    for i in  range(len(employee_list)):

        print("Name =",employee_list[i].name)
        print("Address =",employee_list[i].address)
        print("Employment contract type =",employee_list[i].type)
        print("Employee's ID =",employee_list[i].id)
        print("Syndicates =",employee_list[i].syndicate)
        print("Last day payment =",employee_list[i].payment_day)

        if(employee_list[i].type =='Horista' or employee_list[i].type == 'horista'):
            print("hour_price=",employee_list[i].hourly_wage)
            print("timecard=",employee_list[i].timecard,'\n')

        if(employee_list[i].type =='Comissionado' or employee_list[i].type =='comissionado'):
            print("salary=",employee_list[i].salary)
            print("comision=",employee_list[i].commision, '\n')

        if (employee_list[i].type  == 'Assalariado' or employee_list[i].type =='assalariado'):
            print(employee_list[i].salary, '\n')


def Remove_Employee():

    id = input('Please, enter the ID employee:\n')
    employee_list.pop(int(id))

def Edit_employee_atributs():

    id = input('Please, enter the ID employee:\n')
    