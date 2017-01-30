from graphics import *

def main():
    #init
    win = GraphWin("My Circle", 1200, 800)
    c = Circle(Point(200,200), 100)

    #draw
    c.draw(win)
    
    #pause and exit
    win.getMouse() # pause for click in window
    win.close()

main()
