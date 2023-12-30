# class A(object): 
# 	def __init__(self, x): 
# 		self.x = x 
# 	
# 	def getX(self): 
# 		return self.X 
# 	
# class B(object): 
# 	def __init__(self, x, y): 
# 		self.x = x 
# 		self.y = y 
# 	def getSum(self): 
# 		return self.X + self.y 


# # inherits from A 
# class C_A(A): 
# 	def isA(self): 
# 		return True
# 	
# 	def isB(self): 
# 		return False


# # inherits from B 
# class C_B(B): 
# 	def isA(self): 
# 		return False
# 	
# 	def isB(self): 
# 		return True

# # return required Object of C based on cond 
# def getC(cond): 
# 	if cond: 
# 		return C_A(1) 
# 	else: 
# 		return C_B(1,2) 

# # Object of C_A 
# ca = getC(True) 
# print(ca.isA()) 
# print(ca.isB()) 
# 	
# # Object of C_B 
# cb = getC(False) 
# print(cb.isA()) 
# print(cb.isB()) 


# class A(object): 
# 	def __init__(self, x): 
# 		self.x = x 
	
# 	def getX(self): 
# 		return self.X 

# # Based on condition C inherits 
# # from A or it inherits from 
# # object i.e. does not inherit A 
# cond = True

# # inherits from A or B 
# class C(A if cond else object): 
# 	def isA(self): 
# 		return True

# # Object of C_A 
# ca = C(1) 
# print(ca.isA()) 
class CSStudent:
	stream = 'cse'				 # Class Variable (Static)
	def __init__(self,name,roll):
		self.name = name		 # Instance Variable
		self.roll = roll		 # Instance Variable

# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream) # prints "cse"
print(b.stream) # prints "cse"
print(a.name) # prints "Geek"
print(b.name) # prints "Nerd"
print(a.roll) # prints "1"
print(b.roll) # prints "2"

# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"


# To change the stream for all instances of the class we can change it 
# directly from the class
CSStudent.stream = 'mech'

print(a.stream) # prints 'mech'
print(b.stream) # prints 'mech'
