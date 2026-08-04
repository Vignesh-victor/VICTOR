a= int (input("salary "))
b= int (input("age "))
if (a>=30000 or b<=25):
    v = int(input("your eligible for loan\nenter your loan amount"))
    if (v<=100000):
        print("you eligible for loan")
    else:
        print("maximum loan amount is ONE LAKS")
else:
    print("you not eligible for loan")
