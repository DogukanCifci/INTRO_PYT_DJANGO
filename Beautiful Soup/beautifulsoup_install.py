from cgitb import html
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


"""
1-Web sitesine baglan
2- Kaynak kodunu al
3- BS modülü ile html kodlarini parcala
"""

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE







