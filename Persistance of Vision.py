import time
import serialio as ser
ser.open_port("COM3")
ctr=0
while (ctr<40):
	ser.output(0,True);
	
	time.sleep(0.02);
	
	ser.output(0,False);
	time.sleep(0.02);
	#net time period = 0.04s and persitance of vision time = 0.03125s
	ctr=ctr+1
