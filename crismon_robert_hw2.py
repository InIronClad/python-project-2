#Assignment: (Homework 2)  
#Description: (Drawing shapes using turtle graphics)  
#Author: (Robert Wayne Crismon) 
# 
#Completion Time: (2-3 hours)  
#In completing this program, I obtained help or worked with the following: 
#(Paige Danielson, tutorialspoint.com/python/var.isalpha) 

#importing turtle
import turtle

#open and read the file
input_file = open("movements.txt", "r")
lines = input_file.readlines()
#close out file
input_file.close()

#start for loop
for line in lines:
	#remove whitespace
	line = line.strip()
	#if loops to determine and save direction
	if line == 'F':
		direction = line
	elif line == 'B':
		direction = line
	elif line == 'L':
		direction = line
	elif line == 'R':
		direction = line
		#else loop to save integer
	else:
		distance = int(line)
		#start for turtle drawing
		if direction == "F":
			turtle.forward(distance)
		elif direction == "B":
			turtle.backward(distance)
		elif direction == "L":
			turtle.left(distance)
		elif direction == "R":
			turtle.right(distance)
			#end loop, program