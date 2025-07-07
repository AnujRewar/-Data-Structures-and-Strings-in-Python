#create a dictionary of student names and their marks
marksheet={"anuj":98,"aman":88,"aakash":99,"azad":80}
 
 #input a user name
name=input("Enter the name of a student.").lower()

#retrive the marks of the student
try:
    if name in marksheet:
        print(f"{name.title()}'s marks:{marksheet[name]}")
    else:
        print("Student not found.")
except:
    print("Unknown error")