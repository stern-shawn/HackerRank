class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

# My code

# Create a Student class which inherits from class Person, and extends its
# functionality by having a 'scores' list and a calculate class with returns
# a letter representation of their grade based on the average of all scores.
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        # do CLASS.__init__ to use the inherited constructor
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        grade = sum(scores)/len(scores)
        if (grade >= 90):
            return 'O'
        elif (grade < 90 and grade >= 80):
            return 'E'
        elif (grade < 80 and grade >= 70):
            return 'A'
        elif (grade < 70 and grade >= 55):
            return 'P'
        elif (grade < 55 and grade >= 40):
            return 'D'
        elif (grade < 40):
            return 'T'

# End of my code

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
