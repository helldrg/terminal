
import serial


serialPort = serial.Serial(port = "COM6", baudrate = 115200, bytesize = 8, timeout = 2, stopbits = serial.STOPBITS_ONE)
serialString = ""

while(1):
    if(serialPort.in_waiting > 0):
        serialString = serialPort.readline()
        print(serialString.decode('Ascii'))
        
        # The b at the beginning is used to indicate bytes!
        #serialPort.write(b"Success")