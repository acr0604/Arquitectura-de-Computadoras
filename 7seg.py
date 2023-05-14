import RPi.GPIO as GPIO
import time



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT) #a		
GPIO.setup(6,GPIO.OUT)  #b
GPIO.setup(26,GPIO.OUT) #c 
GPIO.setup(16,GPIO.OUT) #d
GPIO.setup(20,GPIO.OUT) #e
GPIO.setup(21,GPIO.OUT) #f
GPIO.setup(19,GPIO.OUT) #g
GPIO.setup(12,GPIO.IN) #ascendente/descendente

def main():
	while True:
		for i in range(1,17):
			if GPIO.input(12) == GPIO.LOW:
				print(i)
				if i == 1:
					GPIO.output(13,1)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,1)
					GPIO.output(20,1)
					GPIO.output(21,1)
					GPIO.output(19,0)
				elif i == 2:
					GPIO.output(13,0)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,0)
					GPIO.output(20,0)
					GPIO.output(21,0)
					GPIO.output(19,0)
					
				elif i == 3:
					GPIO.output(13,1)
					GPIO.output(6,1)
					GPIO.output(26,0)
					GPIO.output(16,1)
					GPIO.output(20,1)
					GPIO.output(21,0)
					GPIO.output(19,1)
				elif i == 4:
					GPIO.output(13,1)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,1)
					GPIO.output(20,0)
					GPIO.output(21,0)
					GPIO.output(19,1)

				elif i == 5:
					GPIO.output(13,0)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,0)
					GPIO.output(20,0)
					GPIO.output(21,1)
					GPIO.output(19,1)

				elif i == 6:
					GPIO.output(13,1)
					GPIO.output(6,0)
					GPIO.output(26,1)
					GPIO.output(16,1)
					GPIO.output(20,0)
					GPIO.output(21,1)
					GPIO.output(19,1)
					
				elif i == 7:
					GPIO.output(13,1)
					GPIO.output(6,0)
					GPIO.output(26,1)
					GPIO.output(16,1)
					GPIO.output(20,1)
					GPIO.output(21,1)
					GPIO.output(19,1)
					
				elif i == 8:
					GPIO.output(13,1)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,0)
					GPIO.output(20,0)
					GPIO.output(21,0)
					GPIO.output(19,0)
					
				elif i == 9:
					GPIO.output(13,1)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,1)
					GPIO.output(20,1)
					GPIO.output(21,1)
					GPIO.output(19,1)
					
				elif i ==10:
					GPIO.output(13,1)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,0)
					GPIO.output(20,0)
					GPIO.output(21,1)
					GPIO.output(19,1)
					
				elif i == 11:
					GPIO.output(13,1)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,0)
					GPIO.output(20,1)
					GPIO.output(21,1)
					GPIO.output(19,1)
					
				elif i == 12:
					GPIO.output(13,0)
					GPIO.output(6,0)
					GPIO.output(26,1)
					GPIO.output(16,1)
					GPIO.output(20,1)
					GPIO.output(21,1)
					GPIO.output(19,1)
					
				elif i == 13:
					GPIO.output(13,1)
					GPIO.output(6,0)
					GPIO.output(26,0)
					GPIO.output(16,1)
					GPIO.output(20,1)
					GPIO.output(21,1)
					GPIO.output(19,0)
					
				elif i == 14:
					GPIO.output(13,0)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,1)
					GPIO.output(20,1)
					GPIO.output(21,0)
					GPIO.output(19,1)
						
				elif i == 15:
					GPIO.output(13,1)
					GPIO.output(6,0)
					GPIO.output(26,0)
					GPIO.output(16,1)
					GPIO.output(20,1)
					GPIO.output(21,1)
					GPIO.output(19,1)
					
				elif i == 16:
					GPIO.output(13,1)
					GPIO.output(6,0)
					GPIO.output(26,0)
					GPIO.output(16,0)
					GPIO.output(20,1)
					GPIO.output(21,1)
					GPIO.output(19,1)
				time.sleep(1)
			
			else:
				if i == 16:
					GPIO.output(13,1)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,1)
					GPIO.output(20,1)
					GPIO.output(21,1)
					GPIO.output(19,0)
				
				elif i == 15:
					GPIO.output(13,0)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,0)
					GPIO.output(20,0)
					GPIO.output(21,0)
					GPIO.output(19,0)
					
				elif i == 14:
					GPIO.output(13,1)
					GPIO.output(6,1)
					GPIO.output(26,0)
					GPIO.output(16,1)
					GPIO.output(20,1)
					GPIO.output(21,0)
					GPIO.output(19,1)
					
				elif i == 13:
					GPIO.output(13,1)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,1)
					GPIO.output(20,0)
					GPIO.output(21,0)
					GPIO.output(19,1)

				elif i == 12:
					GPIO.output(13,0)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,0)
					GPIO.output(20,0)
					GPIO.output(21,1)
					GPIO.output(19,1)

				elif i == 11:
					GPIO.output(13,1)
					GPIO.output(6,0)
					GPIO.output(26,1)
					GPIO.output(16,1)
					GPIO.output(20,0)
					GPIO.output(21,1)
					GPIO.output(19,1)
					
				elif i == 10:
					GPIO.output(13,1)
					GPIO.output(6,0)
					GPIO.output(26,1)
					GPIO.output(16,1)
					GPIO.output(20,1)
					GPIO.output(21,1)
					GPIO.output(19,1)
					
				elif i == 9:
					GPIO.output(13,1)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,0)
					GPIO.output(20,0)
					GPIO.output(21,0)
					GPIO.output(19,0)
					
				elif i == 8:
					GPIO.output(13,1)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,1)
					GPIO.output(20,1)
					GPIO.output(21,1)
					GPIO.output(19,1)
					
				elif i == 7:
					GPIO.output(13,1)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,0)
					GPIO.output(20,0)
					GPIO.output(21,1)
					GPIO.output(19,1)
					
				elif i == 6:
					GPIO.output(13,1)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,0)
					GPIO.output(20,1)
					GPIO.output(21,1)
					GPIO.output(19,1)
				
				elif i == 5:
					GPIO.output(13,0)
					GPIO.output(6,0)
					GPIO.output(26,1)
					GPIO.output(16,1)
					GPIO.output(20,1)
					GPIO.output(21,1)
					GPIO.output(19,1)
					
				elif i == 4:
					GPIO.output(13,1)
					GPIO.output(6,0)
					GPIO.output(26,0)
					GPIO.output(16,1)
					GPIO.output(20,1)
					GPIO.output(21,1)
					GPIO.output(19,0)
					
				elif i == 3:
					GPIO.output(13,0)
					GPIO.output(6,1)
					GPIO.output(26,1)
					GPIO.output(16,1)
					GPIO.output(20,1)
					GPIO.output(21,0)
					GPIO.output(19,1)
						
				elif i == 2:
					GPIO.output(13,1)
					GPIO.output(6,0)
					GPIO.output(26,0)
					GPIO.output(16,1)
					GPIO.output(20,1)
					GPIO.output(21,1)
					GPIO.output(19,1)
					
				elif i == 1:
					GPIO.output(13,1)
					GPIO.output(6,0)
					GPIO.output(26,0)
					GPIO.output(16,0)
					GPIO.output(20,1)
					GPIO.output(21,1)
					GPIO.output(19,1)
					
				time.sleep(1)
		
	
if __name__ == "__main__":
	main()
