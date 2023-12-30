class First: 
    def setdata(self, value): 
        self.data = value 
    def display(self):
        print(self.data) 
         
         
         
x = First() 
y = First()


print(x)
print(y)
print(isinstance(x, First))

print("="*40)

x.setdata("Ahmed") 
y.setdata(3.14159) 
x.display()
y.display()

print("="*40)

x.data = "New value" 
x.display()

print("="*40)

x.anothername = "spam" 
print(x.anothername)

