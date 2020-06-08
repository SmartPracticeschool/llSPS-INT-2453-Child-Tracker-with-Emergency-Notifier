import time
import sys
import ibmiotf.application
import ibmiotf.device

#Provide your IBM Watson Device Credentials
organization = "1tjvme" # repalce it with organization ID
deviceType ="abcd" #replace it with device type
deviceId = "1002" #repalce with device id
authMethod = "token"
authToken = "1234567890"#repalce with token

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)        
        if cmd.data['command']=='lighton':
                print("LIGHT ON")
        elif cmd.data['command'] == 'lightoff':
            print("LIGHT OFF")
                
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()

while True:
        L1=19.1712;
        L2=83.4163;
        #Send Latitude & Longitude to IBM Watson
        data = {'d':{ 'lat' : L1, 'lon': L2}}
        #print data
        def myOnPublishCallback():
            print ("Published Latitude = %s C" % L1, "Longitude = %s %%" % L2, "to IBM Watson")

        success = deviceCli.publishEvent("event", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(1)
        
        deviceCli.commandCallback = myCommandCallback

        

# Disconnect the device and application from the cloud
deviceCli.disconnect()
