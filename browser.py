#!/usr/bin/env python
import os
'''
The above line tells the operating system how to deal with the file when it 
is executed
'''
'''
Cgi is sending 200 OK, then lets you put any headers you want on the socket.
'''
user_agent = os.environ['HTTP_USER_AGENT']
print "Content-Type: text/html"
print

if 'Chrome' in user_agent:
    print 'You\'re using Chrome'
elif 'Firefox' in user_agent:
    print 'You\'re using Firefox'
else:
    print "Who knows man, who knows"
