#!/usr/bin/env python
import os
'''
The above line tells the operating system how to deal with the file when it 
is executed
'''
'''
Cgi is sending 200 OK, then lets you put any headers you want on the socket.
'''
print "Content-Type: text/html"
print
print "<pre>"
for key, value in os.environ.items():
    print key
    print "\t", value
