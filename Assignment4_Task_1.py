#Task 1: Read a File and Handle Errors
#======================================
try:
    file_name = open("sample.txt", "r")
    print("Reading file content\n",)
    #print(file_name.read())
    counter = 1
    with open('sample.txt', 'r') as file:
        for line in file:
            print('Line ',counter,':', line, end='')
            counter+=1
    file_name.close()
except FileNotFoundError:
    print("Error.The file 'sample.txt' was not found.")





