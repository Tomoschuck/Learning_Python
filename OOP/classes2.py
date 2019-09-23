'''' 
USe of constructors method.

>>> the __init__ method.
'''

class Student:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.full = 'I am ' + first + ' ' + last
        
    def student_1(self):
        print('I am ' + first + ' ' + last)
        
    def student_2(self):
        print('I am ' + first + ' ' + last)
    
    
student_1 = Student('Iszo', 'Linux')
Student_2 = Student('Brad', 'Windows')

print(student_1.full)