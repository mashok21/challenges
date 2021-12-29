
# class Line:

#     def __init__(self, cor1, cor2):
#         self.cor1 = cor1
#         self.cor2 = cor2
               
#     def distance(self):
#         x1, y1 = self.cor1
#         x2, y2 = self.cor2
#         return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        
#     def slope(self):
#         x1, y1 = self.cor1
#         x2, y2 = self.cor2        
#         return (y2-y1)/(x2-x1)

# cordinate1 = (3,2)
# cordinate2 = (8,10)

# l1 = Line(cordinate1, cordinate2)

# print(l1.distance())
# print(l1.slope())

# class Cylinder:
    
#     def __init__(self, height, radius):
#         self.height = height
#         self.radius = radius
    
#     def volume(self):
#         return (22/7)*(self.radius**2)*(self.height)
    
#     def area(self):
#         return (2*(22/7)*self.radius*self.height) + (2*(22/7)*self.radius**2)
        
# c1 = Cylinder(2,3)

# print(c1.volume())
# print(c1.area())

class Account:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def withdraw(self, amount):
        if self.balance > 0:
            if amount > self.balance:
                return 'Low Balance'
            else:
                self.balance = self.balance - amount
        else:
            return 'Nil Balance'


account_name = Account('Ashok', 1000)
print(account_name.name)
print(account_name.balance)
account_name.deposit(1000)
print(account_name.balance)
account_name.withdraw(2000)
print(account_name.balance)
print(account_name.withdraw(1000))