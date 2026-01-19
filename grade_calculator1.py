s=int(input("enter the number of students "))
for i in range(1,s+1):
    print(f"details of student {i} :")
    n=int(input("enter the number of subjects: "))
    l1=[]
    l2=[]
    c=0
    for i in range(1,n+1):
       l1.append(int(input(f"enter the subject {i} marks: ")))
    for i in l1:
        if(i>100):
            l2.append("invalid")
        if(35<=i<=100):
            l2.append("pass")
        else:
            l2.append("fail")
    for i in l2:
        if(i=='pass'):
            c=c+1
    if(c==5):
        total=sum(l1)
        per=(total/(n*100))*100
        if(per>=90):
            print(f"{per:.2f}% , Grade : A")
            print("Excellent job! you have earned 1st class")
        elif(75<=per<90):
            print(f"{per:.2f}% , Grade : B")
            print("Good job! you have earned 2nd class")
        elif(55<=per<75):
            print(f"{per:.2f}% , Grade : C")
            print("Nice job! but try to improve")
        else:
            print(f"{per:.2f}% , Grade : D")
            print("Try to improve more")
    else:
        print(f"you have failed {n-c} subjects.please rewrite the failed exams")

        
