# ----------------- МАТЕРИАЛЬНО-ТЕХНИЧЕСКОЕ ОБЕСПЕЧЕНИЕ И ОСНАЩЁННОСТЬ ОБРАЗОВАТЕЛЬНОГО ПРОЦЕССА ----------------------
# Наличие собственных электронных образовательных и информационных ресурсов

def seven_to_list(row):
    return [row.id, row.name, row.link]


def seven_format():
    return ['id', 'name', 'link']


@csrf_exempt
def sevens(request):
    if request.method == 'GET':
        a = TableSeven.objects.all()
        a = [seven_to_list(item) for item in a]
        return JsonResponse({
            'format': seven_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def sevensFormat(request):
    if request.method == 'GET':
        return JsonResponse(seven_format(), safe=False)


@csrf_exempt
def sevens_by_id(request, id):
    if request.method == 'DELETE':
        obj = TableSeven.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = TableSeven(
            name=req_json['name'],
            link=req_json['link'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = TableSeven.objects.get(id=id)
        obj = TableSeven(
            id=int(id),
            name=req_json['name'],
            link=req_json['link'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


seven_info_replace_map = {
    'td': {
        'name': lambda obj: obj[0],
    }
}


seven_info_replace_links_map = {
    'td': {
         'eoisOwn': lambda obj: obj[1],
    }
}

seven_info_row_template = \
    '<tr itemprop="own">' \
    '<td itemprop="name"></td>' \
    '<td itemprop="eoisOwn"><a href=" "></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def sevens_publish(request):
    if request.method == 'GET':
        sevens_information = TableSeven.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/objects/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "own"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'own'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(sevens_information):
            values = seven_to_list(item)[1:]
            row = bs4.BeautifulSoup(seven_info_row_template)
            replace_page_elements(seven_info_replace_map, row, values)
            replace_page_links(seven_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_sevenormation_replace_map, page_parser, sevenormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")