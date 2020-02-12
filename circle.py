from graphics import *
def drawCircle(xc,yc,x,y):
	return [(xc+x,yc+y),(xc-x,yc+y),(xc+x,yc-y),(xc-x,yc-y),(xc+y,yc+x),(xc-y,yc+x),(xc+y,yc-x),(xc-y,yc-x)]

def bresenham(xc,yc,r):
    pixels=[]
    x=0
    y=r 
    d=3-2*r
    pixels+=drawCircle(xc, yc, x, y)
    while (y >= x): 
        x+=1;  
        if (d>0): 
            y-=1
            d=d+4*(x-y)+10; 
        else:
            d=d+4*x+6; 
        pixels+=drawCircle(xc, yc, x, y)
    return pixels


def main():
    print("Enter the center and radius")
    win=GraphWin('circle',400,400)
    win.setCoords(-200,-200,200,200)
    x,y,r = map(int,input().split())
    pixel=bresenham(x,y,r)
    for i in pixel:
        x,y= i
        win.plot(*i)
    input()

if __name__=='__main__':
    main()