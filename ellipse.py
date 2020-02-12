from graphics import *
from start import setaxis

def putPixel(win,x,y,h,k):
	return [(x+h,y+k),(x+h,-y+k),(-x+h,y+k),(-x+h,-y+k)]
	
def ellipse(x0,y0,r0,r1):
	pixel=[]
	h=x0
	k=y0
	b=r1
	a=r0
	x=0
	y=b
	d=(a**2)*(1-4*y)+4*(b**2)*(2*x+1)
	while abs((b**2)*x)<abs((a**2)*y):
		if d>0:			
			d+=4*(b**2)*(3+2*x)	+4*(a**2)*(2-2*y)
			y-=1		
		else: 
			d+=4*(b**2)*(3+2*x)
		x+=1
		pixel+=putPixel(win,x,y,h,k)
	d=(b**2)*(4*x+1)+4*(a**2)*(1-2*y)	
	while y>=0:		
		if d>0:#S
			d+=4*(a**2)*(-2*y+3)			
		else:
			d+=4*((b**2)*(2+2*x))+4*(a**2)*(-2*y+3)
			x+=1
		y-=1
		pixel+=putPixel(win,x,y,h,k)	
	return pixel

def main():
	x,y,r0,r1=map(int,input().split())
	win=GraphWin("ellipse",400,400)
	setaxis(win)
	pixel=ellipse(x,y,r0,r1)
	for i in pixel:
		x,y= i
		win.plot(*i)
	input()

if __name__=='__main__':
	main()