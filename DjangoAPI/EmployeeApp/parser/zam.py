def standartCopiestwo_to_list(row):
    return [row.id, row.name, row.filename]


def standartCopiestwo_format():
    return ['id', 'name', 'filename']


def standartCopiestwo_format_types():
    return ['text', 'text', 'file']


@csrf_exempt
def standartCopiestwos(request):
    if request.method == 'GET':
        a = standartCopiestwos.objects.all()
        a = [standartCopiestwo_to_list(item) for item in a]
        return JsonResponse({
            'format': standartCopiestwo_format(),
            'types': standartCopiestwo_format_types(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def standartCopiestwosFormat(request):
    if request.method == 'GET':
        return JsonResponse({
            "format": standartCopiestwo_format(),
            "types": standartCopiestwo_format_types(),
        }, safe=False)


@csrf_exempt
def standartCopiestwos_by_id(request, id):
    if request.method == 'DELETE':
        obj = standartCopiestwos.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = standartCopiestwos(
            name=req_json['name'],
            filename=req_json['filename'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = standartCopiestwos.objects.get(id=id)
        obj = standartCopiestwos(
            id=int(id),
            name=req_json['name'],
            filename=req_json['filename'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


standartCopiestwo_info_replace_map = {
    'td': {
        'name': lambda obj: obj[0],
    }
}


standartCopiestwo_info_replace_files_map = {
    'td': {
        'file': lambda obj: obj[1],
    }
}

standartCopiestwo_info_row_template = \
    '<tr itemprop="eduFedDoc">' \
    '<td itemprop="name"></td>' \
    '<td itemprop="file"><a href="" download="">Положение</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def standartCopiestwos_publish(request):
    if request.method == 'GET':
        standartCopiestwos_information = standartCopiestwos.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/eduStandarts/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "eduFgos"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'eduFedDoc'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(standartCopiestwos_information):
            values = standartCopiestwo_to_list(item)[1:]
            row = bs4.BeautifulSoup(standartCopiestwo_info_row_template)
            replace_page_elements(standartCopiestwo_info_replace_map, row, values)
            replace_page_files(standartCopiestwo_info_replace_files_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")