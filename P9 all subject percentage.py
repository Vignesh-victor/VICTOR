t= int (input("ENTER YOUR TAMIL MARK "))
e= int (input("ENGLISH MARK "))
m= int (input("MATHE MARK "))
sc=int (input("SCIENCE MARK "))
so=int (input("SOCIAL MARK "))
ad= t+e+m+sc+so
avg=ad/5
if (avg<35):
    print("additional class is required")
else:
    print("you are good to go ")
