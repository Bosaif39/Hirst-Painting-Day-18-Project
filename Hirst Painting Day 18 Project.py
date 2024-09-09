import colorgram
import turtle 
import random 
tim=Turtle()

colors = colorgram.extract("sweet.jpg",30)
rgb_colors=[]

for i in colors:
    r= i.rgb.r
    b= i.rgb.b
    g= i.rgb.g
    
    new_color=(r,g,b)
    rgb_colors.appedn(new_color)

tim.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(300)
tim.forward(300)
tim.setheading(0)
num_of_dots=100

for i in range(1,num_of_dots+1):
    tim.dot(20,random.choice(rgb_colors))
    tim.forward(50)
    
    if i %1 0==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(100)
        tim.forward(500)
        tim.setheading(0)



screen = Screen()

screen.exitonclick()

