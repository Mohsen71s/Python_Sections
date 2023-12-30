#example for nested fuction
def function1(x): 
    def function2(y):
        print(y + 2)  
        return y + 2
    return 3 * function2(x)

# call the function
a = function1(2) # what is the output  print a
#b = function2(2.5) # what is the result of that
