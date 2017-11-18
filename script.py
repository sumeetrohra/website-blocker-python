import time
from datetime import datetime as dt

hostsTemp="hosts"
hostsPath="C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect="127.0.0.1"
websiteList=["www.facebook.com","facebook.com","amazon.in","www.amazon.in"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        with open(hostsPath,'r+') as file:
            content=file.read()
            for website in websiteList:
                if website in content:
                    pass
                else:
                    file.write("\n"+redirect+" "+website)
            #print("done")
    else:
        with open(hostsPath,'r') as file:
            content=file.readlines()
        
        with open(hostsPath,'w') as file:
            for line in content:
                if not any(website in line for website in websiteList):
                    file.write(line)
        #print("free...")
    time.sleep(5)
