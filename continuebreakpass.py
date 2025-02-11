for i in range(50):
    if i < 10:
        print([i])
        print("one")

    elif 10 < i < 20:
        print([i])
        print("two")

    elif i == 20:
        print([i])
        print("three")
        break

print("Loop completed.")

# List of numbers
num_list = [3, 5, 6, 2, 9, 11, -23, -52, 76]

for num in num_list:
    if num < 0:
        print(f"Negative number found: {num}")
        continue

    if num == 0:
        print(f"Zero found: {num}")
        pass

    if num == 5:
        print(f"The loop will break at 5")
        break

    print(f"Processing number: {num}")
