import json


class Get_Info:
    def __init__(self, name, surname, age,serial):
        self.name = name
        self.surname = surname
        self.age = age
        self.answers = [self.name,self.surname,self.age]
    
    #function will make file for storing answers
    def create_file(self):
        self.file = open("info_file.txt", "a+")

    #function states questions and obtains answers
    def q_and_a(self):
        self.answers.append(input("What month were you born in: "))
        self.answers.append(input("What's your favourite colour: "))
        self.answers.append(input("what job are you in: "))
        self.answers.append(input("which state are you living in: ")) 
        self.make_dict()
        
    def make_dict(self):
        self.info_dict = {}
        self.info_dict[1] = self.answers

    #function will store the answers in the file
    def store_answers(self):
        with open('info_file.txt', "a") as outfile:
            json.dump(self.info_dict, outfile)


class Send_To_Excel:
    def __init__(self):
        pass
 
    def open_excel(self):
        pass

    def make_table(self):
        pass

    def fill_table(self):
        pass

print("Welcome welcome")
number = int(input("what is your number: "))
name = input("Please state your name: ")
surname = input("Now state your surname: ")
age = int(input("How old are you: "))

test = Get_Info(name,surname,age)
test.create_file()
test.q_and_a()
print(test.answers)
test.store_answers()
with open('info_file.txt') as json_file:
    data = json.load(json_file)
    print(data)