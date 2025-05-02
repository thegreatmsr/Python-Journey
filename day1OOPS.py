'''
OOPs is the way of organizing code by creating "blueprints" called Classes to represent real world things like a student, car, or house. 

Class: A Class is a blueprint or template for creating objects. 
Object: An Object is a specific instance of a class.

So basically class has two properties attributes and methods,  attributes refers to the properties and methods refer to the actions
and they together made the object

'''
#Using list creating Student records
student_1= ['Madhav', 10] #Name, Grade
student_2= ['Vishakha', 12] 

print(f"{student_1[0]} is in class {student_1[1]}")
print(f"{student_2[0]} is in class {student_2[1]}")

#Why OOPs:-
'''
1. Models Real  World Prowblems
2. Code Resuablity
3. Easier Maintenance
4. Encapsulation
5. Scalability
6. Flexibility

'''

#Using OOPs Creating Student records
class Student:
    def __init__(self, name, grade, classes): #Methods
        self.name=name #Attributes
        self.grade=grade #attributes
        self.classes=classes
    def student_details(self):
        print(f"{self.name} is in class {self.grade} and is in class {self.classes}")
        
    
studentFromSectionA= Student('Madhav', 'A', 11)
studentFromSectionB= Student('Madhu', 'A',11)
print(studentFromSectionA.name, studentFromSectionA.grade)
print(studentFromSectionB.name, studentFromSectionB.grade)

studentFromSectionA.student_details()
studentFromSectionB.student_details()
print(studentFromSectionA.__dict__)


#Modify the values:-
print(studentFromSectionA.classes)
studentFromSectionA.classes=12
print(studentFromSectionA.classes)
#Delete Object property:-
print(studentFromSectionA.__dict__)
del studentFromSectionA.classes
print(studentFromSectionA.__dict__)




