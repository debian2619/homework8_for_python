# Method to enter new student details
def accept(self, Name, Rollno, marks1, marks2 ):
    # Creates a new class constructor
    # and pass the details
    ob = Student(Name, Rollno, marks1, marks2 )

    # list containing objects of student class
    ls.append(ob)