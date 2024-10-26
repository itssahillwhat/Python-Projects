# import turtle
# jake = turtle.Turtle()

from turtle import Turtle, Screen
jake = Turtle()  # Create Object
print(jake)

# Calling method associated with object
jake.shape("turtle")
jake.color("red")
jake.fd(100)
jake.lt(90)
jake.bk(100)


my_screen = Screen()
print(my_screen.canvheight, my_screen.canvwidth)  # tap into attribute using obj name
my_screen.exitonclick()
