from graphics import *

def main():
    #init
    c = Circle(Point(200,200), 100)
    c.setFill(color_rgb(130, 0, 130))
    win = GraphWin("Update Example", 1200, 800, autoflush=False)

    #actions
    c.draw(win)
    
    for i in range(5000):
        # <drawing commands for ith frame>
        c.move(.1, 0)
        update(30)
    
    #pause and exit
    win.getMouse() # pause for click in window
    win.close()

main()
