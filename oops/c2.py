class animal:
    def __init__(self,name,eats,legs):
        self.name=name
        self.eats=eats
        self.legs=legs
    def details(self):
        print(f"Name:{self.name}\neats:{self.eats}\nlegs:{self.legs}")
l=animal("Lion","meat",4) 
l.details()