read_file_path = 'file_except/digits.txt'

data_list = []

with open(read_file_path) as file_object:
    #contents = file_object.read()
#print(contents)

#Reading Line by Line
    for line in file_object:
        print(line)

#Making a List of Lines from a File
        data_list.append(line.rstrip())
#print List
print(data_list)