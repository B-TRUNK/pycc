#simple function
def simple():
    print(
        'This is a siple function'
    )

print("\n\n")

#function calling
simple()

#==================================================================

#passing a parameter to a function
name = 'Abanoub'
def param(name):
    print(
        f"Hello ,{name}!"
    )
#function calling
param(name)

print("\n\n")

#==================================================================

#passing a default value parameter to a function
def greeting(calling='Anonemous'):
    print(
        f"Hello ,{calling}!"
    )

#==================================================================
#function calling
greeting()

print("\n\n")

#Return Functions
def ret_num(num=42):
    return num

#function calling
print(ret_num())
#==================================================================

#Passing a List
def __ret_list(names):
        for name in names :
            print(f"Hello ,{name.title()}!")

names_list = ['Abanoub' ,'David' ,'Jonathan']

print("\n\n")
__ret_list(names_list)

print("\n\n")
#==================================================================
#Passing an Arbitrary Number of Arguments

def make_pizza(*toppings):
#"""Print the list of toppings that have been requested."""
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')