
from urllib.request import urlopen       # 引入urlopen 模块
from urllib.request import Request       # 引入urlrequest 模块
from urllib import parse                 # 引入parse 模块

req=Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")

postDate = parse.urlencode([
    ("StartStation", "2f940836-cedc-41ef-8e28-c2336ac8fe68"),
    ("EndStation", "977abb69-413a-4ccf-a109-0272c24fd490"),
    ("SearchDate", "2016/08/31"),
    ("SearchTime", "21:30"),
    ("SearchWay", "DepartureInMandarin")

])
req.add_header("Origin", "http://www.thsrc.com.tw")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; rv:48.0) Gecko/20100101 Firefox/48.0)")
resp = urlopen(req,data=postDate.encode("utf-8"))

print(resp.read().decode("utf-8"))




