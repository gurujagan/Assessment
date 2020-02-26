n=int(input("Enter the value:\t"))
if n % 2 != 0:
    print("Weird")
elif (n >2 or n < 5 and n % 2 == 0 ):
    print("Not weird")
elif(n > 6 or n < 20 and n % 2 == 0):
    print("Weird")
elif (n > 20 and n % 2 == 0):
    print("Not weird")
    
