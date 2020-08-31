import xlsxwriter
from xlsxwriter import workbook
import json
import time
import datetime
from datetime import datetime


class Get_Info:
    def __init__(self,serial,info_dict):
        self.serial = serial
        self.info_dict = info_dict
        self.answers = []
    
    #function will make file for storing answers
    def create_file(self):
        file_name = input("State name for storage file: ")
        self.f_name = file_name + ".txt"
        self.file = open(f_name, "a")

    #function states questions and obtains answers
    def q_and_a(self):
        '''
        self.answers.append(input("Please state your name: "))
        self.answers.append(input("Now state your surname: "))
        self.answers.append(int(input("How old are you: ")))
        self.answers.append(input("What month were you born in: "))
        self.answers.append(input("What's your favourite colour: "))
        self.answers.append(input("what job are you in: "))
        self.answers.append(input("which state are you living in: ")) 
        '''
        self.name = input("Please state your name: ")
        self.surname = input("Now state your surname: ")
        self.age = int(input("How old are you: "))
        self.month = input("What month were you born in: ")
        self.colour = input("What's your favourite colour: ")
        self.job = input("what job are you in: ")
        self.state = input("which state are you living in: ")

    #function adds the users answers to a dictionary
    def make_dict(self):
        #self.info_dict[self.serial] = self.answers
        self.info_dict[self.serial] = {}
        self.info_dict[self.serial] ['name']= self.name
        self.info_dict[self.serial] ['surname']= self.surname
        self.info_dict[self.serial] ['age']= self.age
        self.info_dict[self.serial] ['colour']= self.colour
        self.info_dict[self.serial] ['month']= self.month
        self.info_dict[self.serial] ['job']= self.job
        self.info_dict[self.serial] ['state']= self.state
        return self.info_dict

    #function will store the answers in the file as json 
    def store_answers(self):
        with open(self.f_name, "a") as outfile:
            json.dump(self.info_dict, outfile, indent=2)
            #for data in self.answers:
            #    outfile.write(str(data))
            #    outfile.write(',')
            #outfile.write('\n')


class Send_To_Excel():
    def __init__(self,info):
        self.info = info
 
    #create excel document
    def open_excel(self):
        self.workbook = xlsxwriter.Workbook('Information collection.xlsx')
        self.worksheet = self.workbook.add_worksheet()
        self.make_table()
    
    #append to rows and columns...create header for data
    def make_table(self):
        row = 0
        col = 0
        self.worksheet.write(row,col,'S/N')
        self.worksheet.write(row,col+1,'First Name')
        self.worksheet.write(row,col+2,'Last Name')
        self.worksheet.write(row,col+3,'Age')
        self.worksheet.write(row,col+4,'Favourite color')
        self.worksheet.write(row,col+5,'Birthday Month')
        self.worksheet.write(row,col+6,'Current Job')
        self.worksheet.write(row,col+7,'State')
        self.fill_table()
        
    #data from file is exported and placed in created excel sheet within their respective columns
    def fill_table(self):
        '''
        test_dict = {
                        '1':{
                            'name':'Ebuka',
                            "surname": "ifechukwu",
                            "age": 22,
                            "colour": "black",
                            "month": "sep",
                            "job": "engineer",
                            "state": "lagos"
                        },
                        '2': {
                            "name": "chidera",
                            "surname": "ifechukwu",
                            "age": 21,
                            "colour": "red",
                            "month": "may",
                            "job": "mass communication",
                            "state": "lagos"
                        }
                    }
        '''
        col = 0
        for key in self.info:
            self.worksheet.write(int(key),col,key)
            self.worksheet.write(int(key),col+1,self.info[key]['name'])
            self.worksheet.write(int(key),col+2,self.info[key]['surname'])
            self.worksheet.write(int(key),col+3,self.info[key]['age'])
            self.worksheet.write(int(key),col+4,self.info[key]['colour'])
            self.worksheet.write(int(key),col+5,self.info[key]['month'])
            self.worksheet.write(int(key),col+6,self.info[key]['job'])
            self.worksheet.write(int(key),col+7,self.info[key]['state'])
            
        self.workbook.close()
        


print("Welcome welcome")
check = True
info_dict = {}

while check:
    while True:
        try:
            number = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep that's an integer!")
            print(number)
            break
        finally:
            print("Finally, I executed!")

    test = Get_Info(number,info_dict)
    test.create_file()
    test.q_and_a()
    info = test.make_dict()
    ask = input("anymore to add: ")
    if ask == "no":
        test.store_answers()
        check = False

next_level = Send_To_Excel(info)
next_level.open_excel()
#next_level.make_table()
#next_level.fill_table()
