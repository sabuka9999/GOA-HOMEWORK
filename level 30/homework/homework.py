#1
try:
    print(hello_world)
except NameError as i:
    print(f"Caught an error: {i}")


my_dict = {'key1': 10, 'key2': 20, 'key3': 30}
try:
    print(my_dict['key4'])
except KeyError as i:
    print(f"Caught an error: {i}")

    
try:
    number = int("12.34")
except ValueError as i:
    print(f"Caught an error: {i}")


#2
    
def sum_numbers(list1):
    return sum([int(x) if isinstance(x, str) else x for x in list1])

print(sum_numbers([10, "10", 5, "3"]))  
