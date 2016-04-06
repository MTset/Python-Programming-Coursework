#
# greeting.py
#
firstName = (input("Fist name: ")).strip()
middleName = (input("Middle name: ")).strip()
lastName = (input("Last name: ")).strip()
fullName  = firstName + " " + middleName + " " + lastName
# The replace is in case there is no middle name
print("Hi", (fullName.title()).replace("  ", " "))