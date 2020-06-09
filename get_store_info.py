#from datetime import datetime

class Test_Results:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def Create_Info_File(self):
        full_name = self.name + self.surname
        file = open(full_name, "w")
        file.write(self.name + " " + self.surname + " is ready to proceed with what needs to be done")

    def Add_info(self):
        pass


print("Testing program")
test = Test_Results("Ebuka","Ifechukwu", 23)
test.Create_Info_File()
print("Program testing complete")