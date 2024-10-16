#Task 1

count = 0
for i in range(101):
    if count >= 50 and count <= 60:
        count += 1
        continue
    print(count)
    count += 1


#Task 2

total = 0
num = 1

while num <= 10:
    total += num
    num += 1
print(total - 5)


#Task 3

user_input = int(input("Enter a num: "))

if user_input % 2 == 0:
    print(f"{user_input} is an Odd")
else:
    print(f"{user_input} is an Even")


#Task 4

user_input = int(input("Enter a Grade: "))

if user_input <60:
   print(f"{user_input} Grade F")

if user_input <70:
   print(f"{user_input} Grade D")

if user_input <80:
   print(f"{user_input} Grade C")

if user_input <90:
   print(f"{user_input} Grade B")

if user_input ==100:
    print(f"{user_input} Grade A")

 

#Task 5

user_age = int(input("Enter your age: "))

if user_age <= 13:
    print("You are kid")
elif user_age > 13 and user_age < 20:
    print("You are teenager")
elif user_age >= 20:
    print("You are grown up")
else:
    print("Enter right age!")


















































