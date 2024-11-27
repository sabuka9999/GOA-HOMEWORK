#1
def hello_world():
    return "Hello world!"
    
print(hello_world())

#2
def hello_person(name):
    return f"Hello {name}"

print(hello_person("John"))

#3
def multiply(a, b):
    return a * b

print(multiply(4, 5))

#4
def add_three_numbers(a, b, c):
    return a + b + c

print(add_three_numbers(1, 2, 3))

#5
def check_adult(age):
    if age >= 18:
        return "Adult"
    else:
        return "Not an adult"

print(check_adult(20))

#6
def check_passed(score):
    if score > 80:
        return "Passed"
    else:
        return "Failed"

print(check_passed(85))

#7
from turtle import *


def draw_square(size):
    for _ in range(4):
        forward(size)
        right(90)


def draw_four_squares():
    for _ in range(4):
        draw_square(100)  
        penup()            
        forward(150)       
        pendown()         


draw_four_squares()


exitonclick()



