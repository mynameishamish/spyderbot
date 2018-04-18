# from selenium import webdriver
# import time
 
# # options = webdriver.ChromeOptions()
# # options.add_argument('--ignore-certificate-errors')
# # options.add_argument("--test-type")
# # # options.binary_location = "/usr/local/bin/chromedriver"
# # options.binary_location = "/usr/local/bin/chromium"
# # driver = webdriver.Chrome(chrome_options=options)
# # # driver.get('https://python.org')
# # from pyvirtualdisplay import Display
# # from selenium import webdriver

# # display = Display(visible=0, size=(1024, 768))
# # display.start()

# # driver = webdriver.Firefox()
# # driver.get('http://raspberrypi.stackexchange.com/')
# # driver.quit()

# # display.stop()
# driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')  # Optional argument, if not specified will search path.
# driver.get('http://www.google.com/xhtml');
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()

import subprocess
import time
import threading
import sys

import subprocess
import time
p = subprocess.Popen(
['DISPLAY=:0 chromium-browser tv.giphy.com/whatever'])
p.communicate()

time.sleep(1)
print (p.pid)
p.kill()

def display():
	os.system("DISPLAY=:0 chromium-browser tv.giphy.com/whatever")
	time.sleep(2)
	sys.exit()
# display()
# print("hello you")

