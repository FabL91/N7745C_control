import pyvisa as visa
# NOTE: the default pyvisa import works well for Python 3.6+ # if you are working with python version lower than 3.6, use 'import visa' instead of import pyvisa as visa
import time # start of Untitled

rm=visa.ResourceManager()
N7745C=rm.open_resource('TCPIP0::169.254.241.203::inst0::INSTR')


#One Shot Test
"""N7745C.write(':SENSE1:CHANnel1:Power:GAIN:AUTO %d'%(0))
N7745C.write(':SENSE1:CHANnel1:Power:RANGE:AUTO %d'%(0))
N7745C.write(':SENSE1:CHANnel1:Power:RANGE:UPPer %G'%(-10.0))
N7745C.write(':SENSE1:CHANnel1:Power:UNIT %d'%(1))
N7745C.write(':SENSE1:CHANnel1:Power:WAVelength %G NM'%(1550.0))
#N7745C.write(':SENSE1:CHANnel1:FUNCtion:PARameter:LOGGing %d,%G us'%(100 ,100.0))
N7745C.write(':SENSE1:CHANnel1:FUNCtion:PARameter:LOGGing %d,%G s'%(100 ,1.0))
#N7745C.write(':TRIGger1:CHANnel1:INPut %s'%('MMEasure'))
N7745C.write(':SENSE1:CHANnel1:FUNCtion:LOOP%d'%(0))
temp_values=N7745C.query_ascii_values(':SENSE1:CHANnel1:FUNCtion:RESult:INDex?')
loops=int(temp_values[0])
N7745C.write(':SENSe1:CHANnel1:FUNCtion:STATe%s,%s'%('LOGGing','STOP'))
data=N7745C.query_binary_values(':SENSE1:CHANnel1:FUNCtion:RESult:BUFA?','f',False)
print(data)"""

#Continous Shot test













N7745C.close()
rm.close()
#endofUntitled
