__author__ = 'asus'

from urllib.request import urlopen

html=urlopen("https://en.wikipedia.org/robots.txt")

print(html.read().decode("utf-8"))










