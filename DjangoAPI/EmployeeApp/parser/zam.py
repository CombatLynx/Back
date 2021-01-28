# ------------------------- ПЛАТНЫЕ ОБРАЗОВАТЕЛЬНЫЕ УСЛУГИ 1 ---------------------------------

def plat_to_list(row):
    return [row.id, row.info]


def plat_format():
    return ['id', 'info']


def plat_format_types():
    return ['text', 'file']


@csrf_exempt
def plats(request):
    if request.method == 'GET':
        a = Plats.objects.all()
        a = [plat_to_list(item) for item in a]
        return JsonResponse({
            'format': plat_format(),
            'types': plat_format_types(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def platsFormat(request):
    if request.method == 'GET':
        return JsonResponse({
            "format": plat_format(),
            "types": plat_format_types(),
        }, safe=False)


@csrf_exempt
def plats_by_id(request, id):
    if request.method == 'DELETE':
        obj = Plats.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Plats(
            info=req_json['info'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Plats.objects.get(id=id)
        obj = Plats(
            id=int(id),
            info=req_json['info'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


# plat_info_replace_map = {
#     'td': {
#         'name': lambda obj: obj[0],
#         'fio': lambda obj: obj[1],
#         'post': lambda obj: obj[2],
#         'addressStr': lambda obj: obj[3],
#         # 'site': lambda obj: obj[4],
#         'email': lambda obj: obj[5],
#         # 'divisionClauseDocLink': lambda obj: obj[6],
#     }
# }

plat_info_replace_files_map = {
    'td': {
        'paids': lambda obj: obj[0],
    }
}

plat_info_row_template = \
    '<tr itemprop="paidEdu">' \
    '<td itemprop="paids"><a href="" download="">Ссылка</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def plats_publish(request):
    if request.method == 'GET':
        plats_information = Plats.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/paid_edu/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "paidsss"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'paidEdu'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(plats_information):
            values = plat_to_list(item)[1:]
            row = bs4.BeautifulSoup(plat_info_row_template)
            # replace_page_elements(plat_info_replace_map, row, values)
            # replace_page_links(plat_info_replace_links_map, row, values)
            replace_page_files(plat_info_replace_files_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")