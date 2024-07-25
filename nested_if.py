age = int (input("how old are you?:"))

if age >= 18:
	print ("proceed")
	gender = input("Enter gender: ")
	if gender == "male":
		print("move to the 2nd floor")
	elif gender == "female":
		print("move to the 1st floor")
	else:
		print("gender musy be male or female")
else:
	print ("come back next time")
	