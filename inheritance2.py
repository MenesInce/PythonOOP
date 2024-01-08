class Person() :
    def __init__(self, firstName, lastName, phoneNumber) : 
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber

    
    def __repr__(self) :
        return "First Name : {} \nLast Name : {} \nPhone Number : {}".format(self.firstName,self.lastName,self.phoneNumber)

class Student(Person):
    def __init__(self, firstName, lastName, phoneNumber, studentNumber):
        super().__init__(firstName, lastName, phoneNumber)
        self.studentNumber = studentNumber

    def __repr__(self) :
        return  "First Name : {} \nLast Name : {} \nPhone Number : {} \nStudent Number : {}".format(self.firstName,self.lastName,self.phoneNumber,self.studentNumber)

class Professor(Person) :
    def __init__(self, firstName, lastName, phoneNumber,branchName, salary):
        super().__init__(firstName, lastName, phoneNumber)
        self.branchName = branchName
        self.salary = salary
    
    def __repr__(self) :
        return  "First Name : {} \nLast Name : {} \nPhone Number : {} \nBranch Name : {} \nSalary : {}".format(self.firstName,self.lastName,self.phoneNumber,self.branchName, self.salary)

    


per1 = Person("Beyza", "Aslan", "012345678974")
print(per1)
print("--------------------")
std1 = Student("Ali", "Tas", "014785236920", "88865")
print(std1)
print("--------------------")
prof1 = Professor("Ayaz Salih","Canevinden","025896374125","Math",25000)
print(prof1)