import bs4

html_text = '<html><title>QWE</title><body><div id="1">qqqq</div></body>'

if __name__ == '__main__':
    p = bs4.BeautifulSoup(html_text, 'lxml')
    p.find_all('div', {'id': '1'})[0].string = "123123123"
    print(str(p))