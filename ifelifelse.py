num = int(input("Enter a number: "))
if num > 0:
    print("POSITIVE Number")
elif num < 0:
    print("NEGATIVE Number")
else:
    print ("ZERO")

age = int(input("Enter your age: "))
if age >= 13 and age <= 19:
    print("You are a teenager!")
elif age < 13:
    print("You are a child.")
else:
    print("You are an adult.")