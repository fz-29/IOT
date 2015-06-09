import time
import serialio as ser
ser.open_port("COM3")
ctr=1
while True:
	ser.output(6,True)
	ser.output(7,False)
	time.sleep(1)
	ser.output(6,False)
	ser.output(7,True)
	time.sleep(1)
	print ctr
	ctr=ctr+1


import time
import serialio as ser
ser.open_port("COM3")
ctr=0
while True:
		
	ser.output(6,True) #S1,S4 -> ON 
	ser.output(7,False) #S2,S3 -> OFF, both the commands make only one motor run clockwise
	time.sleep(1)
	#STOP THE CURRENT
	ser.output(6,False)
	ser.output(7,False)
	time.sleep(0.5)
	
	#Reverse THE DIRECTION
	#ser.output(6,False)
	ser.output(7,True)
	time.sleep(1)
	print ctr
	ctr=ctr+1