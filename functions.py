from tkinter.constants import NONE
from collections import *
#from caste import *
from teste import *

def Manegers_Menu():

    action = ""
            
    while action != "0":
            print('\nHello Manager !\nWhich action you wanna do?\n\n1 - Edit employee attributes\n2 - Timecard\n3 - Syndicate\n4 - Sales\n5 - Undo/Redo\n6 - Show employess\n0 - Exit')
            action = input('\n')

            if action == '1': #edit_employee_atributs()
                pass

            if action == '2': #timecard
                pass

            if action == '3': #syndicate
                pass

            if action == '4': #sales
                pass

            if action == '5': #undo_redo
                pass

            if action == '6': Print_Employees(employee_list)


employee_list = []

def Add_Employee():

    name = input('Enter a name:\n')
    address = input('Now, enter an address:\n')
    last_payment_day = None
    way_of_receiving = input('Enter payment method:\n')
    syndicate = input('Do you belong to the union?\n')
    type = input('Enter the employment contract type:\n')

    if syndicate == 'Sim' or syndicate == 'sim': syndicate = True

    else: syndicate = False

    employee = ''
    id = employee_list.__len__()
    

    if type == 'Horista' or type == 'horista': 
        hourly_wage = input('Please enter the hourly rate of work:\n')
        employee = Hourly(name, address, type, last_payment_day, way_of_receiving, syndicate, id, hourly_wage, 0)

    elif type == 'Assalariado' or type == 'assalariado':
        monthly_salary = input('Please, enter the salary:\n')
        employee = Salaried(name, address, type, last_payment_day, way_of_receiving, syndicate, id, monthly_salary)

    elif type == 'Comissionado' or type == 'comissionado':
        monthly_salary = input('Please, enter the salary:\n')
        commission_fee = input('Please, enter the sales commission rate:\n')
        employee = Commissioned(name, address, type, last_payment_day, way_of_receiving, syndicate, id, monthly_salary, commission_fee)

    else: print('Please, insert a valid type, like, Horista, Assalariado or Comissionado.\n'), Add_Employee()

    print('Your employees ID will be:', id,'\n')

    employee_list.append(employee)


    """name = input('Enter a name:\n')
    address = input('Now, enter an address:\n')
    payment_day = None
    way_of_receiving = input('Enter payment method:\n')
    syndicate = input('Do you belong to the union?\n')

    id = employee_list.__len__()

    if syndicate == 'Sim' or syndicate == 'sim': syndicate = True

    else: syndicate = False

    print('Your employees ID will be:', id,'\n')
    employee = ''

    if type == 'Horista' or type == 'horista':
        hourly_wage = input('Now, enter the work/hour value:')
        employee = Hourly(name, address, type, payment_day, way_of_receiving, syndicate, id, hourly_wage, -10)

    if type == 'Assalariado' or type == 'assalariado':
        monthly_salary = input('Now, enter the salary amount:')
        employee = Salaried(name, address, type, payment_day, way_of_receiving, syndicate, id, monthly_salary)

    if type == 'Comissionado' or type == 'comissionado':
        monthly_salary = input('Now, enter the salary amount:')
        commission_fee = input('Now, enter the commission fee value:')
        employee = Commissioned(name, address, type, payment_day, way_of_receiving, syndicate, id, monthly_salary, commission_fee)
"""
    #employee_list.append(employee)
    #Write_File_Employees()


def Remove_Employee():

    id = input('Please, enter the ID employee:\n')
    employee_list.pop(int(id))

def Edit_employee_atributs():

    id = input('Please, enter the ID employee:\n')
    attibute = input('Wich attribute do you wanna change?\n')

    if attibute == 'Nome' or attibute == 'nome': employee_list[id].name = input('Enter the new name:\n')


def Print_Employees(employee_list):

    for i in  range(len(employee_list)):

        print("Name =",employee_list[i].name)
        print("Address =",employee_list[i].address)
        print("Employment contract type =",employee_list[i].type)
        print("Employee's ID =",employee_list[i].id)
        print("Syndicates =",employee_list[i].syndicate)
        print("Last payment day =",employee_list[i].payment_day)

        if employee_list[i].type =='Horista' or employee_list[i].type == 'horista':
            print("hour_price=",employee_list[i].hourly_wage)
            print("timecard=",employee_list[i].timecard,'\n')

        if employee_list[i].type =='Comissionado' or employee_list[i].type =='comissionado':
            print("salary=",employee_list[i].monthly_salary)
            print("comision=",employee_list[i].commission_fee, '\n')

        if employee_list[i].type  == 'Assalariado' or employee_list[i].type =='assalariado':
            print('Salary= ', employee_list[i].monthly_salary, '\n')


def Write_File_Employees():
    
     with open('Employees_List.txt', 'a') as file:
        for i in range(len(employee_list)):
            file.write("Employee's ID:" + str(employee_list[i].id) + '\n')
            file.write('Name:' + str(employee_list[i].name) + '\n')
            file.write('Address:' + str(employee_list[i].address) + '\n')
            file.write('Employment contract type:' + str(employee_list[i].type) + '\n')
            file.write('Syndicate:' + str(employee_list[i].syndicate) + '\n')
            file.write('Last day payment:' + str(employee_list[i].payment_day) + '\n')

            if employee_list[i].type =='Horista' or employee_list[i].type == 'horista':
                file.write('Hour Price:' + str(employee_list[i].hourly_wage) + '\n')
                file.write('Timecard:' + str(employee_list[i].timecard) + '\n')
                file.write('\n')

            if employee_list[i].type =='Comissionado' or employee_list[i].type =='comissionado':
                file.write('Monthly Salary:' + str(employee_list[i].monthly_salary) + '\n')
                file.write('Commission:' + str(employee_list[i].commission_fee) + '\n')
                file.write('\n')

            if employee_list[i].type  == 'Assalariado' or employee_list[i].type =='assalariado':
                file.write('Monthly Salary:' + str(employee_list[i].monthly_salary) + '\n')
                file.write('\n')



