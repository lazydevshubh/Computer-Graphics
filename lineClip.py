from line import bresenham as l
from start import setaxis
from polygon import polygon
from graphics import *
global t1,t2
t1=0
t2=1
def isClip(p,q):
    global t1,t2
    flag=1
    if p<0:
        r=q/p
        if r>t2:
            flag=0
        elif r>t1:
            t1=r
    elif p>0:
        r=q/p
        if r<t1:
            flag=0
        else:
            t2=r
    elif q<0:
        flag=0
    return flag
def clip(bxmin,bymin,bxmax,bymax,x1,y1,x2,y2):
    global t1,t2
    dx=x2-x1
    if(isClip(-dx,y1-bymin)):
        if(isClip(dx,bxmax-x1)):
            dy=y2-y1
            if(isClip(-dy,y1-bymin)):
                if(isClip(dy,bymax-y1)):
                    if t2<1:
                        x2=x1+t2*dx
                        y2=y1+t2*dy
                    if t1>0:
                        x1+=t1*dx
                        y1+=t1*dy
    
    return list(map(int,[x1,y1,x2,y2]))
def main():
    win=GraphWin('line',400,400)
    setaxis(win)
    bxmin,bymin=map(int,input("enter the lower vertex").split())
    bxmax,bymax=map(int,input("enter the upper vertex").split())
    x1,y1=map(int,input("Enter the first vertex").split())
    x2,y2=map(int,input("Enter the second vertex").split())
    l(x1,y1,x2,y2,win,'red')
    l(*clip(bxmin,bymin,bxmax,bymax,x1,y1,x2,y2),win,'blue')
    polygon([(bxmin,bymin),(bxmax,bymin),(bxmax,bymax),(bxmin,bymax)],win,'green')
    input("exit")
if __name__=='__main__':
    main()