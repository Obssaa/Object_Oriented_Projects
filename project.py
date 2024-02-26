class Employee:
    """This class represents an employee"""
    def __init__(self,empID="",empFirstName="",empLastName="",empSalary=0.0):
        self._empFirstName=empFirstName
        self._empLastName=empLastName
        self._empID=empID;
        self._empSalary=empSalary

    def setEmpFirstName(self,empFirstName):
        self._empFirstName=empFirstName
    def getEmpFirstName(self):
        return self._empFirstName

    def setEmpLastName(self,empLastName):
        self._empLastName=empLastName
    def getEmpLastName(self):
        return self._empLastName

    def setEmpID(self,empID):
        self._empID=empID
    def getEmpID(self):
        return self._empID

    def setEmpSalary(self,empSalary):
        self._empSalary=empSalary
    def getEmpSalary(self):
        return self._empSalary

class Worker(Employee):
    """This class represents a worker"""
    def __init__(self,empID="",empFirstName="",empLastName="",empSalary=0.0,numHoursPerWeek=0):
        super().__init__(empID,empFirstName,empLastName,empSalary)
        self.__numHoursPerWeek=numHoursPerWeek

    def setNumHoursPerWeek(self,numHoursPerWeek):
        self.__numHoursPerWeek=numHoursPerWeek
    def getNumHoursPerWeek(self):
        return self.__numHoursPerWeek

class SwipeCard:
    """This class represents a swipe card"""
    def __init__(self,cardID="",empID=""):
        self.__cardID=cardID
        self.__empID=empID

    def setCardID(self,cardID):
        self.__cardID=cardID
    def getCardID(self):
        return self.__cardID

    def setEmpID(self,empID):
        self.__empID=empID
    def getEmpID(self):
        return self.__empID

class Project:
    """This class represents a project"""
    def __init__(self,projectID="",projectName=""):
        self.__projectID=projectID
        self.__projectName=projectName

    def setProjectName(self,projectName):
        self.__projectName=projectName
    def getProjectName(self):
        return self.__projectName

    def setProjectID(self,projectID):
        self.__projectID=projectID
    def getProjectID(self):
        return self.__projectID

class Manager(Employee):
    """This class represents a manager"""
    def __init__(self,empID="",empFirstName="",empLastName="",empSalary=0.0,swipeCard=SwipeCard()):
        super().__init__(empID,empFirstName,empLastName,empSalary)
        self.__swipeCard=swipeCard
        self.__workers=[]
        self.__projects=[]

    def setSwipeCard(self,swipeCard):
        self.__swipeCard=swipeCard
    def getSwipeCard(self):
        return self.__swipeCard

    def addWorker(self,worker):
        self.__workers.append(worker)

    def addProject(self,projectID,projectName):
        project=Project(projectID,projectName)
        self.__projects.append(project)

worker_1=Worker(empID="123",empFirstName="Saed",empLastName="Ahmed",empSalary=5000,numHoursPerWeek=40)
worker_2=Worker(empID="124",empFirstName="Omar",empLastName="Jamal",empSalary=6000,numHoursPerWeek=45)
swipe_card_1=SwipeCard(cardID="TR5431",empID="M004")
manager_1=Manager(empID="M004",empFirstName="Samir",empLastName="Khaled",empSalary=40000,swipeCard=swipe_card_1)
manager_1.addWorker(worker_1)
manager_1.addWorker(worker_2)
manager_1.addProject("P001","Build a residential home")
print("Done")



