from bs4 import BeautifulSoup
import lxml
import string
import sys
import requests
import requests.packages.urllib3.util.ssl_
import re
import os
import time
import datetime
import signal


def signal_handler(signal, frame):
    global interrupted
    interrupted = True

signal.signal(signal.SIGINT, signal_handler)

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

link = "https://www.douyu.com/73665"  # bear
link1 = "https://www.douyu.com/67373" # chenyifaer
link2 = "https://www.douyu.com/17732" # tara
link3 = "https://www.douyu.com/71415" # yinzi

interrupted = False

while(1):
	try:
		res = requests.get(link)
		soup = BeautifulSoup(res.text,'lxml')
		form = soup.find_all("script")[3]
		show_status = re.search('\"show_status\":[0-9]', form.text).group(0).split(":")[1]
		show_status_val = int(show_status)
		print(show_status_val)
		while(show_status_val == 1):
			print(datetime.datetime.now())
			os.system('say "party time"')
			time.sleep(2)
			if interrupted:
				print "Leaving... "
				sys.exit()

	except requests.exceptions.RequestException:
		print("Connection Error. ")

	time.sleep(10)
	if interrupted:
		print "Leaving... "
		sys.exit()

