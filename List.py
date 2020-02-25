Cars=["Volvo","Ford","Mahindra","Mercedes"]
for vehi in Cars:
    print(vehi)
#To add a value in List    
Cars.append("Maruthi")
print(Cars)

print("-------------------------------------------------------")
Guru={"Fname":"Guru","Mname":"Moorthy","Lname":"Viswanathan"}
print(Guru)
#To add a key in Dictionary
Guru["Age"]=23
print(Guru)
# To return a Default State not an Error
Guru.get("Status","Invalid key")
# To delete a Dictionary
Guru.clear()
print(Guru)
