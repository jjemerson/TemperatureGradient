#/usr/bin/python
# Simple demo of reading each analog input from the ADS1x15 and printing it to
# the screen.
# Author: Tony DiCola
# License: Public Domain
# Altered by J.J. Emerson to collect data for "Hidden genetic variation shapes the structure of functional elements in Drosophila".
# Code changes retain Public Domain license.
from datetime import datetime
import time
import sys
sys.stdout.flush()

# Import the ADS1x15 module.
import Adafruit_ADS1x15


# Create an ADS1115 ADC (16-bit) instance.
adcs = [
	Adafruit_ADS1x15.ADS1115(busnum=1, address=0x48),
	Adafruit_ADS1x15.ADS1115(busnum=1, address=0x49),
	Adafruit_ADS1x15.ADS1115(busnum=1, address=0x4a)
	]

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 2

# Main loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*(len(adcs)*4)
    for i in range(len(adcs)):
	for j in range(4):
        # Read the specified ADC channel using the previously set gain value.
	        values[i*4+j] = adcs[i].read_adc(j, gain=GAIN)
        # Note you can also pass in an optional data_rate parameter that controls
        # the ADC conversion time (in samples/second). Each chip has a different
        # set of allowed data rate values, see datasheet Table 9 config register
        # DR bit values.

        # Each value will be a 12 or 16 bit signed integer value depending on the
        # ADC (ADS1015 = 12-bit, ADS1115 = 16-bit).
    # Print the ADC values.
    print datetime.now().time(), "\t".join(map(str,values))
    time.sleep(0.01)
