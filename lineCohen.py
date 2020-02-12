from line import bresenham as l
from polygon import polygon
from start import setaxis
from graphics import *

"""
-100 -100
100 100
-150 -150
150 150
"""
def code_for(x,y,x_min,y_min,x_max,y_max):
	code = 0 
	if x < x_min:      # left 
		code |= 1 
	elif x > x_max:    # right 
		code |= 2 
	if y < y_min:      # below  
		code |= 4 
	elif y > y_max:    # above
		code |= 8 
	return code 

def Clip(x1, y1, x2, y2,x_min,y_min,x_max,y_max): 
    code1 = code_for(x1, y1,x_min,y_min,x_max,y_max) 
    code2 = code_for(x2, y2,x_min,y_min,x_max,y_max) 
    accept = False
    while True: 
        if code1 == 0 and code2 == 0: 
            accept = True
            break
        elif (code1 & code2) != 0: 
            break
        else: 
            x = 1.0
            y = 1.0
            if code1 != 0: 
                code_out = code1 
            else: 
                code_out = code2 
            if code_out & 8: 
                x=x1+(x2-x1)*(y_max-y1)/(y2-y1) 
                y =y_max 
  
            elif code_out & 4: 
                x =x1+(x2-x1)*(y_min-y1)/(y2-y1) 
                y = y_min 
  
            elif code_out & 2: 
                y=y1+(y2-y1)*(x_max-x1)/(x2-x1) 
                x=x_max 
  
            elif code_out & 1: 
                y=y1+(y2-y1)*(x_min-x1)/(x2-x1) 
                x=x_min 
            if code_out == code1: 
                x1=x 
                y1=y 
                code1 =code_for(x1,y1,x_min,y_min,x_max,y_max) 
  
            else: 
                x2=x 
                y2=y 
                code2 = code_for(x2, y2,x_min,y_min,x_max,y_max) 
  
    if accept:
    	return  [int(x1),int(y1),int(x2),int(y2)]
    else: 
        [x1, y1, x2, y2]
        
        
def main():
    win=GraphWin('line',400,400)
    setaxis(win)
    bxmin,bymin=map(int,input("enter the lower vertex").split())
    bxmax,bymax=map(int,input("enter the upper vertex").split())
    x1,y1=map(int,input("Enter the first vertex").split())
    x2,y2=map(int,input("Enter the second vertex").split())
    l(x1,y1,x2,y2,win,'red')
    l(*Clip(bxmin,bymin,bxmax,bymax,x1,y1,x2,y2),win,'blue')
    polygon([(bxmin,bymin),(bxmax,bymin),(bxmax,bymax),(bxmin,bymax)],win,'green')  
    input("exit")
    
if __name__=='__main__':
	main()
