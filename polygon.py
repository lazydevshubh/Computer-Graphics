from line import bresenham as l
from start import setaxis
from graphics import *

def polygon(ver,win,color):
    #a+=[a[0]]
    a=ver.copy()
    print(a)
    a+=[a[0]]
    pixel=[]
    for i in range(len(a)-1):
        #print(a[i+1][0],a[i+1][1],a[i][0],a[i][1])
        pixel+=l(a[i+1][0],a[i+1][1],a[i][0],a[i][1],win,color)
    a=a[:-1]
    return pixel
def main():
	win=GraphWin('line',400,400)
	setaxis(win)
	n=int(input('no of vertices'))
	ver=[]
	for i in range(n):
		x,y=map(int,input().split())
		ver+=[[x,y]]
	print(ver)
	polygon(ver,win,'green')
	input('exit')

if __name__=='__main__':
    main()
