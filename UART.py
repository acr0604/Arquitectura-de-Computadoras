import serial
s = serial.Serial('/dev/ttyACM0',9600)

while True:
	print(s.readline().decode().strip())
