class Employee:
    def __init__(self, name, address, type, payment_day, way_of_receiving, syndicate, id):
        self.__name = name
        self.__address = address
        self.__type = type
        self.__last_payment_day = payment_day
        self.__way_of_receiving = way_of_receiving
        self.__syndicate = syndicate
        self.__id = id