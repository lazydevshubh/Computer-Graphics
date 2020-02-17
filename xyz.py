from graphics import *
from start import setaxis

def bresenham(x0, y0, x1, y1,win,color):
    dx = x1 - x0
    dy = y1 - y0
    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1
    dx = abs(dx)
    dy = abs(dy)
    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0
    D = 2*dy - dx
    y = 0
    pixel=[]
    for x in range(dx + 1):
        pixel.append((x0 + x*xx + y*yx, y0 + x*xy + y*yy))
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
    for i in pixel:
    	win.plot(*i,color)
    return pixel

def main():
	x1,y1,x2,y2 = map(int,input().split())
	win=GraphWin('line',400,400)
	setaxis(win)
	pixel=bresenham(x1,y1,x2,y2,win,'blue')
	input()

if __name__=='__main__':
	main()