import time
import serialio as ser
ser.open_port("COM3")
ctr=0
while (ctr<40):
	ser.output(0,True);
	ser.output(1,False);
	time.sleep(0.0625);
	ser.output(1,True);
	ser.output(0,False);
	time.sleep(0.0625);
	ctr=ctr+1
