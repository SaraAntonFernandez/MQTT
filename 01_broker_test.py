from paho.mqtt.client import Client

def on_message(mqtt, userdata, msg):
	print("MESSAGE:", userdata, msg.topic, msq.qos, msg.payload, msg.retain)
	mqttc.publish('clients/test', msg.payload)
	
def main(broker, topic):
	mqttc  = Client()
	mqttc.on_message = on_message
	mqttc.connected(broker)
	mqttc.subscribe(topic)
	mqttc.loop_forever()
	
if __name__ =="__main__":
	import sys
	if len(sys.argv)<3:
		print(f"Usage: {sys.argv[0]} broker topic")
		sys.exit(1)
	broker = sys.argv[1]
	topic = sys.argv[2]
	main(broker, topic)