def scienc_to_list(row):
    return [row.id, row.code, row.name, row.profile, row.studyforms, row.opis_obraz, row.uch_plan, row.annot_link, row.calend_link, row.norm_doc, row.inf_pract, row.inf_isp]


def scienc_format():
    return ['id', 'code', 'name', 'profile', 'studyforms', 'opis_obraz', 'uch_plan', 'annot_link', 'calend_link', 'norm_doc', 'inf_pract', 'inf_isp']


@csrf_exempt
def sciencs(request):
    if request.method == 'GET':
        a = Sciences.objects.all()
        a = [scienc_to_list(item) for item in a]
        return JsonResponse({
            'format': scienc_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def sciencsFormat(request):
    if request.method == 'GET':
        return JsonResponse(scienc_format(), safe=False)


@csrf_exempt
def sciencs_by_id(request, id):
    if request.method == 'DELETE':
        obj = Sciences.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Sciences(
            code=req_json['code'],
            name=req_json['name'],
            profile=req_json['profile'],
            studyforms=req_json['studyforms'],
            opis_obraz=req_json['opis_obraz'],
            uch_plan=req_json['uch_plan'],
            annot_link=req_json['annot_link'],
            calend_link=req_json['calend_link'],
            norm_doc=req_json['norm_doc'],
            inf_pract=req_json['inf_pract'],
            inf_isp=req_json['inf_isp'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Sciences.objects.get(id=id)
        obj = Sciences(
            id=int(id),
            code=req_json['code'],
            name=req_json['name'],
            profile=req_json['profile'],
            studyforms=req_json['studyforms'],
            opis_obraz=req_json['opis_obraz'],
            uch_plan=req_json['uch_plan'],
            annot_link=req_json['annot_link'],
            calend_link=req_json['calend_link'],
            norm_doc=req_json['norm_doc'],
            inf_pract=req_json['inf_pract'],
            inf_isp=req_json['inf_isp'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


scienc_info_replace_map = {
    'td': {
        'eduCode': lambda obj: obj[0],
        'eduName': lambda obj: obj[1],
        'eduLevel': lambda obj: obj[2],
        'eduForm': lambda obj: obj[3],
        'eduEl': lambda obj: obj[10],
    }
}


scienc_info_replace_links_map = {
    'td': {
        'opMain': lambda obj: obj[4],
        'educationPlan': lambda obj: obj[5],
        'educationAnnotation': lambda obj: obj[6],
        'educationShedule': lambda obj: obj[7],
        'methodology': lambda obj: obj[8],
        'eduPr': lambda obj: obj[9],
    }
}

scienc_info_row_template = \
    '<tr itemprop="eduAdOp">' \
    '<td itemprop="eduCode"></td>' \
    '<td itemprop="eduName"></td>' \
    '<td itemprop="eduLevel"></td>' \
    '<td itemprop="eduForm"></td>' \
    '<td itemprop="opMain"><a href="" download="">Положение</a></td>' \
    '<td itemprop="educationPlan"><a href="">Ссылка</a></td>' \
    '<td itemprop="educationAnnotation"><a href="">Ссылка</a></td>' \
    '<td itemprop="educationShedule"><a href="">Ссылка</a></td>' \
    '<td itemprop="methodology"><a href="">Ссылка</a></td>' \
    '<td itemprop="eduPr"><a href="" download="">Положение</a></td>' \
    '<td itemprop="eduEl"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def sciencs_publish(request):
    if request.method == 'GET':
        sciencs_information = Sciences.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/education/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "sciences"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'eduAdOp'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(sciencs_information):
            values = scienc_to_list(item)[1:]
            row = bs4.BeautifulSoup(scienc_info_row_template)
            replace_page_elements(scienc_info_replace_map, row, values)
            replace_page_links(scienc_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_sciencormation_replace_map, page_parser, sciencormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")