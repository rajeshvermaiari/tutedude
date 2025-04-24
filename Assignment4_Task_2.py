#Task 2: Write and Append Data to a File
#======================================
from typing import Concatenate

try:
    fname = 'output.txt'
    open(fname, 'w').close() #Clear content of file writting

    new_text = input("Enter text to write to the file :")
    file_name = open(fname, "a")
    file_name.write(new_text + "\n")
    file_name.close()
    print("Data successfully written to output.txt")

    new_text = input("Enter additional text to append:")
    file_name = open(fname, "a")
    file_name.write(new_text + "\n")
    file_name.close()
    print("Data successfully appended")

    print("Final content of output.txt")
    file_name = open(fname, "r")
    print(file_name.read())
    file_name.close()

except FileNotFoundError:
    print("Error.The file 'sample.txt' was not found.")
