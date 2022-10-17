#defining person as class
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def print_name(self):
        print(f" Fullname:{self.first_name} {self.last_name}")




#Here inherit the person class to student
class Student(Person):
    def __init__(self,first_name,last_name,age,list):
        super().__init__( first_name,last_name,age)
        self.lectures=list
        self.newlist=[]


    def list_lecture(self,lectures):
        for i  in self.lectures:
            self.newlist.append(i)
            print(f"list_of_lectures:{self.newlist}")




    def add_lectures(self,new_lecture):
        print(f"lecture_list={self.lectures}")
        self.lectures.append(new_lecture)
        print(f"added ({new_lecture}) into  list")


    def remove_lecture(self,lecture):
        self.lectures.remove(lecture)
        print(f"deleted({lecture})from list")

s1=Student("meena","lalam",22,['python','AWS'])
s1.print_name()
s1.list_lecture("3")
s1.add_lectures("c++")
s1.remove_lecture("python")





class Professor(Person):
    def __init__(self,first_name,last_name,age,subjects_teaches):
        super().__init__(first_name,last_name,age)
        self.subjects=subjects_teaches
        self.newlist=[]
        #print(f"{subjects_teaches}")

    def list_subjects(self):
        for i in self.subjects:
            self.newlist.append(i)

            print(f"subjects: {self.newlist} ")

    def add_subject(self,new_subject):
        print(f"new_subject={self.subjects}")
        self.subjects.append(new_subject)
        print(f"added ({new_subject}) into subjects")

    def delete_subject(self, sub):
        self.subjects.remove(sub)
        print(f"remove({sub}) from subjects")

p=Professor("syam","tarini",20, ['python' ,'java','DS','OS'])
p.print_name()
p.add_subject("CN")
p.delete_subject("DS")
p.list_subjects()

class Lectures:
    def __init__(self, name, max_no, duration, list):
        self.name = name
        self.max_no = max_no
        self.duration = duration
        self.profes_list = list
        self.newlist=[]

    def display_of_lect_infor(self):
        print("lectures details")
        print(f"name  = {self.name}")
        print(f"max_no= {self.max_no}")
        print(f"duration = {self.duration}")
        print(f"prof_list = {self.profes_list}")

    def add_prof(self, name):

        self.newlist.append(name)
        print(f"added ({name}) into prof_list")

    def profe_list(self):
        for i in self.profes_list:
            self.newlist.append(i)
        print(f"prof_list : {self.newlist} ")


l=Lectures("java",100,"3hours",['mohan','meena','anjali'])
l.display_of_lect_infor()
l.add_prof('siri')
l.profe_list()










#defining person as class
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def print_name(self):
        print(f" Fullname:{self.first_name} {self.last_name}")
        
        
        
        
OUTPUT:
   
 Fullname:meena lalam
list_of_lectures:['python']
list_of_lectures:['python', 'AWS']
lecture_list=['python', 'AWS']
added (c++) into  list
deleted(python)from list
 Fullname:syam tarini
new_subject=['python', 'java', 'DS', 'OS']
added (CN) into subjects
remove(DS) from subjects
subjects: ['python'] 
subjects: ['python', 'java'] 
subjects: ['python', 'java', 'OS'] 
subjects: ['python', 'java', 'OS', 'CN'] 
lectures details
name  = java
max_no= 100
duration = 3hours
prof_list = ['mohan', 'meena', 'anjali']
added (siri) into prof_list
prof_list : ['siri', 'mohan', 'meena', 'anjali'] 










    










