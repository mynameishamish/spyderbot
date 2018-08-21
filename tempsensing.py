
import time
import threading
# from motions import *
from Adafruit_IO import Client, Feed

timeout = 6

ADAFRUIT_IO_KEY = os.environ.get('adafruit_io_key')
ADAFRUIT_IO_USERNAME = 'mynameishamish'

# Dashboard URL: https://io.adafruit.com/mynameishamish/dashboards/spyderbot

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

m1temp_feed = aio.feeds('spyderbot.base')
m2temp_feed = aio.feeds('spyderbot.head')
m3temp_feed = aio.feeds('spyderbot.neck')

def temp():
    while True:
        # print("temp")
        m1temp = robot.m1.present_temperature
        m2temp = robot.m2.present_temperature
        m3temp = robot.m3.present_temperature
        if m1temp is not None and m2temp is not None:
            print('m1Temp={0:0.1f}*C m2Temp={1:0.1f}*C m3Temp={2:0.1f}*C'.format(m1temp, m2temp, m3temp))
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


# t = threading.Timer(.5, temp)
# t.start()
#
# while True:
#     print("loop")
#     time.sleep(1)
