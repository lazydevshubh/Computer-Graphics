from polygon import polygon
from graphics import *
from start import setaxis
import random

def main():
    win=GraphWin('line',400,400)
    setaxis(win)
    n=int(input())
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
    stack=[(0,0)]
    while len(stack)!=0:
        i=stack.pop()
        #print(stack)
        if i not in filled and i not in bound:
            r=random.randint(0,255)
            g=random.randint(0,255)
            b=random.randint(0,255)
            win.plot(*i,color_rgb(r,g,b))
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