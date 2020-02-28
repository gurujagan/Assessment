def Parrot(Talking, Hour):
    if(Talking and (Hour < 7 or Hour > 20)):
       print("True, we are in trouble")
    else:
       print("False, we are not in trouble")
Parrot(True,5)
Parrot(True,23)
Parrot(True,7)       
       
