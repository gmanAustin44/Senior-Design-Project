#import////////////////////////////////
import RPi.GPIO as GPIO
import time
import sys
#import Temperature
#setup/////////////////////////////////
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

#flow sensor start
#GPIO.setmode(GPIO.BOARD)
#inpt = 5    						#Pin Number
GPIO.setup(5, GPIO.IN)
rate_cnt = 0 						#Pulses Per time unit
tot_cnt  = 0 						#Total Pulses from start
minutes  = 0						#Time passed in minutes
constant_3V = 1.6036/(10^7)			#Conversion Ratio based on pump
time_new = 0.0

print('Water Flow - Aproximate')
print('Control C to exit')
#flow sensor stop

#functions////////////////////////////
    #Functions to start components
    #start pump 1
def test():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    #GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
def pump_1_start():
    GPIO.output(26, GPIO.HIGH)
    #stop pump 1
def pump_1_stop():
    GPIO.output(26, GPIO.LOW)
    #start pump 2
#def pump_2_start():
    #GPIO.output(5, GPIO.HIGH)
    #stop pump 2
#def pump_2_stop():
    #GPIO.output(5, GPIO.LOW)
    #start actuator A
def actuator_A_start():
    GPIO.output(19, GPIO.HIGH)
    #stop actuator A
def actuator_A_stop():
    GPIO.output(19, GPIO.LOW)
    #start actuator B
def actuator_B_start():
    GPIO.output(13, GPIO.HIGH)
    #stop actuator B
def actuator_B_stop():
    GPIO.output(13, GPIO.LOW)
    #start actuator C
def actuator_C_start():
    GPIO.output(6, GPIO.HIGH)
    #stop actuator C
def actuator_C_stop():
    GPIO.output(6, GPIO.LOW)
    #Functions for loops
#Function is desiging to start the operation cycle
    #note change the numbers in the sleep timer
    #function to change the duration ofthe pump activation
def operation_loop():
    #tempfile = open("/sys/bus/w1/devices/28-01205bda3750/w1_slave")
    #temptext = tempfile.read()
    #tempfile.close()
    #tempcelsius2 = temptext.split("\n")[1]. split(" ")[9]
    #temperature2 = float(tempcelsius2[2:])
    #temperature2 = temperature2 / 1000
    #print( "Sensor 2")
   # print( temperature2)
    #ceiling = 70
    #if temperature2 > ceiling:
       # print( "Sensor 2")
      #  print( "Testing Steam Line")
     #   print( "temp too High")
    #    actuator_A_start()
    #    time.sleep(3)
      #  actuator_A_stop()
    #else:
      #  print( "temp too low")
    #print( "outside of If statement")
    #actuator_B_start()
    #actuator_A_start()
    #pump_1_start()
   # time.sleep(3)
    pump_1_start()
    #time.sleep(3)
    #pump_1_stop()
    #time.sleep(3)
   # actuator_A_stop()
    #actuator_B_stop()
    
#Function is desiging to fill heat exchanger
    #note change the numbers in the sleep timer
    #function to change the duration ofthe pump activation
def prefill_():
    #actuator_B_start()
    actuator_A_start()
    time.sleep(3)
    pump_1_start()
    time.sleep(3)
    pump_1_stop()
    time.sleep(3)
    actuator_A_stop()
   
    #actuator_B_stop()
#sensors
def Fsensor_1():
    rate_cnt = 0 						#Pulses Per time unit
    tot_cnt  = 0 						#Total Pulses from start
    minutes  = 0						#Time passed in minutes
    constant_3V = 1.6036/(10^7)			#Conversion Ratio based on pump
    time_new = 0.0
    while True:							#Loop forever
	    time_new = time.time() + 10		#+60 = 1 minute
	    rate_cnt = 0
	    count = 0						#Count used for limiting "try" output
	    while time.time() <= time_new:	#Run for time increment in Line 24
		    count += 1
		    if count==10001:			#Reset Count for "try"
			    count=0
		    if GPIO.input(5)!=0:		#Look for pulses
			    rate_cnt += 1
			    tot_cnt  += 1
		    try:
			    if count==10000:		#"try" output every 10,000th time
				    print(GPIO.input(5), end='')		#Status indicator
				    #THIS PRINT STATEMENT WILL OUTPUT CONSTANTLY. It will
				    #output 0s if the propeller is stopped and 1 if it is
				    #moving
				    #True
		    except KeyboardInterrupt:	#Look for exit command
			    print('\nCTRL C - Exiting nicely')
			    GPIO.cleanup()
			    sys.exit()
	    minutes += 1/6
	    print('\nPulses / 10 sec', round(rate_cnt, 4))
	    print('Total Pulses', round(tot_cnt, 4))
	    print('\nGallons / 10 sec', round(rate_cnt*constant_3V, 4))
	    print('\nGallons / min', round(rate_cnt*constant_3V*6, 4))	
	    print('Total Gallons', round(tot_cnt*constant_3V, 4))
	    print('Time (min & clock) ', minutes, '\t', time.asctime(time.localtime(time.time())),'\n')
	    
   
#def Tsensor_1():
    #tempfile = open("/sys/bus/w1/devices/28-9736841e64ff/w1_slave")
    #temptext = tempfile.read()
    #tempfile.close()
    #tempcelsius1 = temptext.split("\n")[1]. split(" ")[9]
    #temperature1 = float(tempcelsius1[2:])
    #temperature1 = temperature1 / 1000
    #print( "Sensor 1 ")
    #print( temperature1 )
    #time.sleep(1)
#def Tsensor_2():
    #tempfile = open("/sys/bus/w1/devices/28-01205bda3750/w1_slave")
    #temptext = tempfile.read()
    #tempfile.close()
    #tempcelsius2 = temptext.split("\n")[1]. split(" ")[9]
    #temperature2 = float(tempcelsius2[2:])
    #temperature2 = temperature2 / 1000
    #print( "Sensor 2")
    #print( temperature2)    
#Function is desiging to fill heat exchanger
    #note change the numbers in the sleep timer
    #function to change the duration ofthe pump activation
def cleaning_():
    actuator_B_start()
    actuator_A_stop()
    #actuator_A_start()
    time.sleep(3)
    pump_2_start()
    #pump_1_start()
    time.sleep(3)
    pump_2_stop()
    time.sleep(3)
    
   
    actuator_B_stop()

#loop
def Operation_cycle():   
    while True:
        operation_loop()
        Fsensor_1() 
        #input_response = input("continue loop?")
        #continue_response = True
        #if input_response == 'n':
            #continue_response = False
            #break;
def Prefill_cycle():   
    while True:
        prefill_() 
        input_response = input("continue loop?")
        continue_response = True
        if input_response == 'n':
            continue_response = False
            break;
def Cleaning_cycle():   
    while True:
        cleaning_() 
        input_response = input("continue loop?")
        continue_response = True
        if input_response == 'n':
            continue_response = False
            break;
#def System_check():

#menu function        
def menu_():
    print("Menu:")
    print("1: Operation Cycle")
    print("2: Prefill:")
    print("3: Cleaning Cycle")
    print("4: System check")
    input_response_choose_cycle = input("Please choose cycle ")
    if input_response_choose_cycle =="1": 
        Operation_cycle() 
    elif input_response_choose_cycle =="2": 
        Prefill_cycle()
         
    elif input_response_choose_cycle =="3": 
        Cleaning_cycle()
        
    elif input_response_choose_cycle == "4": 
        System_check() 

    else: 
        menu_()
         
#//////////////////////////
#body
while True:
    test()
    #Tsensor_1()
    #Tsensor_2()
    menu_()
    print("Loop Terminated, Returning to menu")
    GPIO.cleanup()    

