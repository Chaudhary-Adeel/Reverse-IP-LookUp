#!/usr/bin/env python

# The MIT License (MIT)

# Copyright (c) 2014 Muhammad Adeel

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import urllib, urllib2, json, sys, os

if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')

class Coloring:
	def __init__(self):
		self.green = "\033[92m"
		self.bold = "\033[1m"
		self.red = "\033[91m"
		self.die = "\033[0m"

COLOR = Coloring()

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("Domains.log", "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

sys.stdout = Logger()

def banner():
	print COLOR.bold + COLOR.green + '''
______                            ___________ 
| ___ \                          |_   _| ___ /
| |_/ /_____   _____ _ __ ___  ___ | | | |_/ /
|    // _ \ \ / / _ \ '__/ __|/ _ \| | |  __/ 
| |\ \  __/\ V /  __/ |  \__ \  __/| |_| |    
\_| \_\___| \_/ \___|_|  |___/\___\___/\_|    
=================================================
# Author: Muhammad Adeel                        #
# Blog: http://urdusecurity.blogspot.com        #
# Mail: Chaudhary1337@gmail.com                 #
=================================================\n''' + COLOR.die

url = "http://domains.yougetsignal.com/domains.php"
useragent = "Mozilla/5.0 (X11; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0 Iceweasel/22.0"
contenttype = "application/x-www-form-urlencoded; charset=UTF-8"
banner()
target = raw_input('Enter IP or Domain: ')
if target.startswith('http'):
	print COLOR.bold + "\n[!] Enter URL Like This: " + COLOR.die + COLOR.green +"google.com" + COLOR.die
	sys.exit()


def GetDetails():
	postdata = [('remoteAddress',target),('key','')]
	postdata = urllib.urlencode(postdata)
	request = urllib2.Request(url, postdata)
	request.add_header("Content-type", contenttype)
	request.add_header("User-Agent", useragent)
	try:
		result = urllib2.urlopen(request).read()
	except urllib2.HTTPError, e:
		print COLOR.bold + "[-] Error: " + e.code
	obj = json.loads(result)
	return obj

def Result(object):
	print COLOR.green + "\n[+] Total Domains Hosted: " + COLOR.die + object["domainCount"]
	print COLOR.green + "[+] Target Domain :    " + COLOR.die + object["remoteAddress"]
	print COLOR.green + "[+] Target IP: " + COLOR.die + object["remoteIpAddress"]
	print '\n'
	for domains, hl in object["domainArray"]:
		print COLOR.bold + domains + COLOR.die
	print COLOR.bold + "\n[+] Check Domains.log For Domains List.\n" + COLOR.die

var = GetDetails()
Result(var)

def main():
	if __name__ == '__main__':
		main()
