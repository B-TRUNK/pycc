#including file length function
from word_count import *

#Handling the ZeroDivisionError Exception
num_1 ,num_2 = 4 ,0
try:
    answer = int(num_1/num_2)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(answer)

#Handling the FileNotFoundError Exception
filename = 'alice.txt'
"""
try:
    with open(filename ,'r' ,-1 ,encoding='utf-8') as file_content:
        contents = file_content.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    print(contents)
"""


#Analyzing Text & Apply to count Function which is imported above
count(filename)

#Failing Silently
#Python has a pass statement that tells it to do nothing in a block