"""
'temp_humidity.py'
==================================
Example of sending analog sensor
values to an Adafruit IO feed.

Author(s): Brent Rubell

Tutorial Link: Tutorial Link: https://learn.adafruit.com/adafruit-io-basics-temperature-and-humidity

Dependencies:
    - Adafruit IO Python Client
        (https://github.com/adafruit/io-client-python)
    - Adafruit_Python_DHT
        (https://github.com/adafruit/Adafruit_Python_DHT)
"""

# import standard python modules.
import time
import threading

# import adafruit dht library.
# import Adafruit_DHT

from motions import *

# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed

# Delay in-between sensor readings, in seconds.
timeout = 6

# Pin connected to DHT22 data pin

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = '557c9dd075064cda8cb642a1c84399ec'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username).
ADAFRUIT_IO_USERNAME = 'mynameishamish'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Set up Adafruit IO Feeds.
m1temp_feed = aio.feeds('spyderbot.base')
m2temp_feed = aio.feeds('spyderbot.head')
m3temp_feed = aio.feeds('spyderbot.neck')


# Set up DHT22 Sensor.
# dht22_sensor = Adafruit_DHT.DHT22

def temp():
    while True:
        m1temp = robot.m1.present_temperature
        m2temp = robot.m2.present_temperature
        m3temp = robot.m3.present_temperature
        if m1temp is not None and m2temp is not None:
            print('m1Temp={0:0.1f}*C m2Temp={1:0.1f}*C m3Temp={1:0.1f}*C'.format(m1temp, m2temp, m3temp))
            # Send humidity and temperature feeds to Adafruit IO
            m1temp = '%.2f'%(m1temp)
            m2temp = '%.2f'%(m2temp)
            m3temp = '%.2f'%(m3temp)

            aio.send(m1temp_feed.key, str(m1temp))
            aio.send(m2temp_feed.key, str(m2temp))
            aio.send(m3temp_feed.key, str(m3temp))
        # else:
        #     print('Failed to get DHT22 Reading, trying again in ', DHT_READ_TIMEOUT, 'seconds')
        # Timeout to avoid flooding Adafruit IO
        time.sleep(timeout)


t = threading.Timer(6.0, temp)
t.start()
