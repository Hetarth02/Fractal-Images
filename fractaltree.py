from turtle import *
shape("turtle")
left(90)
speed(0)
def tree(size, level, angle):
	if level == 0:
		return
	forward(size)
	left(angle)
	tree(size * 0.8, level - 1, angle)
	right(angle * 2)
	tree(size * 0.8, level - 1, angle)
	left(angle)
	backward(size)
tree(100, 8, 40)
mainloop()