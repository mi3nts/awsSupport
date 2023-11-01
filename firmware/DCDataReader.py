

# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
 
import paho.mqtt.client as mqtt
import ast
import datetime
import yaml
import collections
import json
import ssl
from mintsXU4 import mintsSensorReader as mSR
from mintsXU4 import mintsDefinitions as mD
from mintsXU4 import mintsLatest as mL
import sys
import pandas as pd

mqttPort              = mD.mqttPortDC
mqttBroker            = mD.mqttBrokerDC
mqttCredentialsFile   = mD.credentials
tlsCert               = mD.tlsCert
nodeInfo              = mD.nodeInfo
sensorInfo            = mD.sensorInfo
credentials           = mD.credentials

connected             = False  # Stores the connection status
broker                = mqttBroker  
port                  = mqttPort  # Secure port
mqttUN                = credentials['mqtt']['username'] 
mqttPW                = credentials['mqtt']['password'] 

nodeIDs               = nodeInfo['mac_address']
print(nodeIDs)

sensorIDs             = sensorInfo['sensorID']
print(sensorIDs)

decoder = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)




# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    for nodeID in nodeIDs:
        for sensorID in sensorIDs:
            topic = nodeID+"/"+ sensorID
            client.subscribe(topic)
            print("Subscrbing to Topic: "+ topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print()
    print(" - - - MINTS DATA RECEIVED - - - ")
    print()
    try:
        [nodeID,sensorID ] = msg.topic.split('/')
        sensorDictionary = decoder.decode(msg.payload.decode("utf-8","ignore"))
        print("Node ID   :" + nodeID)
        print("Sensor ID :" + sensorID)
        print("Data      : " + str(sensorDictionary))
        clientAWS.publish("mintsThings/"+nodeID+"/"+sensorID,payload=json.dumps(sensorDictionary), qos=0, retain=False)
        # At this point --> Publish into 

    except Exception as e:
        print("[ERROR] Could not publish data, error: {}".format(e))


# AWS MQTT Client details 
def on_connect_aws(client, userdata, flags, rc):
    print("Connected with AWS - result code "+str(rc))
    
clientAWS = mqtt.Client()
clientAWS.on_connect = on_connect_aws
clientAWS.tls_set(ca_certs='mintsXU4/credentials/AmazonRootCA1.pem', certfile='mintsXU4/credentials/aws-certificate.pem.crt', keyfile='mintsXU4/credentials/aws-private.pem.key', tls_version=ssl.PROTOCOL_SSLv23)
clientAWS.tls_insecure_set(True)
clientAWS.connect("a1sy4v3syxrxsq-ats.iot.us-east-1.amazonaws.com", 8883, 60) #Taken from REST API endpoint - Use your own. 


# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(mqttUN,mqttPW)

client.tls_set(ca_certs=tlsCert, certfile=None,
                            keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
                            tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)


client.tls_insecure_set(True)
client.connect(broker, port, 60)
client.loop_forever()


