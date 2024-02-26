import datetime,enum

class Gender(enum.Enum):
    male=1
    female=2

class Person:
    """A class that represents a person"""
    def __init__(self,personFirstName="",personLastName="",personAddress="",personDOB=datetime.datetime.now(),personPhoneNumber="",personGender=Gender.female):
        self._personFirstName=personFirstName
        self._personLastName=personLastName
        self._personAddress=personAddress
        self._personDOB=personDOB
        self._personGender=personGender
        self.__personPhoneNumber=personPhoneNumber

    def setPersonFirstName(self,personFirstName):
        self._personFirstName=personFirstName
    def getPersonFirstName(self):
        return self._personFirstName
    def setPersonLastName(self,personLastName):
        self._personLastName=personLastName
    def getPersonLastName(self):
        return self._personLastName
    def setPersonGender(self,personGender):
        self._personGender=personGender
    def getPersonGender(self):
        return self._personGender

    def setPersonPhoneNumber(self,personPhoneNumber):
        self.__personPhoneNumber=personPhoneNumber
    def getPersonPhoneNumber(self):
        return self.__personPhoneNumber

    def setPersonDOB(self,personDOB):
        self._personDOB=personDOB
    def getPersonDOB(self):
        return self._personDOB


    def setPersonAddress(self,personAddress):
        self._personAddress=personAddress
    def getPersonAddress(self):
        return self._personAddress

    def calcAge(self):
        time_difference=datetime.datetime.now()-self._personDOB #subtract the date of birth from the current date and time
        age=(time_difference.days)/365 #calculate it in years, there are 365 days in a year
        return round(age) #return a rounded age (no fractions)

    def __str__(self):
        return "Name: {} {} \nAddress: {}".format(
            self._personFirstName, self._personLastName,self._personAddress
        )

class Employee(Person):
    """An employee class which inherits from a Person classs"""
    def __init__(self,personFirstName="",personLastName="",personAddress="",empSalary=0.0,empJobTitle="",personDOB=datetime.datetime.now(),personPhoneNumber="",personGender=Gender.female,empStaffID="",empDOJ=datetime.datetime.now(),empQualifications=""):
        super().__init__(personFirstName,personLastName,personAddress,personDOB,personPhoneNumber,personGender)
        #Person.__init__(self,personFirstName,personLastName,personAddress)
        self.empSalary=empSalary
        self.empJobTitle=empJobTitle
        self.empStaffID=empStaffID
        self.empDOJ=empDOJ
        self.empQualifications=empQualifications

    def setEmpStaffID(self,empStaffID):
        self.empStaffID=empStaffID
    def getEmpStaffID(self):
        return self.empStaffID
    def setEmpDOJ(self,empDOJ):
        self.empDOJ=empDOJ
    def getEmpDOJ(self):
        return self.empDOJ
    def setEmpQualifications(self,empQualifications):
        self.empQualifications=empQualifications
    def getEmpQualifications(self):
        return self.empQualifications
    def setEmpSalary(self,empSalary):
        self.empSalary=empSalary
    def getEmpSalary(self):
        return self.empSalary

    def setEmpJobTitle(self,empJobTitle):
        self.empJobTitle=empJobTitle
    def getEmpJobTitle(self):
        return self.empJobTitle

    def getMaternalAllowance(self):
        age=super().calcAge() #we calculated the age by refering to the calcAge function in the parent class
        salaryIncrease=0 #slaray increase is 0 for everyone
        if self._personGender==Gender.female and age>25: #except females older than 25
            salaryIncrease=0.05*self.empSalary #here we calculate the salary increase
        return salaryIncrease


    def __str__(self):
        return super().__str__()+"\nSalary: {}\nJob Title: {}".format(
            str(self.empSalary),self.empJobTitle
        )


