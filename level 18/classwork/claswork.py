
test_string = "hello world"
test_list = [1, 2, 3, 4, 5]

# .upper() - Converts all characters in the string to uppercase.
upper_string = test_string.upper()
print(f".upper(): {upper_string}")  # Output: "HELLO WORLD"

# .lower() - Converts all characters in the string to lowercase.
lower_string = test_string.lower()
print(f".lower(): {lower_string}")  # Output: "hello world"

# .capitalize() - Capitalizes the first character of the string and makes all others lowercase.
capitalized_string = test_string.capitalize()
print(f".capitalize(): {capitalized_string}")  # Output: "Hello world"

# .swapcase() - Swaps the case of each character in the string (uppercase becomes lowercase and vice versa).
swapcase_string = test_string.swapcase()
print(f".swapcase(): {swapcase_string}")  # Output: "HELLO WORLD"

# .find() - Returns the index of the first occurrence of the specified substring, or -1 if not found.
find_result = test_string.find("world")
print(f".find(): {find_result}")  # Output: 6 (the index of "world" in "hello world")

# len() - Returns the length of the string or list (the number of elements).
string_length = len(test_string)
list_length = len(test_list)
print(f"len(): {string_length} (for string), {list_length} (for list)")  # Output: 11 (for string), 5 (for list)

# .index() - Returns the index of the first occurrence of the specified substring. Raises an error if not found.
try:
    index_result = test_string.index("world")
    print(f".index(): {index_result}")  # Output: 6
except ValueError:
    print("Substring not found.")

# .append() - Adds an element to the end of the list.
test_list.append(6)
print(f".append(): {test_list}")  # Output: [1, 2, 3, 4, 5, 6]

# .insert() - Inserts an element at the specified position in the list.
test_list.insert(2, 99)  # Inserts 99 at index 2
print(f".insert(): {test_list}")  # Output: [1, 2, 99, 3, 4, 5, 6]

# .pop() - Removes and returns the element at the specified index (default is the last element).
popped_element = test_list.pop()
print(f".pop(): Popped element is {popped_element}, remaining list is {test_list}")  # Output: 6

# .remove() - Removes the first occurrence of the specified value from the list. Raises an error if not found.
test_list.remove(99)
print(f".remove(): {test_list}")  # Output: [1, 2, 3, 4, 5]

