from ubidots import ApiClient
from gpiozero import LightSensor
import time
import datetime
import Adafruit_DHT
import smbus
import os

loop = 0
startuptime =  datetime.datetime.now()

ldr = LightSensor(4)
bus = smbus.SMBus(1)
address = 0x04

# Return CPU temperature as a character string
def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp="," ").replace("\'C\n"," "))

while True:

	loop = loop + 1
	pi_temp = int(float(getCPUtemperature()))
	luz = ldr.value * 100
	humidity, temperature = Adafruit_DHT.read_retry(11, 23)
	moist = bus.read_byte(address) 	
	moist = 127 - (moist / 2)

	print 'Loop: ', loop
	print 'Start Time: ', startuptime
	print 'RPI Temp: ', int(float(getCPUtemperature())), 'C'
	print 'Time Now: ', datetime.datetime.now()
	
	time.sleep(1)

	api = ApiClient(token='ATh21KIJr7x3CIgzx2NULvT1jWHard')

	ldr_light = api.get_variable('580527a376254277d7a3c900')
	dht11_humi = api.get_variable('58054dbc76254247d7e93a0f')
	dht11_temp = api.get_variable('58054eb87625424e72c6fac8')
	hl_69_moist = api.get_variable('5806603976254243acce3ae4')	

	new_dht11_sens_humi = dht11_humi.save_value({'value':humidity})
	new_dht11_sens_temp = dht11_temp.save_value({'value':temperature})
	new_ldr_sens = ldr_light.save_value({'value':luz })
	new_hl_69_sens_moist = hl_69_moist.save_value({'value':moist})
