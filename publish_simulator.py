#!/usr/bin/env python3

import paho.mqtt.client as mqtt 
import time
import random
import json
from datetime import datetime

def onDisconnect(client, userdata, rc):
  print("disonnected")

def onConnect(client, userdata, flags, rc):
  print("connected")

mqttc=mqtt.Client("simulator")
mqttc.on_connect = onConnect
mqttc.on_disconnect = onDisconnect
mqttc.connect("127.0.0.1", port=1883, keepalive=60)
mqttc.loop_start()
while True:

  class_sim = random.randint(-1, 4)
  
  message = {}
  message["vehicule"] = class_sim
  message["datetime"] = datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
  message["probability"] = random.uniform(0.5, 1.)

  mqttc.publish("classification/error", json.dumps(message))
  print("data send: ", message)
  time.sleep(3)