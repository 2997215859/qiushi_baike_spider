# coding:utf-8
import urllib2
from bs4 import BeautifulSoup
url_base = "http://www.qiushibaike.com/hot/"
max_page = 5
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
fout = open('spider_bs/output.html', 'w')
fout.write("<html>")
fout.write("<body>")
for page_num in range(1, max_page + 1):
    if page_num == 1:
        url = url_base
    else:
        url = url_base + "page/" + str(page_num) + "/?s=4936502"

    try:
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request)
    except urllib2.URLError, e:
        if hasattr(e, 'code'):
            print e.code
        if hasattr(e, 'reason'):
            print e.reason

    html_cont = response.read()
    soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
    para_nodes = soup.find_all('div',class_ = 'article block untagged mb15')
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
    for para_node in para_nodes:
        count = count + 1
        # print para_node
        author = para_node.find('h2').get_text()
        content = para_node.find('div', class_='content').find('span').get_text()
        vote = para_node.find('span', class_='stats-vote').find('i').get_text()
        comment = para_node.find('span', class_='stats-comments').find('i').get_text()
        print count, author, content, vote, comment
        fout.write("<td>%d</td>" % count)
        fout.write("<td>%s</td>" % author.encode('utf-8'))
        fout.write("<td>%s</td>" % content.encode('utf-8'))
        fout.write("<td>%s</td>" % vote.encode('utf-8'))
        fout.write("<td>%s</td>" % comment.encode('utf-8'))
        fout.write("</tr>")
fout.write("</body>")
fout.write("</html>")
fout.close()