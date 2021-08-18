def Commission_Sales(employee_list, sale_value):

    id = int(input("Please, enter the employee's ID: "))
    employee_list[id].sales.append((employee_list[id].commission_fee * sale_value))