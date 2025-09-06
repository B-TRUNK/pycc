#Function to Count any text file Words!
def count(file_name):
    try:
        with open(file_name ,encoding="utf-8") as file_content:
            contents = file_content.read()
    except(FileNotFoundError):
        print(f"Sorry ,The File {file_name} is Not Found!")
    else:
        words = contents.split()
        length = len(words)
        print(f"{file_name} word count is approx {length}!")
