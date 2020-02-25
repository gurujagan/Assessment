print("Elgible  Criteria For EMI")
Salary=float(input("Enter the Salary:\t"))
if Salary <= 70000 and Salary >= 60000:
    print("Emi Is provided Upto 3L")
elif(Salary <= 60000 and Salary >= 50000):
    print("Emi is provided Upto 2.5L")
elif(Salary <= 50000 and Salary >= 40000):
    print("Emi is provided upto 2 L")
elif(Salary <= 40000 and Salary >= 30000):    
    print("Emi is Provided upto 1.5L")
elif (Salary < 30000):
    print("Choose Another Scheme ")
else:
    print("Ending")
