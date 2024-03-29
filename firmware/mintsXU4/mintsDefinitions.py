
from getmac import get_mac_address
import serial.tools.list_ports
import yaml
import pandas as pd
# Change Accordingly  
mintsDefinitions          = yaml.load(open('mintsXU4/credentials/mintsDefinitions.yaml'),Loader=yaml.FullLoader)
# dataFolder                = mintsDefinitions['dataFolder']
# dataFolderReference       = mintsDefinitions['dataFolder'] + "/reference"
# dataFolderMQTTReference   = mintsDefinitions['dataFolder'] + "/referenceMqtt"  # The path of your MQTT Reference Data 
# dataFolderMQTT            = mintsDefinitions['dataFolder'] + "/rawMqtt"        # The path of your MQTT Raw Data 
tlsCert                   = mintsDefinitions['tlsCert']     # The path of your TLS cert

# latestOn                  = False

# mqttOn                    = True

credentialsFile           = 'mintsXU4/credentials/credentials.yaml'
credentials               = yaml.load(open(credentialsFile))

# sensorInfoFile            = 'mintsXU4/credentials/sensorIDs.yml'
sensorInfo                  = pd.read_csv('https://raw.githubusercontent.com/mi3nts/AirQualityAnalysisWorkflows/main/influxdb/nodered-docker/sensorIDs.csv')
print("Sensor Info: " + str(sensorInfo))

portInfo                  = pd.read_csv('https://raw.githubusercontent.com/mi3nts/AirQualityAnalysisWorkflows/main/influxdb/nodered-docker/portIDs.csv')
print("Port Info: " + str(portInfo))

nodeInfo                  = pd.read_csv('https://raw.githubusercontent.com/mi3nts/AirQualityAnalysisWorkflows/main/influxdb/nodered-docker/id_lookup.csv')
print("Node Info: " + str(nodeInfo))

# Add in AWS MQTT Credentials 
mqttBrokerDC              = "mqtt.circ.utdallas.edu"
mqttBrokerLoRa            = "mqtt.lora.trecis.cloud"

mqttPortDC                = 8883  # Secure port
mqttPortLoRa              = 1883  # Secure port

print()
print("----- AWS Support -----")
