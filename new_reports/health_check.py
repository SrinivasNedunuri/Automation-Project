#!/usr/bin/env python3
# health check and trigger email if server is down
import time
import psutil
import emails

sender = 'automation@example.com'
recipient = 'student-00-ceea497b272a@example.com'
body = 'Please check your system and resolve the issue as soon as possible.'

while True:
  cpu_util = psutil.cpu_percent(interval = 2)
  if cpu_util>80:
    subject = 'Error - CPU usage is over 80%'
    message = emails.generate(sender, recipient, subject, body,None)
    emails.send(message)
  if psutil.disk_usage('/')[3]>80:
    subject = 'Error - Available disk space is less than 20%'
    message =  emails.generate(sender, recipient, subject, body,None)
    emails.send(message)
  mem = psutil.virtual_memory()
  if (mem.available) < (500*1024*1024):
    subject = 'Error - Available memory is less than 500MB'
    message =  emails.generate(sender, recipient, subject, body,None)
    emails.send(message)
  net = psutil.net_if_addrs()
  if net['lo'][0][1] != '127.0.0.1':
    subject = 'Error - localhost cannot be resolved to 127.0.0.1'
    message =  emails.generate(sender, recipient, subject, body,None)
    emails.send(message) 
  time.sleep(60)
