# ФИНАНСОВО-ХОЗЯЙСТВЕННАЯ ДЕЯТЕЛЬНОСТЬ
# ------------------------- ОБЪЕМ ОБРАЗОВАТЕЛЬНОЙ ДЕЯТЕЛЬНОСТИ ---------------------------------

def rush_to_list(row):
    return [row.id, row.federal, row.sub, row.place, row.fis]


def rush_format():
    return ['id', 'federal', 'sub', 'place', 'fis']


@csrf_exempt
def rushs(request):
    if request.method == 'GET':
        a = rushs.objects.all()
        a = [rush_to_list(item) for item in a]
        return JsonResponse({
            'format': rush_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def rushsFormat(request):
    if request.method == 'GET':
        return JsonResponse(rush_format(), safe=False)


@csrf_exempt
def rushs_by_id(request, id):
    if request.method == 'DELETE':
        obj = rushs.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = rushs(
            federal=req_json['federal'],
            sub=req_json['sub'],
            place=req_json['place'],
            fis=req_json['fis'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = rushs.objects.get(id=id)
        obj = rushs(
            id=int(id),
            federal=req_json['federal'],
            sub=req_json['sub'],
            place=req_json['place'],
            fis=req_json['fis'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


rush_info_replace_map = {
    'td': {
        'finBFrush': lambda obj: obj[0],
        'finBRrush': lambda obj: obj[1],
        'finBMrush': lambda obj: obj[2],
        'finPrush': lambda obj: obj[3],
    }
}

# rush_info_replace_links_map = {
#     'td': {
#         'finYear': lambda obj: obj[4],
#         'finPost': lambda obj: obj[5],
#         'finRas': lambda obj: obj[6],
#     }
# }

rush_info_row_template = \
    '<tr itemprop="vol">' \
    '<td itemprop="finBFrush"></td>' \
    '<td itemprop="finBRrush"></td>' \
    '<td itemprop="finBMrush"></td>' \
    '<td itemprop="finPrush"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def rushs_publish(request):
    if request.method == 'GET':
        rushs_information = rushs.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/budget/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "rushs"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'vol'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(rushs_information):
            values = rush_to_list(item)[1:]
            row = bs4.BeautifulSoup(rush_info_row_template)
            replace_page_elements(rush_info_replace_map, row, values)
            # replace_page_links(rush_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")
