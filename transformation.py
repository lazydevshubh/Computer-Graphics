from line import bresenham as l
from start import setaxis
from graphics import *
from polygon import polygon
import math

ver=[]
def translation(ver,x,y,win):
    input()
    polygon(ver,win,color_rgb(240,240,240))
    setaxis(win)
    #print(ver)
    for i in range(len(ver)):
        ver[i].append(1)
    #print(ver)
    trans=[[1,0,0],[0,1,0],[-x,-y,1]]
    result = [[int(sum(a * b for a, b in zip(A_row, B_col))) for B_col in zip(*trans)] for A_row in ver]
    #print(result)
    for i in range(len(result)):
        result[i]=result[i][:2]
    #print(result)
    polygon(result,win,'green')
    return result
def doRotation(ver,x,y,angle,win):
    angle=(math.pi*angle/180)
    rot=[[math.cos(angle),math.sin(angle),0],[-math.sin(angle),math.cos(angle),0],[0,0,1]]
    input()
    polygon(ver,win,color_rgb(240,240,240))
    setaxis(win)
    for i in range(len(ver)):
        ver[i].append(1)
    result = [[int(sum(a * b for a, b in zip(A_row, B_col))) for B_col in zip(*rot)] for A_row in ver]
    #print(result)
    for i in range(len(result)):
        result[i]=result[i][:2]
    #print(result)
    polygon(result,win,'green')
    return result

def rotation(ver,x,y,angle,win):
    ver=translation(ver,x,y,win)
    result=doRotation(ver,x,y,angle,win)
    ver=translation(result,-x,-y,win)
    return ver

def doScale(ver,x,y,sx,sy,win):
    scal=[[sx,0,0],[0,sy,0],[0,0,1]]
    input()
    polygon(ver,win,color_rgb(240,240,240))
    setaxis(win)
    for i in range(len(ver)):
        ver[i].append(1)
    result = [[int(sum(a * b for a, b in zip(A_row, B_col))) for B_col in zip(*scal)] for A_row in ver]
    #print(result)
    for i in range(len(result)):
        result[i]=result[i][:2]
    #print(result)
    polygon(result,win,'green')
    return result

def scale(ver,x,y,sx,sy,win):
    ver=translation(ver,x,y,win)
    result=doScale(ver,x,y,sx,sy,win)
    ver=translation(result,-x,-y,win)
    return ver

def reflection(ver,x,y,angle,win):
    ver=translation(ver,x,y,win)
    ver=doRotation(ver,x,y,angle,win)
    ref=[[-1,0,0],[0,1,0],[0,0,1]]
    input()
    polygon(ver,win,color_rgb(240,240,240))
    setaxis(win)
    for i in range(len(ver)):
        ver[i].append(1)
    result = [[int(sum(a * b for a, b in zip(A_row, B_col))) for B_col in zip(*ref)] for A_row in ver]
    #print(result)
    for i in range(len(result)):
        result[i]=result[i][:2]
    #print(result)
    polygon(result,win,'green')
    ver=doRotation(result,x,y,-angle,win)
    ver=translation(ver,-x,-y,win)
    return ver
def shearX(ver,shx,win):
    shrx=[[1,0,0],[shx,1,0],[0,0,1]]
    input()
    polygon(ver,win,color_rgb(240,240,240))
    setaxis(win)
    #print(ver)
    for i in range(len(ver)):
        ver[i].append(1)
    #print(ver)
    result = [[int(sum(a * b for a, b in zip(A_row, B_col))) for B_col in zip(*shrx)] for A_row in ver]
    #print(result)
    for i in range(len(result)):
        result[i]=result[i][:2]
    #print(result)
    polygon(result,win,'green')
    return result

def shearY(ver,shy,win):
    shry=[[1,shy,0],[0,1,0],[0,0,1]]
    input()
    polygon(ver,win,color_rgb(240,240,240))
    setaxis(win)
    #print(ver)
    for i in range(len(ver)):
        ver[i].append(1)
    #print(ver)
    result = [[int(sum(a * b for a, b in zip(A_row, B_col))) for B_col in zip(*shry)] for A_row in ver]
    #print(result)
    for i in range(len(result)):
        result[i]=result[i][:2]
    #print(result)
    polygon(result,win,'green')
    return result


def main():
    win=GraphWin('line',400,400)
    setaxis(win)
    n=int(input('no of vertices'))
    ver=[]
    for i in range(n):
        x,y=map(int,input().split())
        ver+=[[x,y]]
    #print(ver)
    polygon(ver,win,'green')
    print("1:translation 2: rotation 3: scale")
    print("4: reflection 5:shear in X 6: shear in Y")
    while(1):
        flag=int(input("Enter the number"))
        if(flag==1):
            par=list(map(int,input("Enter Point x y").split()))
            ver=translation(ver,*par,win)
        elif flag==2:
            par=list(map(int,input("Enter Point x y and angle").split()))
            ver=rotation(ver,*par,win)
        elif flag==3:
            par=list(map(int,input("Enter Point x y and sx sy").split()))
            ver=scale(ver,*par,win)
        elif(flag==4):
            par=list(map(int,input("Enter Point x y and angle of line from y").split()))
            ver=reflection(ver,*par,win)
        elif(flag==5):
            par=list(map(int,input("Enter shx").split()))
            ver=shearX(ver,*par,win)
        elif(flag==6):
            par=list(map(int,input("Enter shy").split()))
            ver=shearY(ver,*par,win)
        else:
            break
    input("exit")
    

if __name__=='__main__':
    main()