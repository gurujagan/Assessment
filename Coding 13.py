def Party(cigar,weekend):
    if weekend:
        if cigar>= 40:
            print("True")
        else:
            print("False")
    else:
         if cigar>= 40 and cigar<=60:
             print("True")
         else:
             print("False")
Party(30,"False")
Party(50,"False")
Party(70,"True")
             
