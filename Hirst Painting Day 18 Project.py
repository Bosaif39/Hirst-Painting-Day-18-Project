import colorgram
import turtle
import random

tim = turtle.Turtle()

colors = colorgram.extract("sweet.jpg", 30)  # Adjust the number of colors if needed
rgb_colors = []

# Convert the extracted colors to RGB tuples and store them in a list
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color) 

# Set up the turtle module
tim.colormode(255)  
tim.speed("fastest")  
tim.penup()  
tim.hideturtle()  
tim.setheading(300)  # Set the initial heading of the turtle
tim.forward(300)  # Move the turtle forward to position it
tim.setheading(0)  # Reset heading to 0 (facing right)

num_of_dots = 100

# Draw the dots
for i in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))  
    tim.forward(50)  # Move forward to the next dot position
    
    # Move to the next line after every 10 dots
    if i % 10 == 0:  
        tim.setheading(90)  # Set heading to 90 (facing up)
        tim.forward(50)  # Move forward to start a new line
        tim.setheading(180)  # Set heading to 180 (facing left)
        tim.forward(500)  # Move back to the start position of the line
        tim.setheading(0)  # Reset heading to 0 (facing right)

screen = turtle.Screen() 
screen.exitonclick() 
