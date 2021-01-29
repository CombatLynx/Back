# ---------------- Копия свидетельства о государственной аккредитации (с приложениями) -----------------------------

def docp_to_list(row):
    return [row.id, row.document]


def docp_format():
    return ['id', 'document']


def docp_format_types():
    return ['text', 'file']


@csrf_exempt
def docps(request):
    if request.method == 'GET':
        a = Docp.objects.all()
        a = [docp_to_list(item) for item in a]
        return JsonResponse({
            'format': docp_format(),
            'types': docp_format_types(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def docpsFormat(request):
    if request.method == 'GET':
        return JsonResponse({
            "format": docp_format(),
            "types": docp_format_types(),
        }, safe=False)


@csrf_exempt
def docps_by_id(request, id):
    if request.method == 'DELETE':
        obj = Docp.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Docp(
            document=req_json['document'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Docp.objects.get(id=id)
        obj = Docp(
            id=int(id),
            document=req_json['document'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


# docp_info_replace_map = {
#     'td': {
#         'name': lambda obj: obj[0],
#         'fio': lambda obj: obj[1],
#         'post': lambda obj: obj[2],
#         'addressStr': lambda obj: obj[3],
#         # 'site': lambda obj: obj[4],
#         'email': lambda obj: obj[5],
#         # 'divisionClauseDocpink': lambda obj: obj[6],
#     }
# }

docp_info_replace_files_map = {
    'td': {
        'ustd': lambda obj: obj[0],
    }
}

docp_info_row_temdocpe = \
    '<tr itemprop="accreditationDocpink">' \
    '<td itemprop="ustd"><a href="" download="">Ссылка</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def docps_publish(request):
    if request.method == 'GET':
        docps_information = Docp.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/document/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "ustavd"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'accreditationDocpink'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(docps_information):
            values = docp_to_list(item)[1:]
            row = bs4.BeautifulSoup(docp_info_row_temdocpe)
            # replace_page_elements(docp_info_replace_map, row, values)
            # replace_page_links(docp_info_replace_links_map, row, values)
            replace_page_files(docp_info_replace_files_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")