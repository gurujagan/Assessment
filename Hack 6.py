Year=int(input("Enter the year: "))
if (Year % 4 == 0 and Year % 100 != 0):
    print("leap year")
elif(Year % 400 == 0):
    print("leap Year")
else:
    print("Not a leap Year")
    
