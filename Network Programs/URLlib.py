# Urlib is a package that collects several modules for working with URLs.
# The two main modules are urllib.request and urllib.error.
# The urllib.request module is used to open and read URLs.
# The urllib.error module contains the exceptions raised by urllib.request.
# The urllib.parse module is used to parse URLs.


import urllib
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
