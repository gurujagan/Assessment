def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile):
    print("True")
    print("Both monkeys are smiling")
  elif (not a_smile and not b_smile):
    print("True")
    print("We are in trouble as both are not smiling")
  else:
    print("False")
    
monkey_trouble(True,True)    
monkey_trouble(False,False)
monkey_trouble(True,False)
