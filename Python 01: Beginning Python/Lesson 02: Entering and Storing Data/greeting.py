#
# greeting.py
#
firstName = (input("Please enter your Fist name: ")).strip()
middleName = (input("Please enter your Middle name: ")).strip()
lastName = (input("Please enter your Last name: ")).strip()
nameList = (firstName, middleName, lastName)
fullName  = " ".join(nameList)
# The replace is in case there is no middle name
print("It's nice to meet you", (fullName.title()).replace("  ", " "))