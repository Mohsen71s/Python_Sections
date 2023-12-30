import module

#print(calc.add(10, 2))

# calc.spam('gumby')



print('-------------------------------')

"""
    Imports Happen Only Once
"""
print(module.a)  # 1

module.a = 10   # Change attribute in module
print(module.a)   #10


import module  # Just fetches already loaded module

print(module.a)   # Code wasn't rerun: attribute unchanged
