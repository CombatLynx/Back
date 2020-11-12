import bs4

with open("index.php", "r", encoding="utf-8") as f:
    contents = f.read()

if __name__ == '__main__':
    soup = bs4.BeautifulSoup(contents, 'lxml')
    soup.find_all('td', {'itemprop': 'email'})[0].string = "000000000000"
    print(str(soup))
