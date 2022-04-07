from paho.mqtt.client import Client
from multiprocessing import Process, Manager
from time import sleep
import random

NUMBERS = 'numbers'
CLIENTS = 'clients'
TIMER_STOP = f'{CLIENTS}/timerstop'
HUMIDITY = humidity

def is_prime(n):
	i=2
	while i*i < n and n%i !=0:
		i+=1
	return i*i > n

def timer(time, data):
	mqttc = Client()
	mqttc.connect(data['broker'])
	msg = f'timer working.timeout: {time}'
	print(msg)
	mqtt.publish(TIMER_STOP, msg)
	sleep(time)
	msg = f'timer working.timeout: {time}'
	mqtt.publish(TIMER_STOP, msg)
	print('timer and working')
	mqtt.disconnect()
	
def on_message(mqttc, data, msg):
	print(f'MESSAGE: data:{data}, msg.topic:{msg.topic}, payload:{msg.payload}')
	try:
		if int(msg.payload) % 2==0:
			worker = Process(target=timer, args=(random.random()*20, data))
			worker.start()
	except ValueError as e:
		print(e)
		pass
		
def on_log(mqttc, userdata, level, string):
	print('LOG', userdata, level, string)
	
def main(broker):
	data = {'client':None, 'broker':broker}
	
	mqttc  = Client(client_id = "combine_numbers", userdata=data)
	data['client'] = mqttc
	mqttc.on_message = on_message
	mqttc.connected(broker)
	mqttc.subscribe(NUMBERS)
	mqttc.loop_forever()
	
if __name__ =="__main__":
	import sys
	if len(sys.argv)<2:
		print(f"Usage: {sys.argv[0]} broker")
		sys.exit(1)
	broker = sys.argv[1]
	main(broker)
