from line import bresenham as l
from start import setaxis
from graphics import *
from polygon import polygon
"""
3
100 100
150 150
150 0
3
175 125
75 25
75 125
"""
def x_intersect(x1,y1,x2,y2, x3,y3,x4,y4) :

    num = (x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return num//den

def y_intersect(x1,y1,x2,y2, x3,y3,x4,y4):  
    num = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return num//den

  
def clip(poly_points, x1,y1,x2,y2): 

    new_points =[]
    for i in range(len(poly_points)):
        k = (i+1) % len(poly_points)
        ix = poly_points[i][0]
        iy = poly_points[i][1]
        kx = poly_points[k][0]
        ky = poly_points[k][1] 

        i_pos = (x2-x1) * (iy-y1) - (y2-y1) * (ix-x1); 
        k_pos = (x2-x1) * (ky-y1) - (y2-y1) * (kx-x1); 
  
        if i_pos < 0  and k_pos < 0 :
            new_points.append([kx,ky])
        elif i_pos >= 0 and k_pos < 0 :
            new_points.append([x_intersect(x1, y1, x2, y2, ix, iy, kx, ky),y_intersect(x1, y1, x2, y2, ix, iy, kx, ky)])
            new_points.append([kx,ky])
        elif i_pos < 0 and k_pos >= 0: 
            new_points.append([x_intersect(x1,y1, x2, y2, ix, iy, kx, ky),y_intersect(x1,y1, x2, y2, ix, iy, kx, ky)])
    return new_points
  
def polyClip(poly, clipper):  
    for i in range(len(clipper)):
        k = (i+1) % len(clipper) 
        poly= clip(poly, clipper[i][0],clipper[i][1], clipper[k][0], clipper[k][1]); 
    return poly


def main():
    win=GraphWin('line',400,400)
    setaxis(win)
    n=int(input("Enter thr number of vertices in polygon"))
    poly=[]
    for i in range(n):
        poly.append(list(map(int,input().split())))
    print(poly)
    m=int(input("Enter thr number of vertices in polygon_clipper"))
    clipper=[]
    for i in range(n):
        clipper.append(list(map(int,input().split())))
    clipped=polyClip(poly,clipper).copy()
    polygon(poly,win,'yellow')
    polygon(clipper,win,'red3')
    polygon(clipped,win,'black')
    input("exit")
if __name__=='__main__':
    main()