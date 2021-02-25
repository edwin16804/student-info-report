

global d
d={}


def inputData():
    while True:
        
        
        while True:
            r=input("Enter the roll no. of the student: ")
            if r.isdigit():
                if r in d:
                    print()
                    print("ROLL NUMBER LREADY IN THE LIST!!")
                else:    
                    break
            
            elif r.isalnum or r.isalpha:
                print()
                print("PLEASE ENTER ROLL NUMBER IN DIGITS ONLY!")
        print()
                
            
        n=input("Enter name of the student: ")
        print()

        while True:
            ge=input("Enter gender[M for male and F for female]: ")
            if ge=='M' or ge=='m' or ge=='f' or ge=='F':
                break
            else:
                print()
                print("PLEASE ENTER 'M' MALE AND 'F' FOR FEMALE!")
                
        print()
        
        f=input("Enter  father name: ")
        print()
        
        mo=input("Enter  mother name: ")
        print()
        
        while True:
            gno=input("Enter GRNO: ")
            if gno.isdigit():
               break
            else:
                print()
                print("PLEASE ENTER GRNO. IN DIGITS ONLY!")
        print()
                
        while True:
            cl=int(input("Enter class from 1 to 12: "))
            if cl>=1 and cl<=12:
                    break
            else:
                print()
                print("CLASS SHOULD BE FROM 1 TO 12 ONLY!")
        print()
        
        while True:
            se=input("Enter section[A,B or C]: ")
            if se.isalpha():
                if se=='a' or se=='A' or se=='b' or se=='B' or se=='c' or se=='C':
                        break
                else:
                    print("Section should be from A,B,C!!")
            else:
                print()
                print("SECTION SHOULD BE IN ALPHABETS ONLY!")
        print()
        
        ad=input("Enter address: ")
        print()
        
        while True:
            
            ph=input("Enter phone number:")
            le=len(ph)
            flag=0
            if le==10:
                if ph.isdigit():
                    break
            elif le!=10:
                print("PHONE NUMBER SHOULD BE OF 10 DIGITS!")
        print()
        while True:
            m1=int(input("Enter marks of student in Subject-1: "))
            if m1<100:
                break
            else:
                print("MARKS SHOULD BE OUT OF HUNDRED ONLY!")
        print()
        while True:
            m2=int(input("Enter marks of student in Subject-2: "))
            if m2<100:
                break
            else:
                print("MARKS SHOULD BE OUT OF HUNDRED ONLY!")
        print() 
        while True:
            m3=int(input("Enter marks of student in Subject-3: "))
            if m3<100:
                break
            else:
                print("MARKS SHOULD BE OUT OF HUNDRED ONLY!")
        print()
        while True:
            m4=int(input("Enter marks of student in Subject-4: "))
            if m4<100:
                break
            else:
                print("MARKS SHOULD BE OUT OF HUNDRED ONLY!")
        print()
        while True:
            m5=int(input("Enter marks of student in Subject-5: "))
            if m5<100:
                break
            else:
                print("MARKS SHOULD BE OUT OF HUNDRED ONLY!")
        tot=m1+m2+m3+m4+m5
        per=(tot/500)*100
        if per<=100 or per>=90:
            gr='A1'
        elif per<=80 or per>=70:
            gr='A2'
        elif per<=60 or per>=50:
            gr='B1'
        elif per<=40 or per>=30:
            gr='B2'
        elif per<30:
            gr='C'
            
        print()
        d[r]={'student name':n,"gender":ge,'father name':f,'mother name:':mo,'GR number':gno,'Class':cl,'section':se,'address':ad,'phone number':ph,'marks in Subject-1':m1,'marks in Subject-2':m1,'marks in Subject-3':m3,'marks in Subject-4':m4,'marks in Subject-5':m5,'Total marks':tot,'Percentage':per,"Grade":gr}
        
        print()

        ch=input("Do you want to input more details?['N' for no and 'Y' for yes]")
        if ch=='n'or ch=='N':
            break
        print("--------------------------------------------------------------------------------")
        print()

def inputOne():
    for i in range(0,1):
        
        
        while True:
            r=input("Enter the roll no. of the student: ")
            if r.isdigit():
                if r in d:
                    print()
                    print("ROLL NUMBER LREADY IN THE LIST!!")
                else:    
                    break
            
            elif r.isalnum or r.isalpha:
                print()
                print("PLEASE ENTER ROLL NUMBER IN DIGITS ONLY!")
        print()
                
            
        n=input("Enter name of the student: ")
        print()

        while True:
            ge=input("Enter gender[M for male and F for female]: ")
            if ge=='M' or ge=='m' or ge=='f' or ge=='F':
                break
            else:
                print()
                print("PLEASE ENTER 'M' MALE AND 'F' FOR FEMALE!")
                
        print()
        
        f=input("Enter  father name: ")
        print()
        
        mo=input("Enter  mother name: ")
        print()
        
        while True:
            gno=input("Enter GRNO: ")
            if gno.isdigit():
               break
            else:
                print()
                print("PLEASE ENTER GRNO. IN DIGITS ONLY!")
        print()
                
        while True:
            cl=int(input("Enter class from 1 to 12: "))
            if cl>=1 and cl<=12:
                    break
            else:
                print()
                print("CLASS SHOULD BE FROM 1 TO 12 ONLY!")
        print()
        
        while True:
            se=input("Enter section[A,B or C]: ")
            if se.isalpha():
                if se=='a' or se=='A' or se=='b' or se=='B' or se=='c' or se=='C':
                        break
                else:
                    print("Section should be from A,B,C!!")
            else:
                print()
                print("SECTION SHOULD BE IN ALPHABETS ONLY!")
        print()
        
        ad=input("Enter address: ")
        print()
        
        while True:
            
            ph=input("Enter phone number:")
            le=len(ph)
            flag=0
            if le==10:
                if ph.isdigit():
                    break
            elif le!=10:
                print()
                print("Phone number should be of 10 digits ")
        print()
        while True:
            m1=int(input("enter marks of student in Subject-1: "))
            if m1<100:
                break
            else:
                print()
                print("marks should be out of hundred!")
        print()
        while True:
            m2=int(input("enter marks of student in Subject-2: "))
            if m2<100:
                break
            else:
                print()
                print("marks should be out of hundred!")
        print() 
        while True:
            m3=int(input("enter marks of student in Subject-3: "))
            if m3<100:
                break
            else:
                print()
                print("marks should be out of hundred!")
        print()
        while True:
            m4=int(input("enter marks of student in Subject-4: "))
            if m4<100:
                break
            else:
                print()
                print("marks should be out of hundred!")
        print()
        while True:
            m5=int(input("enter marks of student in Subject-5: "))
            if m5<100:
                break
            else:
                print()
                print("marks should be out of hundred!")
        tot=m1+m2+m3+m4+m5
        per=(tot/500)*100
        if per<=100 or per>=90:
            gr='A1'
        elif per<=80 or per>=70:
            gr='A2'
        elif per<=60 or per>=50:
            gr='B1'
        elif per<=40 or per>=30:
            gr='B2'
        elif per<30:
            gr='C'
        print()
        d[r]={'student name':n,"gender":ge,'father name':f,'mother name:':mo,'GR number':gno,'Class':cl,'section':se,'address':ad,'phone number':ph,'marks in Subject-1':m1,'marks in Subject-2':m1,'marks in Subject-3':m3,'marks in Subject-4':m4,'marks in Subject-5':m5,'Total marks':tot,'Percentage':per,'Grade':gr}
        
def displayAll():
    for r in d:
        d1=d[r]
        print("Roll number ==> ",r)
        for key,value in d1.items():
            print(key,' ==> ', value)
        
        print()

def report():
    for r in d:
        d1=d[r]
        print("Roll number ==> ",r)
        for key,value in d1.items():
            print(key,' ==> ', value)
        print()
        
            
            
def editAll():
    for r in d:
        d1=d[r]
        print("Roll number ==> ",r)
        for key,value in d1.items():
            print(key,' ==> ', value)
        ch=input("Do you want to make any changes?[N for no and Y for yes]")
        if ch=='Y' or ch=='y':
            d.pop(r)
            print()
            print("Enter details of the student")
            print()
            inputOne()
        
        
        
        
    
        

def editOne():
    m3=input("Which students' information you want to edit[enter rno. ]: ")
    print()
    if m3 in d:
        d1=d[m3]
        print("Roll number ==> ",m3)
        for key,value in d1.items():
            print(key,' ==> ', value)
        d.pop(m3)
        print()
        print("Enter details of the student")
        print()
        inputOne()
    else:
        print("Roll number not in list!!")
        
    

def delRec():
    m3=input("Which students' record you want to delete?[enter rno. ]: ")
    print()
    if m3 in d:
        d1=d[m3]
        for key,value in d1.items():
            print(key,' ==> ', value)
        d.pop(m3)
        print("The record has been deleted")
        
    else:
        print("Roll number not in list!!")

def displayOne(key):
    if key in d:
        d1=d[key]
        for key,value in d1.items():
            print(key, '==>' , value)
        
def displayName():
    name=input("Enter name of the student")
    for key in d:
        d1=d[key]
        if d1['student name']==name:
            displayOne(key)

def displayGRNO():
    grno=input("Enter GRNO. of the student")
    for key in d:
        d1=d[key]
        if d1['GR number']==grno:
            displayOne(key)
        else:
            print("GR number not in the list!!")

def subMarks():
    for r in d:
        d1=d[r]
        for key,value in d1.items():
            if key=='student name' or key=='GR number' or key=='marks in Subject-1' or key=='marks in Subject-2' or key=='marks in Subject-3' or key=='marks in Subject-4' or key=='marks in Subject-5':
                print(key, '==>' , value)
            
        n=input("Press enter to see Subject wise marks of next student")
        print()

def genderList():
    print("----List of boys----")
    for key in d:
        d1=d[key]
        if d1['gender']=='m' or d1['gender']=='M':
            print(d1['student name'])
    print()
    print("----List of girls----")
    for key in d:
        d1=d[key]
        if d1['gender']=='f' or d1['gender']=='F':
            print(d1['student name'])

def topThree():
    n1=0
    n2=0
    n3=0
    l=[]
    l1=[]
    for key in d:
        d1=d[key]
        n=d1.get('Total marks')
        l.append(n)
    
    for i in range(len(l)):
        if l[i]>n1:
            n3=n2
            n2=n1
            n1=l[i]
        elif l[i]>n2:
            n3=n2
            n2=l[i]
        elif l[i]>n3:
            n3=l[i]
    for key in d:
        d1=d[key]
        
        if d1['Total marks']==n1:
            a=d1['student name']
        elif d1['Total marks']==n2:
            b=d1['student name']
        elif d1['Total marks']==n3:
            c= d1['student name']
    print('1.', a ,' : ' ,n1)
    print('2.', b ,' : ' ,n2)
    print('3.', c ,' : ' ,n3)
        

def menu():
    
        print("***********************/LIST OF ACTIONS YOU CAN PERFORM\***********************")
        print("[1] to Enter data of students")
        print("[2] to Edit data of students")
        print("[3] to Edit data of a particular student")
        print("[4] to Delete the record of a particular student")
        print("[5] to Display students detail by GRNO.")
        print("[6] to Display students detail by students name")
        print("[7] to Display all students details ")
        print("[8] to Display subject wise marks with  GRNO. and name")
        print("[9] to Display Report Card")
        print("[10] to  Display top three list")
        print("[11] to Display list gender wise")
        print("[12] to Insert details of student")
        print("[13] to Exit")
        print("********************************************************************************")
        print("--------------------------------------------------------------------------------")
def main():
    while True:
        menu()
        while True:
                ch=int(input("Your choice from 1 to 13: "))
                print()
                if ch==1:
                        
                    print("________ENTER DATA OF STUDENTS________")
                    print()
                    inputData()
                    
                    print("--------------------------------------------------------------------------------")
                    print()
                    

                elif ch==2:
                    if len(d)==0:
                        print("Please enter student details first!!")
                    else:
                        print("________EDIT DATA OF  STUDENTS________")
                        print()
                        
                        editAll()
                        print("--------------------------------------------------------------------------------")
                        print()
                elif ch==3:
                    if len(d)==0:
                        print("Please enter student details first!!")
                    else:
                        print("________EDIT DATA OF A PARTICULAR STUDENT________")
                        print()
                        
                        editOne()
                        print("--------------------------------------------------------------------------------")
                        print()
                elif ch==4:
                    if len(d)==0:
                        print("Please enter student details first!!")
                    else:
                        print("________DELETE RECORD OF A PARTICULAR STUDENT________")
                        print()
                        delRec()
                        print("--------------------------------------------------------------------------------")
                        print()
                elif ch==5:
                    if len(d)==0:
                        print("Please enter student details first!!")
                    else:
                        print("________DISPLAY STUDENT DETAILS BY GRNO.________")
                        print()
                        displayGRNO()
                        print("--------------------------------------------------------------------------------")
                        print()
                        
                elif ch==6:
                    if len(d)==0:
                        print("Please enter student details first!!")
                    else:
                        print("________DISPLAY STUDENT DETAILS BY NAME________")
                        print()
                        displayName()
                        print("--------------------------------------------------------------------------------")
                        print()

                elif ch==7:
                    if len(d)==0:
                        print("Please enter student details first!!")
                    else:
                        print("________DISPLAY ALL STUDENTS DETAILS________")
                        print()
                        displayAll()
                        print("--------------------------------------------------------------------------------")
                        print()

                elif ch==8:
                    if len(d)==0:
                        print("Please enter student details first!!")
                    else:
                        print("________DISPLAY SUBJECT-WISE MARKS WITH NAME AND GRNO.________")
                        print()
                        subMarks()
                        print("--------------------------------------------------------------------------------")
                        print()
                        

                elif ch==9:
                    if len(d)==0:
                        print("Please enter student details first!!")
                    else:
                        print("________DISPLAY REPORT CARD________")
                        print()
                        report()
                        print("--------------------------------------------------------------------------------")
                        print()
                        
                elif ch==10:
                    if len(d)==0:
                        print("Please enter student details first!!")
                    else:
                        print("________DISPLAY TOP THREE LIST________")
                        print()
                        print('----Top Three----')
                        topThree()
                        print("--------------------------------------------------------------------------------")
                        print()
                elif ch==11:
                    if len(d)==0:
                        print("Please enter student details first!!")
                    else:
                        print("________DISPLAY GENDER WISE LIST________")
                        print()
                        genderList()
                        print("--------------------------------------------------------------------------------")
                        print()
                        
                elif ch==12:
                    if len(d)==0:
                        print("Please enter student details first!!")
                    else:
                        print("________INSERT DATA OF A STUDENT________")
                        print()
                        inputOne()
                        print("--------------------------------------------------------------------------------")
                        print()
                      
                elif ch==13:
                    print("Thank you for using the program :)")
                    exit()
                print()
                x=input("DO YOU WANT TO SEE THE MENU AGAIN?[N for no and Y for yes] ")
                if x=='y' or x=='Y':
                    menu()
                else:
                    continue
                    print()
    print() 
        
        
main()    
