import random
from random import *

subjects = []
#[all subjects in school]
classes = []
#[all classes in school]
teacherSub = {}
#{teacher:subject}
blocksS = {}
#{class:{day:[_,class, _, _, class]}}
#{11:{Monday:["", "Maths", "", ""]}}
blocks = {}
#{teacher:{day:[_,class, _, _, class]}}
classSub = {}
#{class:{sub:teacher, sub:teacher}}
subTeacherCount = {}
#{subject:{teacher: count, teacher:count}}
teacherClass = {}
#{teachername:{className}}

days = ["Monday","Tuesday","Wednesday","Thursday", "Friday"]
print("Please be careful when entering the values, this program only accepts values once and continues with that")

c = int(input("Enter number of subjects the school has "))
for i in range(0, c):
    print("Enter subject", i+1, "")
    s = input()
    subjects.append(s)
    subTeacherCount[s] = {}
# print(subjects)
blockN = int(input("How many blocks/periods are there for each teacher (per day)? "))
print("How many teachers are there?")
teacherCount = int(input())
for i in range(0, teacherCount):
    print("Enter teacher number", i+1)
    n = input(" ")
    teacherClass[n] = []
    c = 0
    while c<1:
        print("Enter subject for", n)
        subject = input()
        if subject in subjects:
            c = 5
        else:
            print("That's not a subject this school has please check and re-enter")
    teacherSub[n] = subject
    subTeacherCount[subject][n] = 0
    blocks[n] = {}
    for j in days:
        blocks[n][j] = []
        for k in range(0, blockN):
            blocks[n][j].append("")
classN = int(input("Enter number of year groups (Example Class IX and X, enter 2)"))
for i in range(0, classN):
    print("Enter class name for class number", i+1)
    className = input()
    blocksS[className] = {}
    for day in days:
        blocksS[className][day] = []
        for k in range(0, blockN):
            blocksS[className][day].append("")
    classes.append(className)
    classSub[className] = {}
    count = 0
    while count <1:
        subCount = input("Enter how many subjects this class has")

        if subCount.isnumeric():
            subCount = int(subCount)
            count = 5
        else:
            print("Enter valid number")
    for j in range(0, subCount):
        c = 0
        while c<1:
            print("Enter subject", j+1, "for", className)
            sub = input()
            if sub in subjects:
                tGiven = list(subTeacherCount[sub].keys())[list(subTeacherCount[sub].values()).index(min(subTeacherCount[sub].values()))]
                classSub[className][sub] = tGiven
                subTeacherCount[sub][tGiven] +=1
                teacherClass[tGiven].append(className)
                print(classSub)
                c = 5
            else:
                c = 0
                print("Subject wasn't registered earlier")

    #we just assigned a teacher to each class and their subject
    #all teacher's blocks ready to be assigned
for c in blocksS:
    for day in blocksS[c]:
        choose = list(classSub[c].keys())
        shuffle(choose)
        for block in range(0, len(classSub[c])):
            while (blocksS[c][day][block] == "") :
                tSub = choice(choose)
                t = classSub[c][tSub]
                if (blocks[t][day][block] == ""):
                    blocks[t][day][block] = c
                    blocksS[c][day][block] = tSub
                    choose.remove(tSub)
                    print("Teacher Assigned")
        for block in range(len(classSub[c]), blockN):
            while (blocksS[c][day][block] == ""):
                tSub = choice(list(classSub[c].keys()))
                t  = classSub[c][tSub]
                if (blocks[t][day][block] == ""):
                    blocks[t][day][block] = c
                    blocksS[c][day][block] = tSub
                    print("Teacher Assigned")








#update class time table based on teacher
# for teacher in blocks:
#     for day in blocks[teacher]:
#         for i in range(0, blockN):
#             if blocks[teacher][day][i] != "":
#                 #then this has a class name
#                 blocksS[blocks[teacher][day][i]][day][block] = teacherSub[teacher]


print(blocks)
print(blocksS)
print("Assignment completed")
print("Time table has been made you will now be directed to interface to look at specific time tables")

while True:
    print("Enter 't' to see teacher-wise time tables")
    print("Enter 'cl' to see class-wise time tables")
    toDo = input()
    if toDo == "t":
        teacherView = True
        while teacherView:
            c = 0
            print("Enter teacher name you want to view")
            print("Or enter 'e' to exit this view")
            toDo = input()
            if toDo == "e":
                teacherView = False
            else:
                if toDo in list(blocks.keys()): #15 10 10 10 10 10 10
                    print("Period Number" + " "*(2) + "Monday" + " "*(10-len("Monday")) + "Tuesday" + " "*(10-len("Tuesday")) + "Wednesday" + " "*(10-len("Wednesday")) + "Thursday" + " "*(10-len("Thursday")) + "Friday" + " "*(10-len("Friday")))
                    for i in range(0, blockN):
                        print(str(i+1) + " "*(15-len(str(i+1))) + blocks[toDo]["Monday"][i] + " "*(10-len(blocks[toDo]["Monday"][i]))+ blocks[toDo]["Tuesday"][i] + " "*(10-len(blocks[toDo]["Tuesday"][i])) +blocks[toDo]["Wednesday"][i] + " "*(10-len(blocks[toDo]["Wednesday"][i])) +blocks[toDo]["Thursday"][i] + " "*(10-len(blocks[toDo]["Thursday"][i])) +blocks[toDo]["Friday"][i]+ " "*(10-len(blocks[toDo]["Friday"][i])))
                else:
                    print("Teacher wasn't registered earlier")
    elif toDo == "cl":
        print("Enter class you want to view")
        toDo = input()
        if toDo in list(blocksS.keys()):
            print("Period Number" + " "*(2) + "Monday" + " "*(10-len("Monday")) + "Tuesday" + " "*(10-len("Tuesday")) + "Wednesday" + " "*(10-len("Wednesday")) + "Thursday" + " "*(10-len("Thursday")) + "Friday" + " "*(10-len("Friday")))
            for i in range(0, blockN):
                print(str(i+1) + " "*(15-len(str(i+1))) + blocksS[toDo]["Monday"][i] + " "*(10-len(blocksS[toDo]["Monday"][i]))+ blocksS[toDo]["Tuesday"][i] + " "*(10-len(blocksS[toDo]["Tuesday"][i])) +blocksS[toDo]["Wednesday"][i] + " "*(10-len(blocksS[toDo]["Wednesday"][i])) +blocksS[toDo]["Thursday"][i] + " "*(10-len(blocksS[toDo]["Thursday"][i])) +blocksS[toDo]["Friday"][i]+ " "*(10-len(blocksS[toDo]["Friday"][i])))
            for subject in classSub[toDo]:
                print("This class has", classSub[toDo][subject], "for", subject)
