import os,time

for i in range(0,1): #Annimation intro
    os.system("cls")
    print ("C...... C... S....... M......... S.....")
    time.sleep(1)
    os.system("cls")
    print ("Co..... Ca.. So...... Ma........ Sy....")
    time.sleep(1)
    os.system("cls")
    print ("Con.... Car. Sof..... Man....... Sys...")
    time.sleep(1)
    os.system("cls")
    print ("Cont... Card Soft.... Mana...... Syst..")
    time.sleep(1)
    os.system("cls")
    print ("Contac. Card Softw... Manag..... Syste.")
    time.sleep(1)
    os.system("cls")
    print ("Contact Card Softwar. Manage.... System")
    time.sleep(1)
    os.system("cls")
    print ("Contact Card Software Management System")
    time.sleep(1)
    os.system("cls")

print ("-    -    -    -    -    ") #Welcome screen
print ("Contact Card Software Management System")
print ("-    -    -    -    -    ")

dict={"1stname":"", "last_name":"", "databirth":"", "email":"", "address_street":"", "address_city":"","address_postal":"",
      "address_building_num":"","notes":""}
firstName=input("First Name: ").strip().capitalize()
lastName=input("Last Name: ").strip().capitalize()
dataofBirth=input("Data of Birt DD/MM/YYYY: ").strip()
email=input("Email: ").strip().capitalize()
address_Street=input("Street name: ").strip().lower()
address_City=input("City: ").strip().lower()
address_Postal=input("Postal Code: ").strip() # possible mix of numbers and letters
address_Building_num=input("Building No.: ").strip().lower()
notes=input("Notes: ")
time.sleep(1)
os.system("cls")

dict["1stname"]=firstName
dict["last_name"]=lastName
dict["databirth"]=dataofBirth
dict["email"]=email
dict["address_street"]=address_Street
dict["address_city"]=address_City
dict["address_postal"]=address_Postal
dict["address_building_num"]=address_Building_num
dict["notes"]=notes
print ("-    -    -    -    -    ")
print (f"First Name: {dict['1stname']}")
print (f"Last Name: {dict['last_name']}")
print (f"Date of Birth: {dict['databirth']}")
print (f"Email: {dict['email']}")
print (f"Address: {dict['address_street']}, City: {dict['address_city']},Postal code: {dict['address_postal']} Building Number: {dict['address_building_num']}")
print (f"Notes: {dict['notes']}")
print ("*    *    *    *    *    *")