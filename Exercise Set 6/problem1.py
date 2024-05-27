class Base1:
    def print(self):
        print("Base1")
        
class Base2():
    def print(self):
        print("Base2")
        
class Derived(Base1, Base2):
    def print(self):
        super().print()