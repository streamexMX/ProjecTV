#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import random

servers = ['213.152.180.151:1935','179.43.158.195:1935','179.43.158.196:1935',
           '179.43.158.197:1935','179.43.158.198:1935','179.43.158.199:1935','179.43.158.200:1935',
           '179.43.158.201:1935','179.43.158.203:1935','179.43.158.202:1935',
           '199.195.195.100:1935','173.192.81.169:1935','199.189.105.12:1935',
           '206.190.129.4:1935','199.195.194.244:1935','199.195.195.20:1935','146.185.25.162:1935',
           '146.185.25.186:1935','46.28.49.36:1935','37.130.227.140:1935','146.185.25.130:1935',
           '199.195.195.76:1935','199.195.194.220:1935']

 
def get():
    return random.choice(servers)