import urllib.request, urllib.error, urllib.parse
import sys
import os
import time
import urllib.request, urllib.parse, urllib.error
import math
import multiprocessing
from multiprocessing import Process, Lock, Queue

import random


def CheckProxy(address, targets):
    for t in targets:
        proxy=urllib.request.ProxyHandler({'http': address})
        opener=urllib.request.build_opener(proxy)
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36')]
        try:
            start = time.clock()
            data = opener.open(url = t, timeout = 5).read().decode()
            end = time.clock()
            print("[Proxy {0}]: OK for", t, "in time: {1} s".format(address, end - start))
        except Exception as e:
            print("[Proxy {0}]: not available".format(address))


if __name__ == '__main__':
    
    
    #user defined variables
    
    maxProc = 5
    proxyList = ['http://120.203.214.187:9090', 'http://120.198.230.27:80', 'http://61.163.236.153:9999', 'http://221.122.72.172:3128', 'http://111.1.36.26:85', 'http://111.1.36.166:84', 'http://114.113.221.166:9999']
    targets = ["http://www.baidu.com"]
    
    q = Queue()
    
    for i in proxyList:
        q.put(i)
    
    
    start = time.clock()
    
    while not q.empty():
        p = Process(target=CheckProxy, args=(q.get(), targets))
        p.start()  
        
        if len(multiprocessing.active_children()) > maxProc:
            print('active_children: ', multiprocessing.active_children())
            p.join()
        
    while len(multiprocessing.active_children()) > 0:
        time.sleep(3)
    end = time.clock()
    print("total time:", end - start, "s")
