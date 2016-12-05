# coding:utf8
import urllib
import urllib2
import re

url = "http://www.qiushibaike.com/hot/"
try:
    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print e.code
    if hasattr(e, 'reason'):
        print e.reason

# target: author, date, content, vote-num
content = response.read().decode('utf-8')
#pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
#                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
# pattern = re.compile('<div.*?author.*?title.*?<h2>(.*?)</h2>.*?'+
#                      'content.*?<span>(.*?)</span>.*?'+
#                      'status.*?status-vote.*?number">(.*?)</i>', re.S)
# 获取非匿名用户
pattern = re.compile('<div.*?author.*?title.*?<h2>(.*?)</h2>.*?'+
                     '<div.*?content.*?<span>(.*?)</span>.*?'+
                     '<div.*?stats.*?<span.*?stats-vote.*?<i.*?number">(.*?)</i>.*?'+
                     '<span.*?stats-comments.*?<a.*?qiushi_comments.*?<i.*?number">(.*?)</i>', re.S)

# 爬取匿名用户
# pattern = re.compile('<div.*?author.*?<span>*?<h2>(.*?)</h2>.*?'+
                     # '<div.*?content.*?<span>(.*?)</span>', re.S)
items = re.findall(pattern,content)
# print items
count = 0
fout = open('output.html', 'w')
fout.write("<html>")
fout.write("<body>")
fout.write("<table>")
fout.write("<tr>")
fout.write("<td>序号</td>")
fout.write("<td>内容</td>")
fout.write("<td>赞数</td>")
fout.write("<td>评论数</td>")
fout.write("</tr>")
for item in items:
    fout.write("<tr>")
    count = count + 1
    print count, item[0], item[1], item[2], item[3]
    fout.write("<td>%d</td>" % count)
    fout.write("<td>%s</td>" % item[1].encode('utf-8'))
    fout.write("<td>%s</td>" % item[2].encode('utf-8'))
    fout.write("<td>%s</td>" % item[3].encode('utf-8'))
    fout.write("</tr>")

fout.write("</table>")
fout.write("</body>")
fout.write("</html>")
fout.close()
