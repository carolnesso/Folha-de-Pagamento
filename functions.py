from tkinter.constants import NONE
from imports import *

employee_list = []

def Manegers_Menu():

    action = ""
            
    while action != "0":
            print('\nHello Manager !\nWhich action you wanna do?\n\n1 - Edit employee attributes\n2 - Timecard\n3 - Syndicate\n4 - Sales\n5 - Undo/Redo\n6 - Show employess\n0 - Exit')
            action = input('\n')

            if action == '1': Edit_employee_attributes()

            if action == '2': Timecard()

            if action == '3': #syndicate
                pass

            if action == '4': #sales
                pass

            if action == '5': #undo_redo
                pass

            if action == '6': Print_Employees(employee_list)

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
    
    #while type != 'Horista' or type != 'horista' or type != 'Assalariado' or type != 'assalariado' or type != 'Comissionado' or type != 'comissionado':

    if type == 'Horista' or type == 'horista': 
        hourly_wage = float(input('Please enter the hourly rate of work:\n'))
        employee = Hourly(name, address, type, last_payment_day, way_of_receiving, syndicate, id, hourly_wage, 0)

    elif type == 'Assalariado' or type == 'assalariado':
        monthly_salary = float(input('Please, enter the salary:\n'))
        employee = Salaried(name, address, type, last_payment_day, way_of_receiving, syndicate, id, monthly_salary)

    elif type == 'Comissionado' or type == 'comissionado':
        monthly_salary = float(input('Please, enter the salary:\n'))
        commission_fee = float(input('Please, enter the sales commission rate:\n'))
        employee = Commissioned(name, address, type, last_payment_day, way_of_receiving, syndicate, id, monthly_salary, commission_fee)

    else: print('Please, insert a valid type, like, Horista, Assalariado or Comissionado and star again.\n'), Add_Employee()

    print('Your employees ID will be:', id,'\n')

    print("\nDone!\nBacking to menu...\n")

    employee_list.append(employee)

    Write_File_Employees()

def Remove_Employee():

    id = int(input('Please, enter the ID employee:\n'))
    employee_list.pop(id)

def Timecard():

    id = int(input('Please, enter the ID employee:\n'))
    
    while employee_list[id].type != 'Horista' and employee_list[id].type != 'horista':
        id = int(input('Please, enter a ID number from a hourly employee!\n'))

    employee_list[id].timecard = float(input('Please, enter the number of hours worked:'))

    print("Done, timecard setted!\nBacking to Manager's menu...\n")
    Edit_Employees_File()

def Syndicate():

    id = int(input('Please, enter the ID employee:\n'))

    #while employee_list[id].syndicate != True:
        #id = int(input('Please, enter the ID employee who belongs to the union:\n'))

def Sales_Balance():

    sale_value = float(input('Please, enter the value of the sale: '))
    i = input('Do you have a commission fee?')
    if i == 'sim' or i == 'Sim':
        #paymentrool(sale_value)
        pass
    else:
        #paymentrool(sale_valeu)
        pass

def Edit_employee_attributes():

    id = int(input('Please, enter the ID employee:\n'))
    attibute = input('Wich attribute do you wanna change?\n')

    if attibute == 'nome': employee_list[id].name = input('Enter the new name:\n')

    elif attibute == 'endereço': employee_list[id].address = input('Enter the new address:\n')

    elif attibute == 'o ultimo dia de pagamento': employee_list[id].last_payment_day = input('Enter the last payment day:\n')

    elif attibute == 'como irei receber': employee_list[id].way_of_receiving = input('Enter the new way of receiving:\n')

    elif attibute == 'sindicato': employee_list[id].syndicate = input('Enter the new syndicate status:\n')

    elif attibute == 'contrato empregaticio': employee_list[id].type = input('Enter the new employment contract type:\n')

    elif attibute == 'valor da hora trabalhada': employee_list[id].hourly_wage = float(input('Enter the new ourly rate of work:\n'))

    elif attibute == 'valor do salario mensal': employee_list[id].monthly_salary = float(input('Enter the new the salary:\n'))

    elif attibute == 'valor da taxa de comissao': employee_list[id].monthly_salary = float(input('Enter the new sales commission rate:\n'))

    elif attibute == 'Timecard': employee_list[id].timecard = Timecard()

    else: print('Please, insert a valid attributes, like: nome; endereço; ultimo dia de pagamento; como irei receber; sindicado; contrato empregaticio; valor da hora trabalhada; valor do salario mensal ou valor da taxa de comissao.\n'), Edit_employee_attributes()

    Edit_employee_attributes()

    print("Done, attributes has modified by the manager. Backing to Manager's menu...\n")

def Print_Employees(employee_list):

    for i in  range(len(employee_list)):

        print("Name =",employee_list[i].name)
        print("Address =",employee_list[i].address)
        print("Employment contract type =",employee_list[i].type)
        print("Employee's ID =",employee_list[i].id)
        print("Syndicates =",employee_list[i].syndicate)
        print("Last payment day =",employee_list[i].last_payment_day)

        if employee_list[i].type =='Horista' or employee_list[i].type == 'horista':
            print("hour_price=",employee_list[i].hourly_wage)
            print("timecard=",employee_list[i].timecard,'\n')

        if employee_list[i].type =='Comissionado' or employee_list[i].type =='comissionado':
            print("salary=",employee_list[i].monthly_salary)
            print("comision=",employee_list[i].commission_fee,'\n')        

        if employee_list[i].type  == 'Assalariado' or employee_list[i].type =='assalariado':
            print('Salary= ', employee_list[i].monthly_salary,'\n')

    print("\nDone!\nBacking to Manager's menu...\n")

def Write_File_Employees():
    
     with open('Employees_List.txt', 'w') as file:
        for i in range(len(employee_list)):
            file.write("Employee's ID:" + str(employee_list[i].id) + '\n')
            file.write('Name:' + str(employee_list[i].name) + '\n')
            file.write('Address:' + str(employee_list[i].address) + '\n')
            file.write('Employment contract type:' + str(employee_list[i].type) + '\n')
            file.write('Syndicate:' + str(employee_list[i].syndicate) + '\n')
            file.write('Last day payment:' + str(employee_list[i].last_payment_day) + '\n')

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

def Edit_Employees_File():

    with open('Employees_List_data.txt', 'a+') as file:
        for i in range(len(employee_list)):
            file.write("Employee's ID:" + str(employee_list[i].id) + '\n')
            file.write('Name:' + str(employee_list[i].name) + '\n')
            file.write('Address:' + str(employee_list[i].address) + '\n')
            file.write('Employment contract type:' + str(employee_list[i].type) + '\n')
            file.write('Syndicate:' + str(employee_list[i].syndicate) + '\n')
            file.write('Last day payment:' + str(employee_list[i].last_payment_day) + '\n')

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


def Read_Employees_File():

    with open('Employees_List_data.txt', 'a') as file:
        for i in range(len(employee_list)):
            file.write("Employee's ID:" + str(employee_list[i].id) + '\n')
            file.write('Name:' + str(employee_list[i].name) + '\n')
            file.write('Address:' + str(employee_list[i].address) + '\n')
            file.write('Employment contract type:' + str(employee_list[i].type) + '\n')
            file.write('Syndicate:' + str(employee_list[i].syndicate) + '\n')
            file.write('Last day payment:' + str(employee_list[i].last_payment_day) + '\n')

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