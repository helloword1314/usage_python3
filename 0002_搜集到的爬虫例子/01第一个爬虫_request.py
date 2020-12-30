import urllib
import urllib.request
import re

res = urllib.request.urlopen('http://www.yuqiaochuang.com/tags')  
html = res.read().decode() 
print(html)
#print html
#m = re.findall(r'title="全文">(.*?)</a>', html)
#m = re.findall(r'title="全文">(.*)</a>', html, re.S)
#m = re.findall(r'title="全文">(.*?)</a>', html)
#m = re.findall(r'<div class="title">.*?title="全文">(.*?)</a>', html, re.S)
m = re.findall(r"<div>(.*)</div>", "<div>hello</div>", html, re.S)
for t in m:
    print(t)