import turtle

def draw_shapes():
    #red background setup
    window = turtle.Screen()
    window.bgcolor("red")

    #draw fractal flower
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.resizemode("user")
    brad.shapesize(2, 2, 2)
    brad.speed(10)
    brad.penup()
    brad.setpos(0,200)
    brad.pendown()
    
    #rotate around a circle by 12 degree increments
    for iterator in range(30):
      brad.right(12)
      #draw a square at each angle
      for iterator in range(4):
        brad.forward(100)
        brad.right(90)
    brad.right(90)
    brad.forward(200)
    #draw 2 diamond petals
    for outerator in range(2):
      brad.right(90)
      for iterator in range(2):  
        brad.right(30)
        brad.forward(100)
        brad.left(60)
        brad.forward(100)
        brad.left(150)
      brad.right(90)
    #finish Stem
    brad.forward(150)

    brad.penup()
    brad.setpos(-120,15)

    #Write V for Valeria
    brad.pendown()
    brad.pensize(5)
    brad.left(30)
    brad.forward(50)
    brad.left(120)
    brad.forward(50)
    brad.penup()

    #Write S for Sarah
    brad.setpos(100,19)
    brad.pendown()
    brad.left(33)

    for outerator in range(2):
     for iterator in range(75):
      if (outerator == 0):
          brad.left(3.5)
      else:
          brad.right(3.5) 
      brad.forward(1)

    brad.penup()
    brad.setpos(200,-100)
    brad.shapesize(2, 2, 10)

    window.exitonclick()
     
draw_shapes()
