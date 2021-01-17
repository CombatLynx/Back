# ----------------------------------------------- ОБРАЗОВАНИЕ -----------------------------------------------------
# Информация о результатах перевода, восстановления и отчисления

def obraz_to_list(row):
    return [row.id, row.code, row.name, row.level, row.form, row.out, row.to, row.res, row.exp]


def obraz_format():
    return ['id', 'code', 'name', 'level', 'form', 'out', 'to', 'res', 'exp']


@csrf_exempt
def obrazs(request):
    if request.method == 'GET':
        a = Obrazod.objects.all()
        a = [obraz_to_list(item) for item in a]
        return JsonResponse({
            'format': obraz_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def obrazsFormat(request):
    if request.method == 'GET':
        return JsonResponse(obraz_format(), safe=False)


@csrf_exempt
def obrazs_by_id(request, id):
    if request.method == 'DELETE':
        obj = Obrazod.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Obrazod(
            code=req_json['code'],
            name=req_json['name'],
            level=req_json['level'],
            form=req_json['form'],
            out=req_json['out'],
            to=req_json['to'],
            res=req_json['res'],
            exp=req_json['exp'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Obrazod.objects.get(id=id)
        obj = Obrazod(
            id=int(id),
            code=req_json['code'],
            name=req_json['name'],
            level=req_json['level'],
            form=req_json['form'],
            out=req_json['out'],
            to=req_json['to'],
            res=req_json['res'],
            exp=req_json['exp'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


obraz_info_replace_map = {
    'td': {
        'eduCode': lambda obj: obj[0],
        'eduName': lambda obj: obj[1],
        'eduLevel': lambda obj: obj[2],
        'eduForm': lambda obj: obj[3],
        'numberOut': lambda obj: obj[4],
        'numberTo': lambda obj: obj[5],
        'numberRes': lambda obj: obj[6],
        'numberExp': lambda obj: obj[7],
    }
}


obraz_info_row_template = \
    '<tr itemprop="eduObrazod">' \
    '<td itemprop="eduCode"></td>' \
    '<td itemprop="eduName"></td>' \
    '<td itemprop="eduLevel"></td>' \
    '<td itemprop="eduForm"></td>' \
    '<td itemprop="numberOut"></td>' \
    '<td itemprop="numberTo"></td>' \
    '<td itemprop="numberRes"></td>' \
    '<td itemprop="numberExp"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def obrazs_publish(request):
    if request.method == 'GET':
        obrazs_information = Obrazod.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/education/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "obrazod"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'eduObrazod'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(obrazs_information):
            values = obraz_to_list(item)[1:]
            row = bs4.BeautifulSoup(obraz_info_row_template)
            replace_page_elements(obraz_info_replace_map, row, values)
            # replace_page_links(grant_obrazo_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_obrazormation_replace_map, page_parser, obrazormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")