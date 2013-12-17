'''
Created on 2013-12-2

@author: ray
'''
#!/usr/bin/env python
#-*- coding:utf-8 -*-
 
import httplib, urllib, re, urllib2
import socket
import time
import json

params = dict(
login_email="hisen@xx.com", # replace with your email
login_password="pwd", # replace with your password
format="json",
domain_id=100, # replace with your domain_od, can get it by API Domain.List
record_id=100, # replace with your record_id, can get it by API Record.List
sub_domain="pi", # replace with your sub_domain
record_line="默认",
)
current_ip = None

def ddns(ip):
    params.update(dict(value=ip))
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}
    conn = httplib.HTTPSConnection("dnsapi.cn")
    conn.request("POST", "/Record.Ddns", urllib.urlencode(params), headers)

    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    print data
    conn.close()
    return response.status == 200
'''
class Getmyip:
    def getip(self):
        try:
            myip = self.visit("http://www.ip138.com/ip2city.asp")
        except:
            try:
                myip = self.visit("http://www.bliao.com/ip.phtml")
            except:
                try:
                    myip = self.visit("http://www.whereismyip.com/")
                except:
                    myip = "So sorry!!!"
        return myip
    def visit(self,url):
        opener = urllib2.urlopen(url)
        if url == opener.geturl():
            str = opener.read()
        return re.search('\d+\.\d+\.\d+\.\d+',str).group(0)
'''

def getip():
    #getmyip = Getmyip()
    #ip = getmyip.getip()
    
    
    url="http://iframe.ip138.com/ic.asp"
    content=urllib2.urlopen(url).read()
    begain=content.find('[')
    end=content.find(']')
    ip=content[begain+1:end]
    return ip


if __name__ == '__main__':
    while True:
        try:
            ip = getip()
            print ip
            if current_ip != ip:
                if ddns(ip):
                    current_ip = ip
        except Exception, e:
            print e
            pass
        time.sleep(30)
