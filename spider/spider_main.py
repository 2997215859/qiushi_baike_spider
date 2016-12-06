# coding:utf8
import urllib
import urllib2
import re
max_page = 5
url_base = "http://www.qiushibaike.com/hot/"
fruits = ['banana', 'apple',  'mango']
fout = open('spider/output.html', 'w')
fout.write("<html>")
fout.write("<body>")
for page_num in range(1,max_page+1):
    print page_num
    if page_num == 1:
        url = url_base
    else:
        url = url_base + "page/"+str(page_num)+"/?s=4936502"
    print url
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

    fout.write("<h3>第%s个页面</h3>" % page_num)
    fout.write("<table>")
    fout.write("<tr>")
    fout.write("<td>序号</td>")
    fout.write("<td>作者</td>")
    fout.write("<td>内容</td>")
    fout.write("<td>赞数</td>")
    fout.write("<td>评论数</td>")
    fout.write("</tr>")
    for item in items:
        fout.write("<tr>")
        count = count + 1
        print count, item[0], item[1], item[2], item[3]
        fout.write("<td>%d</td>" % count)
        fout.write("<td>%s</td>" % item[0].encode('utf-8'))
        fout.write("<td>%s</td>" % item[1].encode('utf-8'))
        fout.write("<td>%s</td>" % item[2].encode('utf-8'))
        fout.write("<td>%s</td>" % item[3].encode('utf-8'))
        fout.write("</tr>")

    fout.write("</table>")

fout.write("</body>")
fout.write("</html>")
fout.close()
