#!/usr/bin/env python3

import paho.mqtt.client as mqtt 
import time
import random
import json
from datetime import datetime
from PIL import Image
import glob
import os, os.path
import numpy as np

from video_writer import create_video
from upload_to_s3 import upload_to_s3

def onDisconnect(client, userdata, rc):
  print("disonnected")

def onConnect(client, userdata, flags, rc):
  print("connected")
  # QOS quality of service 2
  mqttc.subscribe("classification/error",2)
  
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    unknown_class = -1
    msg = json.loads(msg.payload)
    path = '../images/'
    if unknown_class == msg["vehicule"] or msg["probability"] < 0.7:
        print("The confidance level of the classification is low")
        image_list = []
        print(msg["datetime"])
        images = glob.glob(path+'*.jpg')
        images = np.sort(images)
        # we could simply send the last image but we have to check when the classification error occur
        image_list = images[-5:]
        create_video(image_list, msg["datetime"])
        upload_to_s3('../videos/' + msg["datetime"] + '.mp4',msg["vehicule"])
        print(image_list)
       
 
mqttc=mqtt.Client("client")
mqttc.on_connect = onConnect
mqttc.on_disconnect = onDisconnect
mqttc.on_message = on_message
mqttc.connect("127.0.0.1", port=1883, keepalive=60)

mqttc.loop_forever()

