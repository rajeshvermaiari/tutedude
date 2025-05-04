#Task 1: Create a Dictionary of Student Marks
#=============================================

marks_dict = {
                'amit':{'hindi':41,'english':88,'maths':58,'sst':78,'science':88},
                'rajesh':{'hindi':65,'english':48,'maths':98,'sst':88,'science':74},
                'rohit':{'hindi':66,'english':41,'maths':52,'sst':38,'science':98}
              }
#print(marks_dict)
#print(marks_dict.get('amit'))

std_name = input("Enter the student name: ")
isExist = (std_name in marks_dict)
if isExist:
    print(std_name.capitalize(),'marks :', marks_dict.get(std_name))
else:
    print('Student not found')
