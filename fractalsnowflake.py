from turtle import *
shape("turtle")
left(90)
speed(0)
def snowflake_side(size, level):
	if level == 0:
		forward(size)
		return
	size = size / 3
	snowflake_side(size, level - 1)
	left(60)
	snowflake_side(size, level - 1)
	right(120)
	snowflake_side(size, level - 1)
	left(60)
	snowflake_side(size, level - 1)
def create_snowflake(length, sides):
	for i in range(sides):
		snowflake_side(length, sides)
		right(360 / sides)
create_snowflake(200, 3)
mainloop()