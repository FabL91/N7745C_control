"""test de logging sur le l'instrument keysight N7745 C"""

#from keysight_ktn7740 import *
import pyvisa as visa
# NOTE: the default pyvisa import works well for Python 3.6+ # if you are working with python version lower than 3.6, use 'import visa' instead of import pyvisa as visa
import time # start of Untitled


rm=visa.ResourceManager()
list_visa = rm.list_resources
print(list_visa)
N7745C=rm.open_resource('TCPIP0::169.254.241.203::inst0::INSTR')

print(N7745C.query("*IDN?")) #The IDeNtification query 

#N7745C.write(":SYSTem:PRESet") #Sets the insrument to its standard settings
N7745C.write(":SENSe2:CHANnel:FUNCtion:STATe LOGG,STOP") #Enables/Disables the logging, MinMax, or stability data acquisition function mode
N7745C.write(":SENSe2:CHANnel:POWer:GAIN:AUTO 0") #Set the Auto Gain
N7745C.write(":SENSe2:CHANnel:POWer:RANGe:AUTO 0") #Enables or disables automatic power ranging for the slot
N7745C.write(":SENSe2:CHANnel:POWer:RANGe:UPPer -10 DBM") #Sets the power range for the module.
N7745C.write(":SENSe2:CHANnel:POWer:UNIT 1") #Sets the sensor power unit 
N7745C.write(":SENSe2:CHANnel:POWer:WAVelength 1552NM")#Sets the sensor wavelength.
N7745C.write(":SENSe2:CHANnel:FUNCtion:PARameter:LOGGing 20,100 MS")#Sets the number of data points and the averaging time for the logging data acquisition function
N7745C.write(":TRIGger2:CHANnel:INPut IGN")#Sets the incoming trigger response and arms the slot
N7745C.write(":SENSe2:CHANnel:FUNCtion:STATe LOGG,STAR")#Enables/Disables the logging
#status = N7745C.query(":SENSe2:CHANnel:FUNCtion:STATe?")#Enables/Disables the logging
#print(status)
# Loop until status is 'LOGGING_STABILITY,COMPLETE'
def get_status():
    """Function to query the status"""
    return N7745C.query(":SENSe2:CHANnel:FUNCtion:STATe?")
status = get_status()

counter = 0 # Initialize counter for iterations

start_time = time.time() # Initialize timer

while "COMPLETE" not in status:
    
    # Increment counter
    counter += 1    
    
    time.sleep(0.25)    # Wait for a specified time before querying again (e.g., 1 second)
    # Query the status again
    status = get_status()    
    
    # Optionally, print the status to monitor the progress
    elapsed_time = time.time() - start_time
    print(f"Iteration {counter}: Current status: {status}, Time elapsed: {elapsed_time:.2f} seconds")

elapsed_time = time.time() - start_time
print(f"Status is COMPLETE. Exiting loop after {counter} iterations and {elapsed_time:.2f} seconds.")

data=N7745C.query_binary_values(':SENSE2:CHANnel:FUNCtion:RESult?','f',False)
print(data)
N7745C.close()
rm.close()










