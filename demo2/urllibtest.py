
from urllib import request

resp=request.urlopen("http://www.baidu.com")

print(resp.read().decode('utf-8'))






