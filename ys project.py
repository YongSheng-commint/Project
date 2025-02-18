import turtle
import random

# Create a screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object named tom
tom = turtle.Turtle()
tom.speed(0)

colorBox = ['#0aebcd', '#8eeb0a', '#db3505', '#8e05db', '#db0505', '#0509db', '#c49000']

se = list(range(140, 180))
seg = list(range(180, 190))
segg = list(range(70, 90))
seggs = list(range(20, 30))

for x in range(3):
    for i in range(450):  
        random.shuffle(colorBox)
        tom.pu()
        tom.fd(random.choice(seg))
        tom.pd()
        tom.color(random.choice(colorBox))
        
        if random.choice([True, False]):
            tom.left(random.choice([5, 10, 15 , 20 , 25]))  
        else:
            tom.right(random.choice([5, 10, 15 , 20 , 25]))  
      
        tom.fd(random.choice(se))
        tom.pu()
        tom.goto(0, 0)  
        tom.pd()


for x in range(3):
    for i in range(500):  
        random.shuffle(colorBox)
        tom.pu()
        tom.fd(random.choice(segg))
        tom.pd()
        tom.color(random.choice(colorBox))
        
        if random.choice([True, False]):
            tom.left(random.choice([5, 10, 15 , 20 , 25]))  
        else:
            tom.right(random.choice([5, 10, 15 , 20 , 25]))  
      
        tom.fd(random.choice(segg))
        tom.pu()
        tom.goto(0, 0)  
        tom.pd()



tom.pensize(1)
for x in range(3):
    for i in range(450):  
        random.shuffle(colorBox)
        tom.pu()
        tom.fd(random.choice(seggs))
        tom.pd()
        tom.color(random.choice(colorBox))
        
        if random.choice([True, False]):
            tom.left(random.choice([5, 10, 15 , 20 , 25]))  
        else:
            tom.right(random.choice([5, 10, 15 , 20 , 25]))  
      
        tom.fd(random.choice(seggs))
        tom.pu()
        tom.goto(0, 0)  
        tom.pd()        



