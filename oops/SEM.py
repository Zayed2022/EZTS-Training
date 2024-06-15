## sports equipment management system
class Sport:
    equipments={}
    def add_equipments(self):
        self.newequip=input('Enter Equipment name:')
        if self.newequip in self.equipments:
            print('Equipment already exists')
        else:
            
