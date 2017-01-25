import datetime
import time
from sense_emu import SenseHat

sense=SenseHat()

while True:
	zeit=str(datetime.datetime.time(datetime.datetime.now()))
	
	h=int(float(zeit[0]))*10 + int(float(zeit[1]))
	if(h>12):
		h=h-12
	
	m=int(float(zeit[3]))*10 + int(float(zeit[4]))
	
	hb=[0,0,0,0]
	mb=[0,0,0,0,0,0]
	
	sense.clear()
	index=3
	while(index>=0):
		hb[index]=h%2
		h=h/2
		sense.set_pixel(7-(3-index), 2, 255*hb[index], 255*hb[index], 255*hb[index])
		index=index-1
	
	index=5
	while(index>=0):
		mb[index]=m%2
		m=m/2
		sense.set_pixel(7-(5-index), 5, 255*mb[index], 255*mb[index], 255*mb[index])
		index=index-1
	
	print(hb, mb)
	

	
	time.sleep(0.3)
	
