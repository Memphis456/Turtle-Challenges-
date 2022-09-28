import turtle




turtle.speed(900)
def square():
    x = -200
    y = 200
    while True:
        
        
            
            
        turtle.pu()
        turtle.goto(x, y)
        if x % 50 == 0 and y % 50 == 0 or x % 50 != 0 and y % 50 != 0:
            turtle.begin_fill()
        
        
##        print(x)
##        print(y)
        turtle.pd()
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(25)
        
        turtle.pu()
        turtle.end_fill()
        x += 25
            
        
            
        if x >= 0:
            y -= 25
            x = -200
            turtle.goto(x, y)
            
    
            
        if y <= 0:
            turtle.done()
            turtle.ht()
            

        
        
    


        


square()

    
