class Employee:
    def __init__(self, name, address, id):
        self.name = name
        self.address = address
        self.id = id
    
    def system_ID(self, system_id):
        system_id = "0"
        while system_id >= 0:
            self.id = system_id + 1

        system_id = system_id + 1
        