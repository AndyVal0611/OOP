# List of numbers
num_list = [3, 6, 2, 9, 11, -23, -52, 76]

for num in num_list:
    if num < 0:
        print(f"Negative number found: {num}")
        continue

    if num == 0:
        print(f"Zero found: {num}")
        pass

    if num == 5:
        print(f"Found 5, breaking the loop!")
        break

    print(f"Processing number: {num}")