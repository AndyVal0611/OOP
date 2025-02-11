print("---------------------------------------------------TASK 1-------------------------------------------------------")
num = int(input("Enter a number: "))
if num > 0:
    print(num, "is a POSITIVE Number.")
elif num < 0:
    print(num, "is a NEGATIVE Number.")
else:
    print("ZERO")

print("")
print("---------------------------------------------------TASK 2-------------------------------------------------------")
for i in range(1, 21):
    if i % 2 == 0:
        print(f"Values: {i}")

user = None
while user != 0:
    user = int(input("Enter a number (enter 0 to stop the loop): "))
    if user == 0:
        print("EXIT.")
    else:
        print(f"You entered: {user}")

print("")

print("---------------------------------------------------TASK 3-------------------------------------------------------")
for k in range(1, 21):
    if k % 5 == 0:
        continue
    if k > 15:
        break
    print(f"Values: {k}")