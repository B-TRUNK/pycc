write_file_path = 'file_except/written.txt'

with open(write_file_path ,'a') as file_object:
    file_object.write('I Love AI.')
    #file_object.write('\nAI is The Future.')
    print('Written Successfully!')