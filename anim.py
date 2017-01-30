from graphics import *

def main():
    #init
    win = GraphWin("Update Example", 1300, 850, autoflush=False)
    c = Circle(Point(200,200), 100)
    c.setFill(color_rgb(255, 127, 0))

    #actions
    c.draw(win)
    xUns = .1
    yUns = -.1
    flip = True
    
    for i in range(100):
        for frame in range(5000):
            if(flip):
                c.move(xUns, 0)
            else:
                c.move(0, yUns)
                
            update(30)

        flip = not(flip)
            
        if( i%2 == 0):
            yUns*= -1
        else:
            xUns*= -1
            
        
    #pause and exit
    win.getMouse() # pause for click in window
    win.close()

main()
