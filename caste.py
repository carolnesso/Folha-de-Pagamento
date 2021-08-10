class Employee:
    def __init__(self, name, address, type, payment_day, way_of_receiving, syndicate, id):
        self.name = name
        self.address = address
        self.type = type
        self.payment_day = payment_day
        self.way_of_receiving = way_of_receiving
        self.syndicate = syndicate
        self.id = id
    
    def system_ID(self, system_id):
        system_id = "0"
        while system_id >= 0:
            self.id = system_id + 1

        system_id = system_id + 1

#hourly wage == taxa por hora

class Hourly(Employee):

    def __init__(self, name, address, type, payment_day, way_of_receiving, syndicate, id, hourly_wage, timecard):
        self.hourly_wage = hourly_wage
        self.timecard = timecard
        

        super().__init__(name, address, type, payment_day, way_of_receiving, syndicate, id)

class Salaried(Employee):

    def __init__(self, name, address, type, payment_day, way_of_receiving, syndicate, id, monthly_salary):
        self.monthly_salary = monthly_salary

        super().__init__(name, address, type, payment_day, way_of_receiving, syndicate, id)

class Commissioned(Salaried):

    def __init__(self, name, address, type, payment_day, way_of_receiving, syndicate, id, monthly_salary, commission_fee):
        self.commission_fee = commission_fee

        super().__init__(name, address, type, payment_day, way_of_receiving, syndicate, id, monthly_salary)