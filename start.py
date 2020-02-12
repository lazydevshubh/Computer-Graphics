from graphics import *

def setaxis(win):
	win.setCoords(-200,-200,200,200)
	l1=Line(Point(-200,0),Point(200,0))
	l2=Line(Point(0,-200),Point(0,200))
	l1.setFill('blue')
	l2.setFill('red')
	l1.setArrow('both')
	l2.setArrow('both')
	l1.draw(win)
	l2.draw(win)

def main():
	''''''

if __name__=='__main__':
    main()