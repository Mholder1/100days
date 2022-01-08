def printList(list):
    finalString = ""

    for word in list:

        if word != list[-1] and word != list[-2]:
            finalString += word + ", "

        elif word == list[-2]:
            finalString += word + " "

        elif word == list[-1]:
            finalString += "and " + list[-1] + "."
       
    return finalString
        

class Staff():	
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender
		

class Salary(Staff):
    def __init__(self, name, pay):
        super().__init__(name, pay)
        self.pay = pay


def calculatePay(self):
    hourlyRate = self.pay / 2080
    print("hourlyRate of " + self.name + " is £" + "{:.2f}".format(hourlyRate))
 

class Duties(Staff):
    def __init__(self, name, gender, shift):
        super().__init__(name, gender)
        self.shift = shift


def areas(self):
    morningDuties = ["toilets", "kitchens", "dormitories"]
    afternoonDuties = ["corridors", "bedrooms", "living spaces"]

    if self.shift == "morning":
        finalString = printList(morningDuties)
        print("Hello " + self.name + ", your areas include " + finalString)
    elif self.shift == "afternoon":
        finalString = printList(afternoonDuties)
        print("Hello " + self.name + ", your areas include " + finalString)
    else:
        print("failed")

        
Ian = Staff("Ian", "Male")

IanDuties = Duties(Ian.name, Ian.gender, "afternoon")
areas(IanDuties)

IanSalary = Salary(Ian.name, 50000)
calculatePay(IanSalary)



        
