num = [3, 6, 2, 9, 11, -23]

for i in range(len(num)):
    if num[i] == 0:
        print(f"The first zero is: {num[i]}")
        break
    elif num[i] % 2 != 0:
        print(f"The first odd number is: {num[i]}")
        break

print("Next testing")

for i in range(len(num)):
    if num[i] == 0:
        print(f"The first zero is: {num[i]}")
        break
    elif num[i] % 2 == 0: 
        print(f"The first even number is: {num[i]}")
        break

print("Zero")
