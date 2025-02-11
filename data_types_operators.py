print("---------------------------------------------------TASK 1-------------------------------------------------------")
# Data Types
a1_int = 4
a1_float = 1.41
a1_complex = 2 + 5j
a1_str = "Good Morning"
a1_list = ["engineer", "architect", "technician"]
a1_tuple = ("Mathematics", "Science", "English")
a1_set = {"ice cream", "yogurt", "cake"}
a1_frozenset = frozenset({1, 9, 25, 26})
a1_dict = dict(name="Serena", label="bestfriend")
a1_bool = True
a1_none = None

print(type(a1_int))
print(type(a1_float))
print(type(a1_complex))
print(type(a1_str))
print(type(a1_list))
print(type(a1_tuple))
print(type(a1_set))
print(type(a1_frozenset))
print(type(a1_dict))
print(type(a1_bool))
print(type(a1_none))

print("---------------------------------------------------TASK 2-------------------------------------------------------")
# Integers
a2_int = 3
addition_int = a1_int + a2_int
subtraction_int = a1_int - a2_int
multiplication_int = a1_int * a2_int
division_int = a1_int / a2_int

print("Integer Operations:")
print("Addition:", addition_int)
print("Subtraction:", subtraction_int)
print("Multiplication:", multiplication_int)
print("Division:", division_int)
print("")

# Floats
a2_float = 0.71
addition_float = a1_float + a2_float
subtraction_float = a1_float - a2_float
multiplication_float = a1_float * a2_float
division_float = a1_float / a2_float

print("Float Operations:")
print("Addition:", addition_float)
print("Subtraction:", subtraction_float)
print("Multiplication:", multiplication_float)
print("Division:", division_float)
print("")

# String Concatenation
a2_str = "Good Morning"
a2con_str = a2_str + ", Cutie Pie!"
a2sliced_str = a2_str[5:]

print("String Operations:")
print("Concatenated String:", a2con_str)
print("Sliced String:", a2sliced_str)
print("")

# List
a2_list = a1_list.copy()
a2_list.append("lawyer")

print("List Operations:")
print("List after appending 'lawyer':", a2_list)
a2_list.remove("technician")
print("List after removing 'technician':", a2_list)
print("")

# Set
a2_set = a1_set.copy()
a2_set.add("gelato")

print("Set Operations:")
print("Set after adding 'gelato':", a2_set)
a2_set.remove("cake")
print("Set after removing 'cake':", a2_set)
print("")

# Dictionary Access
name = a1_dict.get("name")
label = a1_dict.get("label")

print("Dictionary Access:")
print("Name:", name)
print("Label:", label)

# Modify Dictionary
a1_dict["name"] = "Serena van der Woodsen"
a1_dict["show"] = "Gossip Girl"     # added the "show" section

print("Modified Information:", a1_dict)

print("---------------------------------------------------TASK 3-------------------------------------------------------")
# Provide values fo a3 and b3
a3 = 23
b3 = 15
print("Values:")
print("a3 =", a3)
print("b3 =", b3)
print("")

# Arithmetic Operations
print("Arithmetic Operations:")
print(f"Sum: {a3 + b3}")
print(f"Difference: {a3 - b3}")
print(f"Product: {a3 * b3}")
print(f"Division: {a3 / b3}")
print(f"Modulus: {a3 % b3}")
print(f"Floor Division: {a3 // b3}")
print(f"Exponentiation: {a3 ** b3}")
print("")

# Comparison Operations
print("Comparison Operations:")
print(f"Equal to: {a3 == b3}")
print(f"Not equal to: {a3 != b3}")
print(f"Greater than: {a3 > b3}")
print(f"Less than: {a3 < b3}")
print(f"Greater than or equal to: {a3 >= b3}")
print(f"Less than or equal to: {a3 <= b3}")
print("")

# Logical Operations
print("Logical Operations:")
print(f"Logical AND: {a3 > 0 and b3 > 0}")
print(f"Logical OR: {a3 > 0 or b3 > 0}")
print(f"Logical NOT: {not a3 > 0}")
print("")

# Bitwise Operations
print("Bitwise Operations:")
print(f"Bitwise AND: {a3 & b3}")
print(f"Bitwise OR: {a3 | b3}")
print(f"Bitwise XOR: {a3 ^ b3}")
print(f"Bitwise NOT: {~a3}")
print(f"Left Shift: {a3 << 1}")
print(f"Right Shift: {a3 >> 1}")

#End
print("-------------------------------------------------END OF TASK-----------------------------------------------------")