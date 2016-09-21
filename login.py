#!/usr/bin/env python
import os
import sys
import cgi
import secret
import cgitb
cgitb.enable()

method = os.environ['REQUEST_METHOD']

form = cgi.FieldStorage()

print "Content-Type: text/html"

if method == 'POST':
    username = form.getfirst('username')
    password = form.getfirst('password')

    if username == secret.username and password == secret.password:
        print "Set-Cookie: auth=YouAndMe"
        
        print
        print "<h1>Welcome back</h1>"
    else:
        print
        print "<h1>Error! Invalid user name or password</h1>"
        print "<h1>You don't even go here</h1>"
else:
    raw_cookie = os.getenv('HTTP_COOKIE', '') or '='
    key, cookie = raw_cookie.split('=')

    if cookie == 'YouAndMe':
        print
        print "<h1>Welcome back</h1>"

print
print '<form method="POST">'
print 'Username: <input name="username">'
print '<br>'
print 'Password: <input type="password"'
print 'name="password">'
print '<br>'
print '<button type="submit">Login</button>'
print '</form>'
