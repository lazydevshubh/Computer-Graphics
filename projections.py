from polygon import polygon
from start3d import setaxis
from line import bresenham as l
from graphics import *
import math
import random


def draw(ver,win):
	ver2d = []
	for i in ver:
		ver2d.append((i[0] - int(i[2]*(math.cos(math.pi/4))), i[1] - int(i[2]*(math.sin(math.pi/4)))))
	r=random.randint(0,255)
	g=random.randint(0,255)
	b=random.randint(0,255)
	polygon(ver2d[:4],win,color_rgb(r,g,b))
	r=random.randint(0,255)
	g=random.randint(0,255)
	b=random.randint(0,255)
	polygon(ver2d[4:],win,color_rgb(r,g,b))
	for i in range(4):
		l(*ver2d[i],*ver2d[i+4],win,"black")


def perspective(ver,cop,ref,nor,win):
	x,y,z=map(int,ref)
	a,b,c=map(int,cop)
	n1,n2,n3=map(int,nor)
	d0=sum([a*b for a,b in zip(ref,nor)])
	d1=sum([a*b for a,b in zip(cop,nor)])
	d=d0-d1
	proj=[[n1*a + d , b*n1 , c*n1 , n1],[a*n2 , b*n2 + d , c*n2 , n2],[a*n3 , b*n3 , c*n3 + d , n3],[-a*d0 , -b*d0 , -c*d0 , -d1]]
	result = [[int(sum(a * b for a, b in zip(A_row, B_col))) for B_col in zip(*proj)] for A_row in ver]
	for i in range(len(result)):
		for j in range(len(result[0])):
			result[i][j]//=result[i][-1]
		result[i]=result[i][:3]
	draw(result,win)

def parallel(ver,cop,ref,nor,win):
	x,y,z=map(int,ref)
	a,b,c=map(int,cop)
	n1,n2,n3=map(int,nor)
	d0=sum([a*b for a,b in zip(ref,nor)])
	d1=sum([a*b for a,b in zip(cop,nor)])
	d=d0-d1
	proj=[[d1-a*n1,-b*n1,-c*n1,0],[-a*n2,d1-b*n2,c*n2,0],[-a*n3,-b*n3,d1-c*n3,0],[a*d0,b*d0,c*d0,d1]]
	result = [[int(sum(a * b for a, b in zip(A_row, B_col))) for B_col in zip(*proj)] for A_row in ver]
	for i in range(len(result)):
		for j in range(len(result[0])):
			result[i][j]//=result[i][-1]
		result[i]=result[i][:3]
	draw(result,win)


def main():
	win=GraphWin('line',400,400)
	setaxis(win)
	ver=[[0,0,0,1],[150,0,0,1],[150,150,0,1],[0,150,0,1],[0,0,150,1],[150,0,150,1],[150,150,150,1],[0,150,150,1]]
	draw(ver,win)
	while(1):
		k=win.getKey()
		if k=="1":
			perspective(ver,[500,500,600],[0,0,0],[0,0,1],win)
		elif k=="2":
			perspective(ver,[-150,-150,-100],[250,0,0],[1,1,0],win)
		elif k=="3":
			perspective(ver,[250,250,250],[0,0,0],[1,1,1],win)
		elif k=="o":
			parallel(ver,[0,0,1],[0,0,0],[0,0,1],win)
		elif k=="i":
			parallel(ver,[1,1,1],[50,50,50],[1,1,1],win)
		elif k=="d":
			parallel(ver,[1,1,2],[300,0,0],[1,1,2],win)
		elif k=="t":
			parallel(ver,[6,4,3],[300,0,0],[6,4,3],win)
		elif k=="c":
			parallel(ver,[3,4,5],[0,0,0],[0,0,1],win)
		elif k=="C":
			parallel(ver,[3,4,10],[0,0,0],[0,0,1],win)
		elif k=="e":
			win.close()
			break

if __name__=='__main__':
    main()