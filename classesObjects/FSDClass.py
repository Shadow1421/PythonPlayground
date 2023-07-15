class Student:
    def __init__(self, userName, address, experience, passoutYear):
        self.userName = userName
        self.address = address
        self.experience = experience
        self.passoutYear = passoutYear

batch = Student("Neeraj", "A-111", 11, 2012)
print(batch.userName)         
print(batch.address)          
print(batch.experience)      
print(batch.passoutYear)    
