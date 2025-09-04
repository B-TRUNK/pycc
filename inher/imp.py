from supercar import *

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

gas_car = Car('ford' ,'mustang' ,1970)
gas_car.fill_gas_tank()
#Override
my_tesla.fill_gas_tank()
