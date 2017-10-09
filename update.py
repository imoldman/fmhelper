import re
import requests
from lxml import etree
from bs4 import BeautifulSoup


def get_full_summary_html_from_web_page(url):
    # get html
    session = requests.session()
    session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    html = session.get(url).text

    # parse html, get summary
    doc = BeautifulSoup(html)
    summary = doc.find('div', attrs={'class':'rich_intro'}).find('article')

    # remove all property (like style class) in summary
    for t in summary.recursiveChildGenerator():
        t.attrs = None

    # to string
    result = ''.join([str(x) for x in summary.children])

    # detect all http(s) to link
    return re.sub('http[s]?://(?:[^ ()])+', '<a href="\g<0>">\g<0></a>', result)

print(get_full_summary_html_from_web_page("http://www.ximalaya.com/75325738/sound/53762268/"))