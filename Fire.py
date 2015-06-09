import serialio as ser
import time
ser.open_port("COM3")

while True:
	inp=ser.input(0)
	if inp==True :
		#ser.output(0,True)
		print "Fire!!!"
	else :
		#ser.output(0,False)
		print "Safe"