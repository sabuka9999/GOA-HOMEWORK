#2
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key in my_dict:
    print(key)

my_dict2 = {'a': 5, 'b': 6, 'c': 7}
   
for key in my_dict2.keys():
    print(key)

my_dict3 = {'a': 3, 'b': 4, 'c': 8}

for value in my_dict3.values():
    print(value)

my_dict4 = {'a': 11, 'b': 12, 'c': 13}

for key in my_dict4:
    print(my_dict[key])

my_dict5 = {'a': 14, 'b': 15, 'c': 16}

for key, value in my_dict5.items():
    print(value)

#3
dict1 = {'name': 'Alice', 'age': 25, 'city': "New York"}
dict2 = {'brand': 'Toyota', 'model': 'Corolla', 'year': 2020}
dict3 = {'fruit': 'Apple', 'color': 'Red', 'price': 1.5}
dict4 = {'language': 'Python', 'version': 3.10, 'creator': 'Guido'}
dict5 = {'animal': 'Dog', 'breed': 'Labrador', 'age': 5}

print("Name of the person is " + dict1["name"] + " and she lives in " + dict1["city"] + ".")
print("She is " + str(dict1["age"]) + " years old.")

print("The fruit is " + dict3["fruit"] + " and its color is " + dict3["color"] + ".")
print("The price of the " + dict3["fruit"] + " is $" + str(dict3["price"]) + ".")

print("The programming language is " + dict4["language"] + " and its version is " + str(dict4["version"]) + ".")
print("It was created by " + dict4["creator"] + ".")


print("The animal is a " + dict5["animal"] + " of breed " + dict5["breed"] + ".")
print("The age of the " + dict5["breed"] + " is " + str(dict5["age"]) + " years.")