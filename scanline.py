from line import bresenham as l
from start import setaxis
from graphics import *
from polygon import polygon
import math

def fill(edge_table,y_min,y_max,win):
    active_edge = []
    for curr_y in range(y_min,y_max+1):
        i=0
        while i<len(active_edge):
            if active_edge[i][2]==curr_y:
                active_edge.pop(i)
            else:
                i+=1
        for e in range(len(active_edge)):
            if e%2: 
                active_edge[e][1]+=active_edge[e][3]
                active_edge[e][0]=math.floor(active_edge[e][1])
            else:	 
                active_edge[e][1]+=active_edge[e][3]
                active_edge[e][0]=math.ceil(active_edge[e][1])
        if curr_y in edge_table:
            active_edge+=edge_table[curr_y]
        active_edge.sort()
        for cur in range(0,len(active_edge)-1,2):
            #print(active_edge)
            for x in range(active_edge[cur][0],active_edge[cur+1][0]+1):
                win.plot(x,curr_y,'green')
def main():
    win=GraphWin('line',400,400)
    setaxis(win)
    n=int(input('no of vertices'))
    ver=[]
    ymax=-10000
    ymin=10000
    for i in range(n):
        x,y=map(int,input().split())
        ver+=[[x,y]]
        ymax=max(ymax,y)
        ymin=min(ymin,y)
    print(ver)
    ver+=[ver[0]]
    #polygon(ver,win,'black')
    edgeTable={}
    for i in range(n):
        x1,y1,x2,y2=*ver[i],*ver[i+1]
        if y1>y2:
            x1,y1,x2,y2=x2,y2,x1,y1
        if y1==y2:
            continue
        if x1==x2:
            slope=0
        else:
            slope=(x2-x1)/(y2-y1)
        if y1 in edgeTable:
            edgeTable[y1]+=[[x1,x1,y2,slope]]
        else:
            edgeTable[y1]=[[x1,x1,y2,slope]]
    print(edgeTable)
    fill(edgeTable,ymin,ymax,win)
    input('exit')
    
    
if __name__=='__main__':
	main()			