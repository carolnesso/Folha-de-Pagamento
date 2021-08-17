class Employee:
    def __init__(self, name, address, type, last_payment_day, way_of_receiving, syndicate, id):
        self.__name = name
        self.__address = address
        self.__type = type
        self.__last_payment_day = last_payment_day
        self.__way_of_receiving = way_of_receiving
        self.__syndicate = syndicate
        self.__id = id

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

    @property
    def type(self):
        return self.__type

    @property
    def last_payment_day(self):
        return self.__last_payment_day

    @property
    def way_of_receiving(self):
        return self.__way_of_receiving

    @property
    def syndicate(self):
        return self.__syndicate

    @property
    def id(self):
        return self.__id


    @name.setter
    def name(self, valid_name):
       
        valid_name = input('Insert a valid name, without numbers.\n')
        
        self.__name = valid_name

    @address.setter
    def address(self, valid_address):
        
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
        valid_way_of_receiving = input('Please, insert a valid way of receiving, like Depósito em conta; Cheque em mãos; Envio do cheque pelos correios.\n')
        
        self.__way_of_receiving = valid_way_of_receiving

    @syndicate.setter
    def syndicate(self, boolean):
        self.__syndicate = boolean

    @id.setter
    def id(self, i):
        #i will be the count of the list, in this case, where we find the employee
        self.__id = i
    
