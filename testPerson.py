from person import Person,Employee,Gender,datetime

emp_1=Employee(personFirstName="Sara",personLastName="Samir",
               personAddress="Abu Dhabi",empSalary=25000.0,
               empJobTitle="Civil engineer",personGender=Gender.female,personDOB=datetime.datetime(1990, 5, 17),
               personPhoneNumber="050411122",empStaffID="001",empDOJ=datetime.datetime(2021, 9, 13),
               empQualifications="BS in Civil Engineering"
               )
emp_2=Employee()
emp_2.setPersonFirstName("Amal")
print("Sara's age: ",emp_1.calcAge()," years old")
print("Sara's salary increase=",emp_1.getMaternalAllowance())
emp_2.setPersonLastName("Saed")
##

print(emp_1.__str__())
print("Done")