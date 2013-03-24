import math

def convert(w, x, y, z) :
	dx = y-w
	dy = z-x
	xpoint = dx**2
	ypoint = dy**2
	result = math.sqrt(xpoint+ypoint)
	print result

w = input('input x1: ')
x = input('input y1: ')
y = input('input x2: ')
z = input('input y2: ')
convert(w, x, y, z)
