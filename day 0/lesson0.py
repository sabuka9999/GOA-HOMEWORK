from turtle import*
#we want to paint a house
width(7)
color("purple")
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
goto(200, 200)
pendown()



color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(50, 110)
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
goto(150, 110)
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





exitonclick()