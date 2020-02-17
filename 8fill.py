from polygon import polygon
from graphics import *
from start import setaxis
import random

def main():
    win=GraphWin('line',400,400)
    setaxis(win)
    n=int(input("Enter the number of vertices"))
    ver=[]
    for i in range(n):
        x,y=map(int,input().split())
        ver+=[[x,y]]
    pixel=polygon(ver,win,'green')
    filled={}
    #print(pixel)
    bound={}
    for i in pixel:
        bound[i]=1
    print("Click inside polygon")
    p=win.getMouse()
    stack=[(int(p.getX()),int(p.getY()))]
    while len(stack)!=0:
        i=stack.pop()
        #print(stack)
        if i not in filled and i not in bound:
            win.plot(*i,"grey")
            filled[i]=1
            x,y=i
            stack+=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            if (((x+1,y) not in bound) and ((x,y+1) not in bound)):
                stack+=[(x+1,y+1)]
            if (((x-1,y) not in bound) and ((x,y+1) not in bound)):
                stack+=[(x-1,y+1)]
            if (((x+1,y) not in bound) and ((x,y-1) not in bound)):
                stack+=[(x+1,y-1)]
            if (((x-1,y) not in bound) and ((x,y-1) not in bound)):
                stack+=[(x-1,y-1)]
    input('exit')

if __name__=='__main__':
	main()