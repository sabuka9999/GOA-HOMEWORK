from turtle import*
bgcolor("skyblue")
#we want paint a house

width(7)
color("purple")
penup()
goto(-200, -200)
pendown()

begin_fill()


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(0, 0)
pendown()

#paint the roof


color("red")


begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(-150, -60)
pendown()


color("brown")
begin_fill()
right(60)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)





penup()
goto(-50, -60)
pendown()
right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
end_fill()

width(3)
penup()
forward(150)
pendown()
color("black")
begin_fill()
forward(75)
right(90)
forward(75)
right(90)
forward(40)
right(90)
forward(75)
end_fill()
#The GOA text on the flag
penup()
goto(-50, 125)
color("green")
write("GOA", font=("Arial", 26, "bold"))

goto(-770, -200)
color("lightgreen")
begin_fill()
right(180)
pendown()
forward(1540)

right(90)
forward(200)
right(90)
forward(1540)
right(90)
forward(200)
end_fill()
#draw trunk
penup()
goto(-600, -200)
pendown()
color("brown")
begin_fill()
setheading(90)
forward(150)
right(90)
forward(20)
right(90)
forward(150)
end_fill()

#Draw leaves
penup()
goto(-690, 50)
pendown()
color("green")
begin_fill()
circle(100)
end_fill()


#Draw trunk
penup()
goto(600, -200)
pendown()
color("brown")
begin_fill()
setheading(90)
forward(150)
right(90)
forward(20)
right(90)
forward(150)
end_fill()

#Draw leaves
penup()
goto(510, 50)
pendown()
color("green")
begin_fill()
circle(100)
end_fill()







exitonclick()

































































exitonclick()
























































































































exitonclick