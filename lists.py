#Working with Lists
print("\n\n")

motorcycles = ['VW', 'BMW', 'Mercedes','Audi']
print(motorcycles)
motorcycles[1] = 'Opel'         #modifying an item
motorcycles.append('Honda')     #add a new item at the end

print(motorcycles)
motorcycles.insert(0, 'Yamaha') #add a new item at a specific position
del motorcycles[0]              #removes a specific element
#motorcycles.remove('ducati')    #removing an item by value

#popping
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print("\n")


for item in motorcycles:
    {
        print(item)
    }

#Lists are Like Arrays
#Accessing a One Specific Element of a List:
print(motorcycles[0])

#Accessing the Second Last Element of a List:
print(motorcycles[-2])
print("\n")
#================================================================
#Organizing a List
motorcycles.sort()
motorcycles.sort(reverse=True)

#just displaying your list in a sorted matter but doesn't affect it!
print(sorted(motorcycles))

#sort at a reverse order
motorcycles.reverse()

#finding the length of a lisr
print(len(motorcycles))

print(motorcycles,"\n\n")

#================================================================
#Making Numerical Lists

for value in range(1, 5):
    print(value)


numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)


squares = []
for value in range(1, 11):

    square = value ** 2
    squares.append(square)

print(squares)

#Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

#Working with Part of a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])

#Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

