import re
total=[]
def highestfunc():
    highest = 0
    id = 0
    if(x==int(num)-1):
     for i in range(int(num)):
        if (int(total[i].get("marks")) > int(highest)):
            highest = int(total[x].get("marks"))
            id = i
     print(f'{total[id].get("name")} with rollno.{total[id].get("rollno")} got highest marks which were {total[id].get("marks")}' )
def lowestfunc():
    lowest = 101
    id = 0
    if (x == int(num)-1):
     for i in range(int(num)):
        if (int(total[i].get("marks")) < int(lowest)):
            lowest = int(total[x].get("marks"))
            id = x
     print(f'{total[id].get("name")} with rollno.{total[id].get("rollno")} got lowest marks which were {total[id].get("marks")}')
def inputrollno():
 total[x]["rollno"]=input('Enter Rollno.: ')
 res = bool(re.match('[\d]+$', total[x]["rollno"]))
 if (res==False):
     print("Roll no. should be a digit.")
     total[x].popitem()
     inputrollno()
 for i in range(x):
     if(total[i]["rollno"]==total[x]["rollno"]and i!=x):
         print("Roll no. should unique.")
         total[x].popitem()
         inputrollno()
def inputname():
    total[x]["name"]=input('Enter Name: ')
    res = bool(re.match('[a-zA-Z\s]+$', total[x]["name"]))
    if (res==False):
        print("Names can be only alphabetical letters and spaces.")
        total[x].popitem()
        inputname()
def inputage():
    total[x]["age"]=input('Enter Age: ')
    res = bool(re.match('[\d]+$', total[x]["age"]))
    if (res==False):
        print('Age must be digits.')
        total[x].popitem()
        inputage()
def inputmarks():
    total[x]["marks"]=input('Enter Marks: ')
    res = bool(re.match('[\d]+$', total[x]["marks"]))
    if (res==False):
        print('Marks must be in digits')
        total[x].popitem()
        inputmarks()
    elif(int(total[x]["marks"])<0 or int(total[x]["marks"])>100):
        print('Marks must be between zero and 100')
        total[x].popitem()
        inputmarks()
def averagefunc():
    sum = 0
    if (x == int(num)-1):
     for i in range(int(num)):
        sum += int(total[i].get("marks"))
        average = sum / int(num)
     print(f'average is  {average}')


def main():
        globals()['student%s' % x] = {'name': 'not asigned1', 'age': 'not assigned', 'rollno': 'not assigned',
                                     'marks': 'not assigned'}
        total.append(globals()['student%s' % x])
        inputrollno()
        inputname()
        inputage()
        inputmarks()
        highestfunc()
        lowestfunc()
        averagefunc()
        if(x==int(num)-1):
            print('**roll_num** |     **name**    |  **age**  | **marks**')
            for i in range(int(num)):
             print(f'{total[i].get("rollno").center(13)}|{total[i].get("name").center(17)}|{total[i].get("age").center(11)}|{total[i].get("marks").center(10)}')


num= input('Total students : ')
for x in range(int(num)):
 main()








