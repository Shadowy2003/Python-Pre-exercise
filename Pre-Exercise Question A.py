#    Pre-exercise Question A
#    The _requests_ module is an HTTP client library for sending HTTP requests in Python.

#    Open the address below on your browser, and once it has loaded, observe the web page, and do nothing:

#    https://w3schools.com/python/demopage.htm

#    Now on your computer, using the requests module, write a code that gets and prints the HTML source code of the above web page from the Internet.


import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)
