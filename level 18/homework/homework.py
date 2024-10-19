#Task 1
a = 14
b = 7
print(a + b)

#Task 2
first_name = "john"
last_name = "Doe"
#კონკატენაცია არის პროცესის სახელწოდება, როდესაც სტრინგები ერთდება ერთმანეთთან
print(first_name +""+ last_name)

#Task 3
a = 5
b = 10
print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True


#Task 4
a = 5
b = 10
print(a > b) 
print(a < b) 
print(b == a) 
print(a != b) 
print(a >= b)
print(a <= b)

#Task 5
print(5 + 5 == 8 + 2)  # True
print(10 - 2 > 6 * 1)  # True
print(3 ** 2 <= 5 * 3) # True

#Task 6
# AND ოპერატორი
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

# OR ოპერატორი
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

#Task 7
for i in range(1, 11):
    print(i)

#Task 8
numbers = [1, 2, 3, 4, 5]
total_sum = 0
for num in numbers:
    total_sum += num
print(total_sum)

#Task 9
message = "Hello, World!"
for char in message:
    print(char)

#Task 10
i = 1
while i <= 10:
    print(i)
    i += 1

#Task 11
total = 0
i = 1
while total < 50:
    total += i
    i += 1
print(total)

#Task 12
def check_number_divisibility(num):
    if num % 3 == 0 or num % 5 == 0:
        print(f"{num} it will divided by 3 or 5")
    else:
        print(f"{num} it is not divisible by 3 or 5")

check_number_divisibility(15)

#Task 13
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

print(calculate_average([1, 3, 4, 5, 2]))

#Task 14
def alternate_uppercase(text):
    result = ''
    for i in range(len(text)):
        if i % 2 == 0:
            result += text[i].upper()
        else:
            result += text[i].lower()
    return result

print(alternate_uppercase("hello"))

#Task 15
def square_numbers(numbers):
    squared_list = []
    for num in numbers:
        squared_list.append(num ** 2)
    return squared_list

print(square_numbers([3, 12, 5, 2, 6]))