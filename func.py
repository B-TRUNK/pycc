#simple function
def simple():
    print(
        'This is a siple function'
    )

print("\n\n")

#function calling
simple()

#passing a parameter to a function
name = 'Abanoub'
def param(name):
    print(
        f"Hello ,{name}!"
    )
#function calling
param(name)

#passing a default value parameter to a function
def greeting(calling='Anonemous'):
    print(
        f"Hello ,{calling}!"
    )


#function calling
greeting()