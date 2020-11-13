import bs4

basic_information_replace_map = {
    'td': {
        'regDate': lambda obj: obj.BIregDate,
        'address': lambda obj: obj.BIaddress,
        'workTime': lambda obj: obj.BIworkTime,
        'telephone': lambda obj: obj.BItelephone,
        'fax': lambda obj: obj.BIfaxes,
        'email': lambda obj: obj.BIemail,
        'addressPlace': lambda obj: obj.BIaddressPlace
    }
}


def read_page(filename):
    with open(filename, "r") as f:
        content = f.read()
        return bs4.BeautifulSoup(content, 'lxml')


def write_page(filename, page):
    with open(filename, "w") as f:
        print(page, file=f)


def replace_page_elements(replace_map, parser, obj):
    f = bs4.BeautifulSoup(obj, 'lxml')
    for tag, parameters in obj.items():
        for name, getter in parameters:
            tags = f.find_all(tag, {'itemprop': name})
            if len(tags) == 1:
                tags[0].string = getter(obj)
            else:
                pass
    return str(parser)
