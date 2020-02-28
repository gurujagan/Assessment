def Speeding(Speed,Birthday):
    Warn=0
    if Birthday:
        warn=5
        if Speed <= 60 + warn:
            print(0)
    elif Speed >= 81 + warn:
        print(2)
    else:
        print(1)
Speeding(60,False)
Speeding(65,False)
Speeding(65,True) 
