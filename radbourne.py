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
	def __init__(self, name, gender, shift):
		self.name = name
		self.gender = gender
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

class Salary():
    def __init__(self, rate, hours):
        self.rate = rate
        self.hours = hours

def calculatePay(self):
    salary = self.rate * self.hours
    if len(str(salary)) <= 5:
        print("Every week before tax, £" + str(salary) + "0 is taken home")
    else:
        print("Every week before tax, £" + str(salary) + " is taken home")

        
        
Ian = Staff("Ian", "Male", "afternoon")
areas(Ian)


IanPay = Salary(8.92, 42)
calculatePay(IanPay)