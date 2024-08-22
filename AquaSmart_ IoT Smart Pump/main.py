import machine
import usocket as socket
import time
import network


timeout = 0 # WiFi Connection Timeout variable 
# Restarting WiFi
wifi = network.WLAN(network.AP_IF)
wifi.active(True)

wifi.config(essid = 'AquaSmart:IoT_Smart_Pump',password = '12345678KTSC',authmode = network.AUTH_WPA_WPA2_PSK)
print(wifi.ifconfig())

    
# HTML Document

html='''<!DOCTYPE html>
<html lang="en">
<head>
  
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <title>Powered by ASIDDAU ALAL KUFFAR</title>


<style>
.l2 {
  background-color: white; 
  color: black; 
  border: 6px solid #008CBA;

  background-color: white; /* Green */
  border: none;
  color: black;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  border-radius: 30%;
  transition-duration: 0.4s;
  cursor: pointer;

  
}

.l2:hover {
  background-color: #008CBA;
  color: white;
}


body{
  background-color: skyblue;
}

</style>
  
</head>
<body>


<center><h2 class="b2" > AquaSmart: IoT Smart Pump Webserver  </h2></center>
<form>
<center>
  <h3> Water Pump Auto Start & Stop </h3>
  <button class="l2" name="WPASS" value='ONOFF' type='submit'>  Auto Start & Stop </button>
  <h3> WATER_PUMP </h3>
  <button class="l2" name="PUMP" value='ON' type='submit'>  ON </button>
  <button class="l2" name="PUMP" value='OFF' type='submit'> OFF </button>


<h3 class="ktsc">Powered by ASIDDAU ALAL KUFFAR / IT</h3>



</center>
  
</body>
</html>
'''

# Output Pin DeclarationPUMP = machine.Pin(2,machine.Pin.OUT)
PUMP = machine.Pin(15,machine.Pin.OUT)
PUMP.value(1)

# Initialising Socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET - Internet Socket, SOCK_STREAM - TCP protocol

Host = '' # Empty means, it will allow all IP address to connect
Port = 80 # HTTP port
s.bind((Host,Port)) # Host,Port

s.listen(5) # It will handle maximum 5 clients at a time

# main loop
while True:
  connection_socket,address=s.accept() # Storing Conn_socket & address of new client connected
  print("Got a connection from ", address)
  request=connection_socket.recv(1024) # Storing Response coming from client
  print("Content ", request) # Printing Response 
  request=str(request) # Coverting Bytes to String
  # Comparing & Finding Postion of word in String 
  PUMP_ON =request.find('/?PUMP=ON')
  PUMP_OFF =request.find('/?PUMP=OFF')
  PUMP_ONOFF =request.find('/?WPASS=ONOFF')

  if(PUMP_ON==6):
    PUMP.value(0)
    
  if(PUMP_OFF==6):
    PUMP.value(1)
  
  if(PUMP_ONOFF==6):
    PUMP.value(0)
    time.sleep(5)
    PUMP.value(1)
    
  # Sending HTML document in response everytime to all connected clients  
  response=html 
  connection_socket.send(response)
  
  #Closing the socket
  connection_socket.close() 

