class Students: #Student Class
    def __init__(self, name, grade, percentage,team): #Method
        self.name=name #Attribute
        self.grade=grade
        self.percentage=percentage
        self.team=team
        
    def students_details(self):
        print(f"{self.name} is in grade {self.grade} , with the percentage {self.percentage}%, and is in team {self.team}") 
team1='A'
team2= 'B'
studentFromSectionA= Students('Madhav', 'A', 97, team1)
studentFromSectionB= Students('Madhu', 'A', 97, team2)
print(studentFromSectionA.__dict__)
studentFromSectionA.students_details()
studentFromSectionB.students_details()
# 4 Features in OOPs:-
'''
1. Abstraction:- Hiding unnecesary deatils from the user through class, methods
2. Encapsulation:- Restrict the access to certain attributes or methods
3. Inheritance
4. Polymorphism


'''

#Abstraction:-
'''
Abstraction = Hidden Details

For example electromagnetic waves at surface level we don't know much about that but we are bascilly using alot of electronic devices in our daily life

Another example the message sending button we use in our chat application we know on clicking the that button the typed text or the message will get send to the desired recipents we want to text

For Example ATM machine also


Abstract Class:-
1. A class which contains one or more abstract methods and concrete methods.
2. Abstract class must have at least one abstract method.


'''
from abc import ABC , abstractmethod
class States(ABC):
    @abstractmethod
    def Food(self):
        pass
    def Belongs(self):
        print("This state belongs to India") 


class TamilNadu(States):
    def Food(self):
        print("Ohhh Yeah Idli Dosa Sambar Chatni Chatni")

class Haryana(States):
    def Food(self):
        print("Maakhe di roti sarsoaa da saag")
        
        
class Bihar(States):
    def Food(self):
        print("Liiti Choka")
        
        
t1=TamilNadu()
h1=Haryana()
b1=Bihar()

t1.Food()
        
    





