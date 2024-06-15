class animal:
    def nm(self):
        self.name = input("Name:")
        self.eats=input("Eats:")
        self.legs=input("Legs:")
    def details(self):
        print(f"Name:{self.name}\neats:{self.eats}\nlegs:{self.legs}")
l=animal()
l.nm()
l.details()