#!/usr/bin/python


print ("Hello, Python!")

#import cookielib
from requests import Request, Session

s = Session()

#Create a CookieJar object to hold the cookies
cj = cookielib.CookieJar()

#Create an opener to open pages using the http protocol and to process cookies.
opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())

response = opener.open('http://google.com/') # <---
response.read()

#Check out the cookies
print ("the cookies are: ")
for cookie in cj:
    print (cookie)

if __name__ == "__main__":
    try :
        hello()
    except Exception as excp:
        print ("Error:\n" + str(excp.args))
