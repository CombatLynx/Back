from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpResponseNotFound

from .models import Departments, Employees, BasicInformations, DepartmentsInformation, Subdivisions, Founders, \
    Filiations, Representations, Managements, Volumes, Vacs, Leaders, Teachers, FilialLeaders, Leaderstwo, \
    StandartCopies, PaidServices, Internationaldog, Internationalaccr, SpecCab, SpecPrac, SpecLib, SpecSport, \
    SpecMeal, SpecHealth, Ovz, LinkOvz, OvzTwo, Grants, GrantInfo, Acts, Jobs, GosAccreditations, Prof, InfChi, \
    AdmissionResults, Perevod, Obraz, Practices, ScienceResults, SvedOrg, Facilities, ObjPract, Libraries, Sports, \
    Meals, Health, TableOne, TableTwo, TableThree, TableFour, TableFive, TableSix, TableSeven

from .serializers import DepartmentSerializer, EmployeeSerializer, BasicInformationSerializer, \
    DepartmentsInformationSerializer, SubdivisionsSerializer

from django.core.files.storage import default_storage
from datetime import datetime

import bs4


# Create your views here.
@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)


@csrf_exempt
def basicInformationApi(request, id=0):
    if request.method == 'GET':
        basicInformations = BasicInformations.objects.all()
        basicInformations_serializer = BasicInformationSerializer(basicInformations, many=True)
        return JsonResponse(basicInformations_serializer.data, safe=False)

    elif request.method == 'POST':
        basicInformation_data = JSONParser().parse(request)
        basicInformation_serializer = BasicInformationSerializer(data=basicInformation_data)
        if basicInformation_serializer.is_valid():
            basicInformation_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        basicInformation_data = JSONParser().parse(request)
        basicInformation = BasicInformations.objects.get(BIid=basicInformation_data['BIid'])
        basicInformation_serializer = BasicInformationSerializer(basicInformation, data=basicInformation_data)
        if basicInformation_serializer.is_valid():
            basicInformation_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        basicInformation = BasicInformations.objects.get(BIid=id)
        basicInformation.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


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
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        return bs4.BeautifulSoup(content, 'lxml')


def write_page(filename, page):
    with open(filename, "w", encoding="utf-8") as f:
        print(page, file=f)


def replace_page_elements(replace_map, parser, obj):
    for tag, parameters in replace_map.items():
        for name, getter in parameters.items():
            tags = parser.find_all(tag, {'itemprop': name})
            if len(tags) == 1:
                print(getter(obj))
                tags[0].string = str(getter(obj))
            else:
                pass
    return parser


@csrf_exempt
def publish_basic_information(request):
    if request.method == 'POST':
        body_json = JSONParser().parse(request)
        id = body_json['id']
        information = BasicInformations.objects.get(BIid=id)
        file = 'EmployeeApp/parser/pages/common/index.html'
        page_parser = read_page(file)
        new_page = str(replace_page_elements(basic_information_replace_map, page_parser, information))
        write_page(file, new_page)
        return HttpResponse("OK")


@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)


# ------------------------- ОРГАНЫ УПРАВЛЕНИЯ ОБРАЗОВАТЕЛЬНОЙ ОРГАНИЗАЦИИ ---------------------------------

def management_to_list(row):
    return [row.id, row.name, row.fio, row.regulation]


def management_format():
    return ['id', 'name', 'fio', 'regulation']


@csrf_exempt
def managements(request):
    if request.method == 'GET':
        a = Managements.objects.all()
        a = [management_to_list(item) for item in a]
        return JsonResponse({
            'format': management_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def managementsFormat(request):
    if request.method == 'GET':
        return JsonResponse(management_format(), safe=False)


@csrf_exempt
def managements_by_id(request, id):
    if request.method == 'DELETE':
        obj = Managements.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Managements(
            name=req_json['name'],
            fio=req_json['fio'],
            regulation=req_json['regulation'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Managements.objects.get(id=id)
        obj = Managements(
            id=int(id),
            name=req_json['name'],
            fio=req_json['fio'],
            regulation=req_json['regulation'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


management_info_replace_map = {
    'td': {
        'name': lambda obj: obj[0],
        'fio': lambda obj: obj[1],
    }
}

management_info_replace_links_map = {
    'td': {
        'divisionClauseDocLink': lambda obj: obj[2],
    }
}

management_info_row_template = \
    '<tr itemprop="management">' \
    '<td itemprop="name"></td>' \
    '<td itemprop="fio"></td>' \
    '<td itemprop="divisionClauseDocLink"><a href="" download="">Положение</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def managements_publish(request):
    if request.method == 'GET':
        managements_information = Managements.objects.all()

        file = 'EmployeeApp/parser/pages/struct/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'id': "management"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'management'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(managements_information):
            values = management_to_list(item)[1:]
            row = bs4.BeautifulSoup(management_info_row_template)
            replace_page_elements(management_info_replace_map, row, values)
            replace_page_links(management_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------- СТРУКТУРНЫЕ ПОДРАЗДЕЛЕНИЯ ОБРАЗОВАТЕЛЬНОЙ ОРГАНИЗАЦИИ ---------------------------------

def subdivision_to_list(row):
    return [row.id, row.name, row.fio, row.position, row.address, row.off_site, row.email, row.file_url]


def subdivision_format():
    return ['id', 'name', 'fio', 'position', 'address', 'off_site', 'email', 'file_url']


def subdivision_format_types():
    return ['text', 'text', 'text', 'text', 'text', 'text', 'text', 'file']


@csrf_exempt
def subdivisions(request):
    if request.method == 'GET':
        a = Subdivisions.objects.all()
        a = [subdivision_to_list(item) for item in a]
        return JsonResponse({
            'format': subdivision_format(),
            'types': subdivision_format_types(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


uploaded_file_dir = "EmployeeApp/parser/pages/sveden/upload/"


def handle_uploaded_file(f):
    with open(uploaded_file_dir + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


import mimetypes


@csrf_exempt
def handle_file(request, filename=None):
    if request.method == "POST":
        handle_uploaded_file(request.FILES['upload_file'])
        return HttpResponse(200)
    elif request.method == "GET":
        file_path = uploaded_file_dir + filename
        file = open(file_path, 'rb')
        mime_type, _ = mimetypes.guess_type(file_path)
        response = HttpResponse(file, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
    else:
        return HttpResponseNotFound()


@csrf_exempt
def subdivisionsFormat(request):
    if request.method == 'GET':
        return JsonResponse({
            "format": subdivision_format(),
            "types": subdivision_format_types(),
        }, safe=False)


@csrf_exempt
def subdivisions_by_id(request, id):
    if request.method == 'DELETE':
        obj = Subdivisions.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Subdivisions(
            name=req_json['name'],
            fio=req_json['fio'],
            position=req_json['position'],
            address=req_json['address'],
            off_site=req_json['off_site'],
            email=req_json['email'],
            file_url=req_json['file_url'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Subdivisions.objects.get(id=id)
        obj = Subdivisions(
            id=int(id),
            name=req_json['name'],
            fio=req_json['fio'],
            position=req_json['position'],
            address=req_json['address'],
            off_site=req_json['off_site'],
            email=req_json['email'],
            file_url=req_json['file_url'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


department_info_replace_map = {
    'td': {
        'name': lambda obj: obj[0],
        'fio': lambda obj: obj[1],
        'post': lambda obj: obj[2],
        'addressStr': lambda obj: obj[3],
        # 'site': lambda obj: obj[4],
        'email': lambda obj: obj[5],
        # 'divisionClauseDocLink': lambda obj: obj[6],
    }
}

department_info_replace_links_map = {
    'td': {
        'site': lambda obj: obj[4],
    }
}

department_info_replace_files_map = {
    'td': {
        'divisionClauseDocLink': lambda obj: obj[6],
    }
}


def replace_page_links(replace_map, parser, obj):
    for tag, parameters in replace_map.items():
        for name, getter in parameters.items():
            tags = parser.find_all(tag, {'itemprop': name})
            if len(tags) == 1:
                tags[0].a['href'] = str(getter(obj))
                tags[0].a.string = str(getter(obj))
                print(tags[0].a)
            else:
                pass
    return parser


def replace_page_files(replace_map, parser, obj):
    for tag, parameters in replace_map.items():
        for name, getter in parameters.items():
            tags = parser.find_all(tag, {'itemprop': name})
            if len(tags) == 1:
                tags[0].a['href'] = "../upload/" + str(getter(obj))
                tags[0].a.string = str(getter(obj))
                print(tags[0].a)
            else:
                pass
    return parser


department_info_row_template = \
    '<tr itemprop="structOrgUprav">' \
    '<td itemprop="name"></td>' \
    '<td itemprop="fio"></td>' \
    '<td itemprop="post" style="text-transform: capitalize !important;"></td>' \
    '<td itemprop="addressStr"></td>' \
    '<td itemprop="site"><a href="">Ссылка</a></td>' \
    '<td itemprop="email" style="font-size: 10px !important;"></td>' \
    '<td itemprop="divisionClauseDocLink"><a href="" download>Положение</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def subdivisions_publish(request):
    if request.method == 'GET':
        departments_information = Subdivisions.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/struct/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'id': "departments"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'structOrgUprav'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(departments_information):
            values = subdivision_to_list(item)[1:]
            row = bs4.BeautifulSoup(department_info_row_template)
            replace_page_elements(department_info_replace_map, row, values)
            replace_page_links(department_info_replace_links_map, row, values)
            replace_page_files(department_info_replace_files_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------- Основные сведения ---------------------------------

def basic_information_to_list(row):
    return [row.id, row.date_create, row.address, row.mode, row.phones, row.emails, row.address_place]


def basic_information_format():
    return ['id', 'date_create', 'address', 'mode', 'phones', 'emails', 'address_place']


@csrf_exempt
def basic_informations(request):
    if request.method == 'GET':
        a = BasicInformations.objects.all()
        a = [basic_information_to_list(item) for item in a]
        return JsonResponse({
            'format': basic_information_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def basic_informationsFormat(request):
    if request.method == 'GET':
        return JsonResponse(basic_information_format(), safe=False)


@csrf_exempt
def basic_informations_by_id(request, id):
    if request.method == 'DELETE':
        obj = BasicInformations.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = BasicInformations(
            date_create=req_json['date_create'],
            address=req_json['address'],
            mode=req_json['mode'],
            phones=req_json['phones'],
            emails=req_json['emails'],
            address_place=req_json['address_place'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = BasicInformations.objects.get(id=id)
        obj = BasicInformations(
            id=int(id),
            date_create=req_json['date_create'],
            address=req_json['address'],
            mode=req_json['mode'],
            phones=req_json['phones'],
            emails=req_json['emails'],
            address_place=req_json['address_place'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


basic_information_info_replace_map = {
    'td': {
        'regDate': lambda obj: obj[0],
        'address': lambda obj: obj[1],
        'workTime': lambda obj: obj[2],
        'telephone': lambda obj: obj[3],
        # 'site': lambda obj: obj[4],
        'email': lambda obj: obj[4],
        # 'divisionClauseDocLink': lambda obj: obj[6],
    }
}

basic_information_info_replace_links_map = {
    'td': {
        'addressPlace': lambda obj: obj[5],
    }
}

basic_information_info_row_template = \
    '<tr itemprop="common">' \
    '<td itemprop="regDate" style="width: 30%;"></td>' \
    '<td itemprop="address"></td>' \
    '<td itemprop="workTime"></td>' \
    '<td itemprop="telephone"></td>' \
    '<td itemprop="email"></td>' \
    '<td itemprop="addressPlace"><a href="">Ссылка</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def basic_informations_publish(request):
    if request.method == 'GET':
        basic_informations_information = BasicInformations.objects.all()

        file = 'EmployeeApp/parser/pages/common/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'id': "main_information"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'common'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(basic_informations_information):
            values = basic_information_to_list(item)[1:]
            row = bs4.BeautifulSoup(basic_information_info_row_template)
            replace_page_elements(basic_information_info_replace_map, row, values)
            replace_page_links(basic_information_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------- УЧРЕДИТЕЛИ ОБРАЗОВАТЕЛЬНОЙ ОРГАНИЗАЦИИ ---------------------------------

def founder_to_list(row):
    return [row.id, row.name, row.address, row.phones, row.email, row.off_site]


def founder_format():
    return ['id', 'name', 'address', 'phones', 'email', 'off_site']


def founder_format_types():
    return ['text', 'text', 'text', 'text', 'text', 'text']


@csrf_exempt
def founders(request):
    if request.method == 'GET':
        a = Founders.objects.all()
        a = [founder_to_list(item) for item in a]
        return JsonResponse({
            'format': founder_format(),
            'types': founder_format_types(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def foundersFormat(request):
    if request.method == 'GET':
        return JsonResponse({
            "format": subdivision_format(),
            "types": subdivision_format_types(),
        }, safe=False)


@csrf_exempt
def founders_by_id(request, id):
    if request.method == 'DELETE':
        obj = Founders.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Founders(
            name=req_json['name'],
            address=req_json['address'],
            phones=req_json['phones'],
            email=req_json['email'],
            off_site=req_json['off_site'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Founders.objects.get(id=id)
        obj = Founders(
            id=int(id),
            name=req_json['name'],
            address=req_json['address'],
            phones=req_json['phones'],
            email=req_json['email'],
            off_site=req_json['off_site'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


founder_info_replace_map = {
    'td': {
        'nameUchred': lambda obj: obj[0],
        'addressUchred': lambda obj: obj[1],
        'telUchred': lambda obj: obj[2],
        'mailUchred': lambda obj: obj[3],
    }
}

founder_info_replace_links_map = {
    'td': {
        'websiteUchred': lambda obj: obj[4],
    }
}

founder_info_row_template = \
    '<tr itemprop="uchred">' \
    '<td itemprop="nameUchred"></td>' \
    '<td itemprop="addressUchred"></td>' \
    '<td itemprop="telUchred"></td>' \
    '<td itemprop="mailUchred"></td>' \
    '<td itemprop="websiteUchred"><a href="">Ссылка</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def founders_publish(request):
    if request.method == 'GET':
        founders_information = Founders.objects.all()

        file = 'EmployeeApp/parser/pages/common/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "uchredLaw"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'uchred'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(founders_information):
            values = founder_to_list(item)[1:]
            row = bs4.BeautifulSoup(founder_info_row_template)
            replace_page_elements(founder_info_replace_map, row, values)
            replace_page_links(founder_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------- ФИЛИАЛЫ ОБРАЗОВАТЕЛЬНОЙ ОРГАНИЗАЦИИ ---------------------------------

def filiation_to_list(row):
    return [row.id, row.name, row.address, row.work_time, row.telephone, row.email, row.website]


def filiation_format():
    return ['id', 'name', 'address', 'work_time', 'telephone', 'email', 'website']


@csrf_exempt
def filiations(request):
    if request.method == 'GET':
        a = Filiations.objects.all()
        a = [filiation_to_list(item) for item in a]
        return JsonResponse({
            'format': filiation_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def filiationsFormat(request):
    if request.method == 'GET':
        return JsonResponse(filiation_format(), safe=False)


@csrf_exempt
def filiations_by_id(request, id):
    if request.method == 'DELETE':
        obj = Filiations.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Filiations(
            name=req_json['name'],
            address=req_json['address'],
            work_time=req_json['work_time'],
            telephone=req_json['telephone'],
            email=req_json['email'],
            website=req_json['website'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Filiations.objects.get(id=id)
        obj = Filiations(
            id=int(id),
            name=req_json['name'],
            address=req_json['address'],
            work_time=req_json['work_time'],
            telephone=req_json['telephone'],
            email=req_json['email'],
            website=req_json['website'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


filiation_info_replace_map = {
    'td': {
        'nameFil': lambda obj: obj[0],
        'addressFil': lambda obj: obj[1],
        'workTimeFil': lambda obj: obj[2],
        'telephoneFil': lambda obj: obj[3],
        'emailFil': lambda obj: obj[4],
    }
}

filiation_info_replace_links_map = {
    'td': {
        'websiteFil': lambda obj: obj[5],
    }
}

filiation_info_row_template = \
    '<tr itemprop="fil">' \
    '<td itemprop="nameFil"></td>' \
    '<td itemprop="addressFil"></td>' \
    '<td itemprop="workTimeFil"></td>' \
    '<td itemprop="telephoneFil"></td>' \
    '<td itemprop="emailFil"></td>' \
    '<td itemprop="websiteFil"><a href="">Ссылка</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def filiations_publish(request):
    if request.method == 'GET':
        filiations_information = Filiations.objects.all()

        file = 'EmployeeApp/parser/pages/common/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "filInfo"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'fil'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(filiations_information):
            values = filiation_to_list(item)[1:]
            row = bs4.BeautifulSoup(filiation_info_row_template)
            replace_page_elements(filiation_info_replace_map, row, values)
            replace_page_links(filiation_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------- ПРЕДСТАВИТЕЛЬСТВО ОБРАЗОВАТЕЛЬНОЙ ОРГАНИЗАЦИИ ---------------------------------

def representation_to_list(row):
    return [row.id, row.name, row.address, row.work_time, row.telephone, row.email, row.website]


def representation_format():
    return ['id', 'name', 'address', 'work_time', 'telephone', 'email', 'website']


@csrf_exempt
def representations(request):
    if request.method == 'GET':
        a = Representations.objects.all()
        a = [representation_to_list(item) for item in a]
        return JsonResponse({
            'format': representation_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def representationsFormat(request):
    if request.method == 'GET':
        return JsonResponse(representation_format(), safe=False)


@csrf_exempt
def representations_by_id(request, id):
    if request.method == 'DELETE':
        obj = Representations.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Representations(
            name=req_json['name'],
            address=req_json['address'],
            work_time=req_json['work_time'],
            telephone=req_json['telephone'],
            email=req_json['email'],
            website=req_json['website'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Representations.objects.get(id=id)
        obj = Representations(
            id=int(id),
            name=req_json['name'],
            address=req_json['address'],
            work_time=req_json['work_time'],
            telephone=req_json['telephone'],
            email=req_json['email'],
            website=req_json['website'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


representation_info_replace_map = {
    'td': {
        'nameRep': lambda obj: obj[0],
        'addressRep': lambda obj: obj[1],
        'workTimeRep': lambda obj: obj[2],
        'telephoneRep': lambda obj: obj[3],
        'emailRep': lambda obj: obj[4],
    }
}

representation_info_replace_links_map = {
    'td': {
        'websiteRep': lambda obj: obj[5],
    }
}

representation_info_row_template = \
    '<tr itemprop="rep">' \
    '<td itemprop="nameRep"></td>' \
    '<td itemprop="addressRep"></td>' \
    '<td itemprop="workTimeRep"></td>' \
    '<td itemprop="telephoneRep"></td>' \
    '<td itemprop="emailRep"></td>' \
    '<td itemprop="websiteRep"><a href="">Ссылка</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def representations_publish(request):
    if request.method == 'GET':
        representations_information = Representations.objects.all()

        file = 'EmployeeApp/parser/pages/common/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "repInfo"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'rep'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(representations_information):
            values = representation_to_list(item)[1:]
            row = bs4.BeautifulSoup(representation_info_row_template)
            replace_page_elements(representation_info_replace_map, row, values)
            replace_page_links(representation_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------- ОБЪЕМ ОБРАЗОВАТЕЛЬНОЙ ДЕЯТЕЛЬНОСТИ ---------------------------------

def volume_to_list(row):
    return [row.id, row.federal, row.sub, row.place, row.fis, row.money, row.moneyfile, row.plan, row.info]


def volume_format():
    return ['id', 'federal', 'sub', 'place', 'fis', 'money', 'moneyfile', 'plan', 'info']


@csrf_exempt
def volumes(request):
    if request.method == 'GET':
        a = Volumes.objects.all()
        a = [volume_to_list(item) for item in a]
        return JsonResponse({
            'format': volume_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def volumesFormat(request):
    if request.method == 'GET':
        return JsonResponse(volume_format(), safe=False)


@csrf_exempt
def volumes_by_id(request, id):
    if request.method == 'DELETE':
        obj = Volumes.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Volumes(
            federal=req_json['federal'],
            sub=req_json['sub'],
            place=req_json['place'],
            fis=req_json['fis'],
            money=req_json['money'],
            moneyfile=req_json['moneyfile'],
            plan=req_json['plan'],
            info=req_json['info'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Volumes.objects.get(id=id)
        obj = Volumes(
            id=int(id),
            federal=req_json['federal'],
            sub=req_json['sub'],
            place=req_json['place'],
            fis=req_json['fis'],
            money=req_json['money'],
            moneyfile=req_json['moneyfile'],
            plan=req_json['plan'],
            info=req_json['info'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


volume_info_replace_map = {
    'td': {
        'finBFVolume': lambda obj: obj[0],
        'finBRVolume': lambda obj: obj[1],
        'finBMVolume': lambda obj: obj[2],
        'finPVolume': lambda obj: obj[3],
    }
}

volume_info_replace_links_map = {
    'td': {
        'finYear': lambda obj: obj[4],
        'finPost': lambda obj: obj[5],
        'finRas': lambda obj: obj[6],
    }
}

volume_info_row_template = \
    '<tr itemprop="volume">' \
    '<td itemprop="finBFVolume"></td>' \
    '<td itemprop="finBRVolume"></td>' \
    '<td itemprop="finBMVolume"></td>' \
    '<td itemprop="finPVolume"></td>' \
    '<td itemprop="finYear"><a href="" download="">Положение</a></td>' \
    '<td itemprop="finPost"><a href="" download="">Положение</a></td>' \
    '<td itemprop="finRas"><a href="">Ссылка</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def volumes_publish(request):
    if request.method == 'GET':
        volumes_information = Volumes.objects.all()

        file = 'EmployeeApp/parser/pages/budget/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "volumes"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'volume'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(volumes_information):
            values = volume_to_list(item)[1:]
            row = bs4.BeautifulSoup(volume_info_row_template)
            replace_page_elements(volume_info_replace_map, row, values)
            replace_page_links(volume_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------- ВАКАНТНЫЕ МЕСТА ДЛЯ ПРИЁМА (ПЕРЕВОДА) ---------------------------------

def vac_to_list(row):
    return [row.id, row.code, row.spec, row.level, row.kurs, row.form, row.federal, row.sub, row.place, row.fis]


def vac_format():
    return ['id', 'code', 'spec', 'level', 'kurs', 'form', 'federal', 'sub', 'place', 'fis']


@csrf_exempt
def vacs(request):
    if request.method == 'GET':
        a = Vacs.objects.all()
        a = [vac_to_list(item) for item in a]
        return JsonResponse({
            'format': vac_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def vacsFormat(request):
    if request.method == 'GET':
        return JsonResponse(vac_format(), safe=False)


@csrf_exempt
def vacs_by_id(request, id):
    if request.method == 'DELETE':
        obj = Vacs.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Vacs(
            code=req_json['code'],
            spec=req_json['spec'],
            level=req_json['level'],
            kurs=req_json['kurs'],
            form=req_json['form'],
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
        obj_old = Vacs.objects.get(id=id)
        obj = Vacs(
            id=int(id),
            code=req_json['code'],
            spec=req_json['spec'],
            level=req_json['level'],
            kurs=req_json['kurs'],
            form=req_json['form'],
            federal=req_json['federal'],
            sub=req_json['sub'],
            place=req_json['place'],
            fis=req_json['fis'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


vac_info_replace_map = {
    'td': {
        'eduCode': lambda obj: obj[0],
        'eduName': lambda obj: obj[1],
        'eduLevel': lambda obj: obj[2],
        'eduCourse': lambda obj: obj[3],
        'eduForm': lambda obj: obj[4],
        'numberBFVacant': lambda obj: obj[5],
        'numberBRVacant': lambda obj: obj[6],
        'numberBMVacant': lambda obj: obj[7],
        'numberPVacant': lambda obj: obj[8],
    }
}

# vac_info_replace_links_map = {
#     'td': {
#         'finYear': lambda obj: obj[4],
#         'finPost': lambda obj: obj[5],
#         'finRas': lambda obj: obj[6],
#     }
# }

vac_info_row_template = \
    '<tr itemprop="vac">' \
    '<td itemprop="eduCode"></td>' \
    '<td itemprop="eduName"></td>' \
    '<td itemprop="eduLevel"></td>' \
    '<td itemprop="eduCourse"></td>' \
    '<td itemprop="eduForm"></td>' \
    '<td itemprop="numberBFVacant"></td>' \
    '<td itemprop="numberBRVacant"></td>' \
    '<td itemprop="numberBMVacant"></td>' \
    '<td itemprop="numberPVacant"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def vacs_publish(request):
    if request.method == 'GET':
        vacs_information = Vacs.objects.all()

        file = 'EmployeeApp/parser/pages/vacant/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "vacant"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'vac'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(vacs_information):
            values = vac_to_list(item)[1:]
            row = bs4.BeautifulSoup(vac_info_row_template)
            replace_page_elements(vac_info_replace_map, row, values)
            # replace_page_links(vac_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------ РУКОВОДСТВО. ПЕДАГОГИЧЕСКИЙ (НАУЧНО-ПЕДАГОГИЧЕСКИЙ) СОСТАВ -------------------------------
# ------------------------- ИНФОРМАЦИЯ ОБ АДМИНИСТРАЦИИ ОБРАЗОВАТЕЛЬНОЙ ОРГАНИЗАЦИИ ---------------------------------

def leader_to_list(row):
    return [row.id, row.fio, row.post, row.phone, row.address]


def leader_format():
    return ['id', 'fio', 'post', 'phone', 'address']


@csrf_exempt
def leaders(request):
    if request.method == 'GET':
        a = Leaders.objects.all()
        a = [leader_to_list(item) for item in a]
        return JsonResponse({
            'format': leader_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def leadersFormat(request):
    if request.method == 'GET':
        return JsonResponse(leader_format(), safe=False)


@csrf_exempt
def leaders_by_id(request, id):
    if request.method == 'DELETE':
        obj = Leaders.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Leaders(
            fio=req_json['fio'],
            post=req_json['post'],
            phone=req_json['phone'],
            address=req_json['address'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Leaders.objects.get(id=id)
        obj = Leaders(
            id=int(id),
            fio=req_json['fio'],
            post=req_json['post'],
            phone=req_json['phone'],
            address=req_json['address'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


leader_info_replace_map = {
    'td': {
        'fio': lambda obj: obj[0],
        'post': lambda obj: obj[1],
        'telephone': lambda obj: obj[2],
        'email': lambda obj: obj[3],
    }
}

# vac_info_replace_links_map = {
#     'td': {
#         'finYear': lambda obj: obj[4],
#         'finPost': lambda obj: obj[5],
#         'finRas': lambda obj: obj[6],
#     }
# }

leader_info_row_template = \
    '<tr itemprop="rucovodstvo">' \
    '<td itemprop="fio"></td>' \
    '<td itemprop="post"></td>' \
    '<td itemprop="telephone"></td>' \
    '<td itemprop="email"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def leaders_publish(request):
    if request.method == 'GET':
        leaders_information = Leaders.objects.all()

        file = 'EmployeeApp/parser/pages/employees/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "rucov"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'rucovodstvo'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(leaders_information):
            values = leader_to_list(item)[1:]
            row = bs4.BeautifulSoup(leader_info_row_template)
            replace_page_elements(leader_info_replace_map, row, values)
            # replace_page_links(vac_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------ РУКОВОДСТВО. ПЕДАГОГИЧЕСКИЙ (НАУЧНО-ПЕДАГОГИЧЕСКИЙ) СОСТАВ -------------------------------
# ------------------------- ИНФОРМАЦИЯ ОБ АДМИНИСТРАЦИИ ОБРАЗОВАТЕЛЬНОЙ ОРГАНИЗАЦИИ ЗАМЕСТИТЕЛИ------------------------

def leadersTwo_to_list(row):
    return [row.id, row.fio, row.post, row.phone, row.address]


def leadersTwo_format():
    return ['id', 'fio', 'post', 'phone', 'address']


@csrf_exempt
def leadersTwos(request):
    if request.method == 'GET':
        a = Leaderstwo.objects.all()
        a = [leadersTwo_to_list(item) for item in a]
        return JsonResponse({
            'format': leadersTwo_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def leadersTwosFormat(request):
    if request.method == 'GET':
        return JsonResponse(leadersTwo_format(), safe=False)


@csrf_exempt
def leadersTwos_by_id(request, id):
    if request.method == 'DELETE':
        obj = Leaderstwo.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Leaderstwo(
            fio=req_json['fio'],
            post=req_json['post'],
            phone=req_json['phone'],
            address=req_json['address'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Leaderstwo.objects.get(id=id)
        obj = Leaderstwo(
            id=int(id),
            fio=req_json['fio'],
            post=req_json['post'],
            phone=req_json['phone'],
            address=req_json['address'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


leadersTwo_info_replace_map = {
    'td': {
        'fio': lambda obj: obj[0],
        'post': lambda obj: obj[1],
        'telephone': lambda obj: obj[2],
        'email': lambda obj: obj[3],
    }
}

# vac_info_replace_links_map = {
#     'td': {
#         'finYear': lambda obj: obj[4],
#         'finPost': lambda obj: obj[5],
#         'finRas': lambda obj: obj[6],
#     }
# }

leadersTwo_info_row_template = \
    '<tr itemprop="rucovodstvoZam">' \
    '<td itemprop="fio"></td>' \
    '<td itemprop="post"></td>' \
    '<td itemprop="telephone"></td>' \
    '<td itemprop="email"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def leadersTwos_publish(request):
    if request.method == 'GET':
        leadersTwos_information = Leaderstwo.objects.all()

        file = 'EmployeeApp/parser/pages/employees/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "rucovZam"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'rucovodstvoZam'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(leadersTwos_information):
            values = leadersTwo_to_list(item)[1:]
            row = bs4.BeautifulSoup(leadersTwo_info_row_template)
            replace_page_elements(leadersTwo_info_replace_map, row, values)
            # replace_page_links(vac_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------ РУКОВОДСТВО. ПЕДАГОГИЧЕСКИЙ (НАУЧНО-ПЕДАГОГИЧЕСКИЙ) СОСТАВ -------------------------------
# ----------------------ИНФОРМАЦИЯ О РУКОВОДИТЕЛЯХ ФИЛИАЛОВ ОБРАЗОВАТЕЛЬНОЙ ОРГАНИЗАЦИИ-----------------

def filialLeader_to_list(row):
    return [row.id, row.name, row.fio, row.post, row.phone, row.address]


def filialLeader_format():
    return ['id', 'name', 'fio', 'post', 'phone', 'address']


@csrf_exempt
def filialLeaders(request):
    if request.method == 'GET':
        a = FilialLeaders.objects.all()
        a = [filialLeader_to_list(item) for item in a]
        return JsonResponse({
            'format': filialLeader_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def filialLeadersFormat(request):
    if request.method == 'GET':
        return JsonResponse(filialLeader_format(), safe=False)


@csrf_exempt
def filialLeaders_by_id(request, id):
    if request.method == 'DELETE':
        obj = FilialLeaders.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = FilialLeaders(
            name=req_json['name'],
            fio=req_json['fio'],
            post=req_json['post'],
            phone=req_json['phone'],
            address=req_json['address'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = FilialLeaders.objects.get(id=id)
        obj = FilialLeaders(
            id=int(id),
            name=req_json['name'],
            fio=req_json['fio'],
            post=req_json['post'],
            phone=req_json['phone'],
            address=req_json['address'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


filialLeader_info_replace_map = {
    'td': {
        'nameFil': lambda obj: obj[0],
        'fio': lambda obj: obj[1],
        'post': lambda obj: obj[2],
        'telephone': lambda obj: obj[3],
        'email': lambda obj: obj[4],
    }
}

# vac_info_replace_links_map = {
#     'td': {
#         'finYear': lambda obj: obj[4],
#         'finPost': lambda obj: obj[5],
#         'finRas': lambda obj: obj[6],
#     }
# }

filialLeader_info_row_template = \
    '<tr itemprop="rucovodstvoFil">' \
    '<td itemprop="nameFil"></td>' \
    '<td itemprop="fio"></td>' \
    '<td itemprop="post"></td>' \
    '<td itemprop="telephone"></td>' \
    '<td itemprop="email"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def filialLeaders_publish(request):
    if request.method == 'GET':
        filialLeaders_information = FilialLeaders.objects.all()

        file = 'EmployeeApp/parser/pages/employees/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "filialLeaders"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'rucovodstvoFil'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(filialLeaders_information):
            values = filialLeader_to_list(item)[1:]
            row = bs4.BeautifulSoup(filialLeader_info_row_template)
            replace_page_elements(filialLeader_info_replace_map, row, values)
            # replace_page_links(vac_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------ РУКОВОДСТВО. ПЕДАГОГИЧЕСКИЙ (НАУЧНО-ПЕДАГОГИЧЕСКИЙ) СОСТАВ -------------------------------
# ----------ИНФОРМАЦИЯ О ПЕРСОНАЛЬНОМ СОСТАВЕ ПЕДАГОГИЧЕСКИХ РАБОТНИКОВ ОБРАЗОВАТЕЛЬНОЙ ОРГАНИЗАЦИИ-----------------

def teacher_to_list(row):
    return [row.id, row.fio, row.post, row.dicipline, row.edulevel, row.qual, row.level, row.tittitle, row.naimnapr,
            row.levelup, row.allyears, row.scpecyears]


def teacher_format():
    return ['id', 'fio', 'post', 'dicipline', 'edulevel', 'qual', 'level', 'tittitle', 'naimnapr', 'levelup',
            'allyears', 'scpecyears']


@csrf_exempt
def teachers(request):
    if request.method == 'GET':
        a = Teachers.objects.all()
        a = [teacher_to_list(item) for item in a]
        return JsonResponse({
            'format': teacher_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def teachersFormat(request):
    if request.method == 'GET':
        return JsonResponse(teacher_format(), safe=False)


@csrf_exempt
def teachers_by_id(request, id):
    if request.method == 'DELETE':
        obj = Teachers.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Teachers(
            fio=req_json['fio'],
            post=req_json['post'],
            dicipline=req_json['dicipline'],
            edulevel=req_json['edulevel'],
            qual=req_json['qual'],
            level=req_json['level'],
            tittitle=req_json['tittitle'],
            naimnapr=req_json['naimnapr'],
            levelup=req_json['levelup'],
            allyears=req_json['allyears'],
            scpecyears=req_json['scpecyears'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Teachers.objects.get(id=id)
        obj = Teachers(
            id=int(id),
            fio=req_json['fio'],
            post=req_json['post'],
            dicipline=req_json['dicipline'],
            edulevel=req_json['edulevel'],
            qual=req_json['qual'],
            level=req_json['level'],
            tittitle=req_json['tittitle'],
            naimnapr=req_json['naimnapr'],
            levelup=req_json['levelup'],
            allyears=req_json['allyears'],
            scpecyears=req_json['scpecyears'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


teacher_info_replace_map = {
    'td': {
        'fio': lambda obj: obj[0],
        'post': lambda obj: obj[1],
        'teachingDiscipline': lambda obj: obj[2],
        'teachingLevel': lambda obj: obj[3],
        'teachingQual': lambda obj: obj[4],
        'degree': lambda obj: obj[5],
        'academStat': lambda obj: obj[6],
        'employeeQualification': lambda obj: obj[7],
        'profDevelopment': lambda obj: obj[8],
        'genExperience': lambda obj: obj[9],
        'specExperience': lambda obj: obj[10],
    }
}

# vac_info_replace_links_map = {
#     'td': {
#         'finYear': lambda obj: obj[4],
#         'finPost': lambda obj: obj[5],
#         'finRas': lambda obj: obj[6],
#     }
# }

teacher_info_row_template = \
    '<tr itemprop="teachingStaff">' \
    '<td itemprop="fio"></td>' \
    '<td itemprop="post"></td>' \
    '<td itemprop="teachingDiscipline"></td>' \
    '<td itemprop="teachingLevel"></td>' \
    '<td itemprop="teachingQual"></td>' \
    '<td itemprop="degree"></td>' \
    '<td itemprop="academStat"></td>' \
    '<td itemprop="employeeQualification"></td>' \
    '<td itemprop="profDevelopment"></td>' \
    '<td itemprop="genExperience"></td>' \
    '<td itemprop="specExperience"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def teachers_publish(request):
    if request.method == 'GET':
        teachers_information = Teachers.objects.all()

        file = 'EmployeeApp/parser/pages/employees/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "teacher"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'teachingStaff'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(teachers_information):
            values = teacher_to_list(item)[1:]
            row = bs4.BeautifulSoup(teacher_info_row_template)
            replace_page_elements(teacher_info_replace_map, row, values)
            # replace_page_links(vac_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------- ОБРАЗОВАТЕЛЬНЫЕ СТАНДАРТЫ ---------------------------------

def standartCopie_to_list(row):
    return [row.id, row.name, row.filename]


def standartCopie_format():
    return ['id', 'name', 'filename']


@csrf_exempt
def standartCopies(request):
    if request.method == 'GET':
        a = StandartCopies.objects.all()
        a = [standartCopie_to_list(item) for item in a]
        return JsonResponse({
            'format': standartCopie_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def standartCopiesFormat(request):
    if request.method == 'GET':
        return JsonResponse(standartCopie_format(), safe=False)


@csrf_exempt
def standartCopies_by_id(request, id):
    if request.method == 'DELETE':
        obj = StandartCopies.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = StandartCopies(
            name=req_json['name'],
            filename=req_json['filename'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = StandartCopies.objects.get(id=id)
        obj = StandartCopies(
            id=int(id),
            name=req_json['name'],
            filename=req_json['filename'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


standartCopie_info_replace_map = {
    'td': {
        'eduFedDoc': lambda obj: obj[0],
    }
}

standartCopie_info_replace_links_map = {
    'td': {
        'eduStandartDoc': lambda obj: obj[1],
    }
}

standartCopie_info_row_template = \
    '<tr itemprop="standart">' \
    '<td itemprop="eduFedDoc"></td>' \
    '<td itemprop="eduStandartDoc"><a href="" download="">Положение</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def standartCopies_publish(request):
    if request.method == 'GET':
        standartCopies_information = StandartCopies.objects.all()

        file = 'EmployeeApp/parser/pages/eduStandarts/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "eduStandarts"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'standart'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(standartCopies_information):
            values = volume_to_list(item)[1:]
            row = bs4.BeautifulSoup(standartCopie_info_row_template)
            replace_page_elements(standartCopie_info_replace_map, row, values)
            replace_page_links(standartCopie_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------- ПЛАТНЫЕ ОБРАЗОВАТЕЛЬНЫЕ УСЛУГИ ---------------------------------

def paidService_to_list(row):
    return [row.id, row.info, row.dogpaid, row.doc, row.order, row.docnew]


def paidService_format():
    return ['id', 'info', 'dogpaid', 'doc', 'order', 'docnew']


@csrf_exempt
def paidServices(request):
    if request.method == 'GET':
        a = PaidServices.objects.all()
        a = [paidService_to_list(item) for item in a]
        return JsonResponse({
            'format': paidService_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def paidServicesFormat(request):
    if request.method == 'GET':
        return JsonResponse(paidService_format(), safe=False)


@csrf_exempt
def paidServices_by_id(request, id):
    if request.method == 'DELETE':
        obj = PaidServices.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = PaidServices(
            info=req_json['info'],
            dogpaid=req_json['dogpaid'],
            doc=req_json['doc'],
            order=req_json['order'],
            docnew=req_json['docnew'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = PaidServices.objects.get(id=id)
        obj = PaidServices(
            id=int(id),
            info=req_json['info'],
            dogpaid=req_json['dogpaid'],
            doc=req_json['doc'],
            order=req_json['order'],
            docnew=req_json['docnew'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


paidService_info_replace_map = {
    'td': {
        'paidEdu': lambda obj: obj[0],
    }
}

paidService_info_replace_links_map = {
    'td': {
        'paidParents': lambda obj: obj[1],
        'paidParents': lambda obj: obj[2],
        'paidParents': lambda obj: obj[3],
        'paidParents': lambda obj: obj[4],
    }
}

paidService_info_row_template = \
    '<tr itemprop="paid">' \
    '<td itemprop="paidParents"><a href="" download="">Положение</a></td>' \
    '<td itemprop="paidParents"><a href="" download="">Положение</a></td>' \
    '<td itemprop="paidParents"><a href="" download="">Положение</a></td>' \
    '<td itemprop="paidParents"><a href="" download="">Положение</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def paidServices_publish(request):
    if request.method == 'GET':
        paidServices_information = PaidServices.objects.all()

        file = 'EmployeeApp/parser/pages/paid_edu/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "paidEdu"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'paid'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(paidServices_information):
            values = volume_to_list(item)[1:]
            row = bs4.BeautifulSoup(paidService_info_row_template)
            replace_page_elements(paidService_info_replace_map, row, values)
            replace_page_links(paidService_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ----------------------------------- Международное сотрудничество  -------------------------------------------
# -----Информация о заключенных и планируемых к заключению договорах с иностранными и (или) международными
# -------------------------------организациями по вопросам образования и науки---------------------------------

def internationalDog_to_list(row):
    return [row.id, row.state_name, row.org_name, row.dog_reg]


def internationalDog_format():
    return ['id', 'state_name', 'org_name', 'dog_reg']


@csrf_exempt
def internationalDogs(request):
    if request.method == 'GET':
        a = Internationaldog.objects.all()
        a = [internationalDog_to_list(item) for item in a]
        return JsonResponse({
            'format': internationalDog_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def internationalDogsFormat(request):
    if request.method == 'GET':
        return JsonResponse(internationalDog_format(), safe=False)


@csrf_exempt
def internationalDogs_by_id(request, id):
    if request.method == 'DELETE':
        obj = Internationaldog.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Internationaldog(
            state_name=req_json['state_name'],
            org_name=req_json['org_name'],
            dog_reg=req_json['dog_reg'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Internationaldog.objects.get(id=id)
        obj = Internationaldog(
            id=int(id),
            state_name=req_json['state_name'],
            org_name=req_json['org_name'],
            dog_reg=req_json['dog_reg'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


internationalDog_info_replace_map = {
    'td': {
        'stateName': lambda obj: obj[0],
        'orgName': lambda obj: obj[1],
        'dogReg': lambda obj: obj[2],
    }
}

# internationalDog_info_replace_links_map = {
#     'td': {
#         'paidParents': lambda obj: obj[1],
#         'paidParents': lambda obj: obj[2],
#         'paidParents': lambda obj: obj[3],
#         'paidParents': lambda obj: obj[4],
#     }
# }

internationalDog_info_row_template = \
    '<tr itemprop="internationalDog">' \
    '<td itemprop="stateName"></td>' \
    '<td itemprop="orgName"></td>' \
    '<td itemprop="dogReg"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def internationalDogs_publish(request):
    if request.method == 'GET':
        internationalDogs_information = Internationaldog.objects.all()

        file = 'EmployeeApp/parser/pages/inter/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "internationalD"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'internationalDog'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(internationalDogs_information):
            values = internationalDog_to_list(item)[1:]
            row = bs4.BeautifulSoup(internationalDog_info_row_template)
            replace_page_elements(internationalDog_info_replace_map, row, values)
            # replace_page_links(internationalDog_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ----------------------------------- Международное сотрудничество  -------------------------------------------
# ----------------------------- Информация о международной аккредитации ---------------------------------------

def internationalAccr_to_list(row):
    return [row.id, row.edu_code, row.edu_name, row.org_name, row.date_end]


def internationalAccr_format():
    return ['id', 'edu_code', 'edu_name', 'org_name', 'date_end']


@csrf_exempt
def internationalAccrs(request):
    if request.method == 'GET':
        a = Internationalaccr.objects.all()
        a = [internationalAccr_to_list(item) for item in a]
        return JsonResponse({
            'format': internationalAccr_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def internationalAccrsFormat(request):
    if request.method == 'GET':
        return JsonResponse(internationalAccr_format(), safe=False)


@csrf_exempt
def internationalAccrs_by_id(request, id):
    if request.method == 'DELETE':
        obj = Internationalaccr.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Internationalaccr(
            edu_code=req_json['edu_code'],
            edu_name=req_json['edu_name'],
            org_name=req_json['org_name'],
            date_end=req_json['date_end'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Internationalaccr.objects.get(id=id)
        obj = Internationalaccr(
            id=int(id),
            edu_code=req_json['edu_code'],
            edu_name=req_json['edu_name'],
            org_name=req_json['org_name'],
            date_end=req_json['date_end'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


internationalAccr_info_replace_map = {
    'td': {
        'eduCode': lambda obj: obj[0],
        'eduName': lambda obj: obj[1],
        'orgName': lambda obj: obj[2],
        'dateEnd': lambda obj: obj[3],
    }
}

# internationalDog_info_replace_links_map = {
#     'td': {
#         'paidParents': lambda obj: obj[1],
#         'paidParents': lambda obj: obj[2],
#         'paidParents': lambda obj: obj[3],
#         'paidParents': lambda obj: obj[4],
#     }
# }

internationalAccr_info_row_template = \
    '<tr itemprop="internationalAccr">' \
    '<td itemprop="eduCode"></td>' \
    '<td itemprop="eduName"></td>' \
    '<td itemprop="orgName"></td>' \
    '<td itemprop="dateEnd"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def internationalAccrs_publish(request):
    if request.method == 'GET':
        internationalAccrs_information = Internationalaccr.objects.all()

        file = 'EmployeeApp/parser/pages/inter/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "internationalA"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'internationalAccr'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(internationalAccrs_information):
            values = internationalAccr_to_list(item)[1:]
            row = bs4.BeautifulSoup(internationalAccr_info_row_template)
            replace_page_elements(internationalAccr_info_replace_map, row, values)
            # replace_page_links(internationalDog_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------------------------- Доступная среда  ------------------------------------------------
# --------------------------- Сведения о специально оборудованных учебных кабинетах ---------------------------

def specCab_to_list(row):
    return [row.id, row.address, row.name, row.osn, row.ovz]


def specCab_format():
    return ['id', 'address', 'name', 'osn', 'ovz']


@csrf_exempt
def specCabs(request):
    if request.method == 'GET':
        a = SpecCab.objects.all()
        a = [specCab_to_list(item) for item in a]
        return JsonResponse({
            'format': specCab_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def specCabsFormat(request):
    if request.method == 'GET':
        return JsonResponse(specCab_format(), safe=False)


@csrf_exempt
def specCabs_by_id(request, id):
    if request.method == 'DELETE':
        obj = SpecCab.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = SpecCab(
            address=req_json['address'],
            name=req_json['name'],
            osn=req_json['osn'],
            ovz=req_json['ovz'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = SpecCab.objects.get(id=id)
        obj = SpecCab(
            id=int(id),
            address=req_json['address'],
            name=req_json['name'],
            osn=req_json['osn'],
            ovz=req_json['ovz'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


specCab_info_replace_map = {
    'td': {
        'addressCab': lambda obj: obj[0],
        'nameCab': lambda obj: obj[1],
        'osnCab': lambda obj: obj[2],
        'ovzCab': lambda obj: obj[3],
    }
}

# internationalDog_info_replace_links_map = {
#     'td': {
#         'paidParents': lambda obj: obj[1],
#         'paidParents': lambda obj: obj[2],
#         'paidParents': lambda obj: obj[3],
#         'paidParents': lambda obj: obj[4],
#     }
# }

specCab_info_row_template = \
    '<tr itemprop="purposeCab">' \
    '<td itemprop="addressCab"></td>' \
    '<td itemprop="nameCab"></td>' \
    '<td itemprop="osnCab"></td>' \
    '<td itemprop="ovzCab"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def specCabs_publish(request):
    if request.method == 'GET':
        specCabs_information = SpecCab.objects.all()

        file = 'EmployeeApp/parser/pages/ovz/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "cab"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'purposeCab'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(specCabs_information):
            values = specCab_to_list(item)[1:]
            row = bs4.BeautifulSoup(specCab_info_row_template)
            replace_page_elements(specCab_info_replace_map, row, values)
            # replace_page_links(internationalDog_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------------------------- Доступная среда  ------------------------------------------------
# ----------------------- Сведения о приспособленных объектах для проведения практических занятий -------------

def specPrac_to_list(row):
    return [row.id, row.address, row.name, row.osn, row.ovz]


def specPrac_format():
    return ['id', 'address', 'name', 'osn', 'ovz']


@csrf_exempt
def specPracs(request):
    if request.method == 'GET':
        a = SpecPrac.objects.all()
        a = [specPrac_to_list(item) for item in a]
        return JsonResponse({
            'format': specPrac_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def specPracsFormat(request):
    if request.method == 'GET':
        return JsonResponse(specPrac_format(), safe=False)


@csrf_exempt
def specPracs_by_id(request, id):
    if request.method == 'DELETE':
        obj = SpecPrac.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = SpecPrac(
            address=req_json['address'],
            name=req_json['name'],
            osn=req_json['osn'],
            ovz=req_json['ovz'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = SpecPrac.objects.get(id=id)
        obj = SpecPrac(
            id=int(id),
            address=req_json['address'],
            name=req_json['name'],
            osn=req_json['osn'],
            ovz=req_json['ovz'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


specPrac_info_replace_map = {
    'td': {
        'addressPrac': lambda obj: obj[0],
        'namePrac': lambda obj: obj[1],
        'osnPrac': lambda obj: obj[2],
        'ovzPrac': lambda obj: obj[3],
    }
}

# internationalDog_info_replace_links_map = {
#     'td': {
#         'paidParents': lambda obj: obj[1],
#         'paidParents': lambda obj: obj[2],
#         'paidParents': lambda obj: obj[3],
#         'paidParents': lambda obj: obj[4],
#     }
# }

specPrac_info_row_template = \
    '<tr itemprop="purposePrac">' \
    '<td itemprop="addressPrac"></td>' \
    '<td itemprop="namePrac"></td>' \
    '<td itemprop="osnPrac"></td>' \
    '<td itemprop="ovzPrac"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def specPracs_publish(request):
    if request.method == 'GET':
        specPracs_information = SpecPrac.objects.all()

        file = 'EmployeeApp/parser/pages/ovz/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "prac"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'purposePrac'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(specPracs_information):
            values = specPrac_to_list(item)[1:]
            row = bs4.BeautifulSoup(specPrac_info_row_template)
            replace_page_elements(specPrac_info_replace_map, row, values)
            # replace_page_links(internationalDog_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------------------------- Доступная среда  ------------------------------------------------
# ----------------------- -----------------Сведения о библиотеке ----------------------------------------------

def specLib_to_list(row):
    return [row.id, row.name, row.address, row.sq, row.cnt, row.ovz]


def specLib_format():
    return ['id', 'name', 'address', 'sq', 'cnt', 'ovz']


@csrf_exempt
def specLibs(request):
    if request.method == 'GET':
        a = SpecLib.objects.all()
        a = [specLib_to_list(item) for item in a]
        return JsonResponse({
            'format': specLib_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def specLibsFormat(request):
    if request.method == 'GET':
        return JsonResponse(specLib_format(), safe=False)


@csrf_exempt
def specLibs_by_id(request, id):
    if request.method == 'DELETE':
        obj = SpecLib.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = SpecLib(
            name=req_json['name'],
            address=req_json['address'],
            sq=req_json['sq'],
            cnt=req_json['cnt'],
            ovz=req_json['ovz'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = SpecLib.objects.get(id=id)
        obj = SpecLib(
            id=int(id),
            name=req_json['name'],
            address=req_json['address'],
            sq=req_json['sq'],
            cnt=req_json['cnt'],
            ovz=req_json['ovz'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


specLib_info_replace_map = {
    'td': {
        'objName': lambda obj: obj[0],
        'objAddress': lambda obj: obj[1],
        'objSq': lambda obj: obj[2],
        'objCnt': lambda obj: obj[3],
        'objOvz': lambda obj: obj[4],
    }
}

# internationalDog_info_replace_links_map = {
#     'td': {
#         'paidParents': lambda obj: obj[1],
#         'paidParents': lambda obj: obj[2],
#         'paidParents': lambda obj: obj[3],
#         'paidParents': lambda obj: obj[4],
#     }
# }

specLib_info_row_template = \
    '<tr itemprop="purposeLibr">' \
    '<td itemprop="objName"></td>' \
    '<td itemprop="objAddress"></td>' \
    '<td itemprop="objSq"></td>' \
    '<td itemprop="objCnt"></td>' \
    '<td itemprop="objOvz"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def specLibs_publish(request):
    if request.method == 'GET':
        specLibs_information = SpecLib.objects.all()

        file = 'EmployeeApp/parser/pages/ovz/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "lib"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'purposeLibr'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(specLibs_information):
            values = specLib_to_list(item)[1:]
            row = bs4.BeautifulSoup(specLib_info_row_template)
            replace_page_elements(specLib_info_replace_map, row, values)
            # replace_page_links(internationalDog_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------------------------- Доступная среда  ------------------------------------------------
# ---------------------------------- Сведения об объектах спорта ----------------------------------------------

def specSport_to_list(row):
    return [row.id, row.name, row.address, row.sq, row.cnt, row.ovz]


def specSport_format():
    return ['id', 'name', 'address', 'sq', 'cnt', 'ovz']


@csrf_exempt
def specSports(request):
    if request.method == 'GET':
        a = SpecSport.objects.all()
        a = [specSport_to_list(item) for item in a]
        return JsonResponse({
            'format': specSport_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def specSportsFormat(request):
    if request.method == 'GET':
        return JsonResponse(specSport_format(), safe=False)


@csrf_exempt
def specSports_by_id(request, id):
    if request.method == 'DELETE':
        obj = SpecSport.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = SpecSport(
            name=req_json['name'],
            address=req_json['address'],
            sq=req_json['sq'],
            cnt=req_json['cnt'],
            ovz=req_json['ovz'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = SpecSport.objects.get(id=id)
        obj = SpecSport(
            id=int(id),
            name=req_json['name'],
            address=req_json['address'],
            sq=req_json['sq'],
            cnt=req_json['cnt'],
            ovz=req_json['ovz'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


specSport_info_replace_map = {
    'td': {
        'objName': lambda obj: obj[0],
        'objAddress': lambda obj: obj[1],
        'objSq': lambda obj: obj[2],
        'objCnt': lambda obj: obj[3],
        'objOvz': lambda obj: obj[4],
    }
}

# internationalDog_info_replace_links_map = {
#     'td': {
#         'paidParents': lambda obj: obj[1],
#         'paidParents': lambda obj: obj[2],
#         'paidParents': lambda obj: obj[3],
#         'paidParents': lambda obj: obj[4],
#     }
# }

specSport_info_row_template = \
    '<tr itemprop="purposeSport">' \
    '<td itemprop="objName"></td>' \
    '<td itemprop="objAddress"></td>' \
    '<td itemprop="objSq"></td>' \
    '<td itemprop="objCnt"></td>' \
    '<td itemprop="objOvz"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def specSports_publish(request):
    if request.method == 'GET':
        specSports_information = SpecSport.objects.all()

        file = 'EmployeeApp/parser/pages/ovz/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "sport"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'purposeSport'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(specSports_information):
            values = specSport_to_list(item)[1:]
            row = bs4.BeautifulSoup(specSport_info_row_template)
            replace_page_elements(specSport_info_replace_map, row, values)
            # replace_page_links(internationalDog_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------------------------- Доступная среда  ------------------------------------------------
# ---------------------------------- Сведения об условиях питания обучающихся ---------------------------------

def specMeal_to_list(row):
    return [row.id, row.name, row.address, row.sq, row.cnt, row.ovz]


def specMeal_format():
    return ['id', 'name', 'address', 'sq', 'cnt', 'ovz']


@csrf_exempt
def specMeals(request):
    if request.method == 'GET':
        a = SpecMeal.objects.all()
        a = [specMeal_to_list(item) for item in a]
        return JsonResponse({
            'format': specMeal_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def specMealsFormat(request):
    if request.method == 'GET':
        return JsonResponse(specMeal_format(), safe=False)


@csrf_exempt
def specMeals_by_id(request, id):
    if request.method == 'DELETE':
        obj = SpecMeal.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = SpecMeal(
            name=req_json['name'],
            address=req_json['address'],
            sq=req_json['sq'],
            cnt=req_json['cnt'],
            ovz=req_json['ovz'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = SpecMeal.objects.get(id=id)
        obj = SpecMeal(
            id=int(id),
            name=req_json['name'],
            address=req_json['address'],
            sq=req_json['sq'],
            cnt=req_json['cnt'],
            ovz=req_json['ovz'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


specMeal_info_replace_map = {
    'td': {
        'objName': lambda obj: obj[0],
        'objAddress': lambda obj: obj[1],
        'objSq': lambda obj: obj[2],
        'objCnt': lambda obj: obj[3],
        'objOvz': lambda obj: obj[4],
    }
}

# internationalDog_info_replace_links_map = {
#     'td': {
#         'paidParents': lambda obj: obj[1],
#         'paidParents': lambda obj: obj[2],
#         'paidParents': lambda obj: obj[3],
#         'paidParents': lambda obj: obj[4],
#     }
# }

specMeal_info_row_template = \
    '<tr itemprop="meals">' \
    '<td itemprop="objName"></td>' \
    '<td itemprop="objAddress"></td>' \
    '<td itemprop="objSq"></td>' \
    '<td itemprop="objCnt"></td>' \
    '<td itemprop="objOvz"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def specMeals_publish(request):
    if request.method == 'GET':
        specMeals_information = SpecMeal.objects.all()

        file = 'EmployeeApp/parser/pages/ovz/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "meal"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'meals'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(specMeals_information):
            values = specMeal_to_list(item)[1:]
            row = bs4.BeautifulSoup(specMeal_info_row_template)
            replace_page_elements(specMeal_info_replace_map, row, values)
            # replace_page_links(internationalDog_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------------------------- Доступная среда  ------------------------------------------------
# ---------------------------- Сведения об условиях охраны здоровья обучающихся -------------------------------

def specHealth_to_list(row):
    return [row.id, row.name, row.address, row.sq, row.cnt, row.ovz]


def specHealth_format():
    return ['id', 'name', 'address', 'sq', 'cnt', 'ovz']


@csrf_exempt
def specHealths(request):
    if request.method == 'GET':
        a = SpecHealth.objects.all()
        a = [specHealth_to_list(item) for item in a]
        return JsonResponse({
            'format': specHealth_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def specHealthsFormat(request):
    if request.method == 'GET':
        return JsonResponse(specHealth_format(), safe=False)


@csrf_exempt
def specHealths_by_id(request, id):
    if request.method == 'DELETE':
        obj = SpecHealth.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = SpecHealth(
            name=req_json['name'],
            address=req_json['address'],
            sq=req_json['sq'],
            cnt=req_json['cnt'],
            ovz=req_json['ovz'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = SpecHealth.objects.get(id=id)
        obj = SpecHealth(
            id=int(id),
            name=req_json['name'],
            address=req_json['address'],
            sq=req_json['sq'],
            cnt=req_json['cnt'],
            ovz=req_json['ovz'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


specHealth_info_replace_map = {
    'td': {
        'objName': lambda obj: obj[0],
        'objAddress': lambda obj: obj[1],
        'objSq': lambda obj: obj[2],
        'objCnt': lambda obj: obj[3],
        'objOvz': lambda obj: obj[4],
    }
}

# internationalDog_info_replace_links_map = {
#     'td': {
#         'paidParents': lambda obj: obj[1],
#         'paidParents': lambda obj: obj[2],
#         'paidParents': lambda obj: obj[3],
#         'paidParents': lambda obj: obj[4],
#     }
# }

specHealth_info_row_template = \
    '<tr itemprop="health">' \
    '<td itemprop="objName"></td>' \
    '<td itemprop="objAddress"></td>' \
    '<td itemprop="objSq"></td>' \
    '<td itemprop="objCnt"></td>' \
    '<td itemprop="objOvz"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def specHealths_publish(request):
    if request.method == 'GET':
        specHealths_information = SpecHealth.objects.all()

        file = 'EmployeeApp/parser/pages/ovz/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "heal"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'health'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(specHealths_information):
            values = specHealth_to_list(item)[1:]
            row = bs4.BeautifulSoup(specHealth_info_row_template)
            replace_page_elements(specHealth_info_replace_map, row, values)
            # replace_page_links(internationalDog_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------------------------- Доступная среда  ------------------------------------------------
# ---------------------------------------------- Сведения -----------------------------------------------------

def ovz_to_list(row):
    return [row.id, row.facil_ovz, row.ovz, row.net_ovz]


def ovz_format():
    return ['id', 'facil_ovz', 'ovz', 'net_ovz']


@csrf_exempt
def ovzs(request):
    if request.method == 'GET':
        a = Ovz.objects.all()
        a = [ovz_to_list(item) for item in a]
        return JsonResponse({
            'format': ovz_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def ovzsFormat(request):
    if request.method == 'GET':
        return JsonResponse(ovz_format(), safe=False)


@csrf_exempt
def ovzs_by_id(request, id):
    if request.method == 'DELETE':
        obj = Ovz.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Ovz(
            facil_ovz=req_json['facil_ovz'],
            ovz=req_json['ovz'],
            net_ovz=req_json['net_ovz'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Ovz.objects.get(id=id)
        obj = Ovz(
            id=int(id),
            facil_ovz=req_json['facil_ovz'],
            ovz=req_json['ovz'],
            net_ovz=req_json['net_ovz'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


ovz_info_replace_map = {
    'td': {
        'purposeFacilOvz': lambda obj: obj[0],
        'ovz': lambda obj: obj[1],
        'comNetOvz': lambda obj: obj[2],
    }
}

# internationalDog_info_replace_links_map = {
#     'td': {
#         'paidParents': lambda obj: obj[1],
#         'paidParents': lambda obj: obj[2],
#         'paidParents': lambda obj: obj[3],
#         'paidParents': lambda obj: obj[4],
#     }
# }

ovz_info_row_template = \
    '<tr itemprop="ovztr">' \
    '<td itemprop="purposeFacilOvz"></td>' \
    '<td itemprop="ovz"></td>' \
    '<td itemprop="comNetOvz"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def ovzs_publish(request):
    if request.method == 'GET':
        ovzs_information = Ovz.objects.all()

        file = 'EmployeeApp/parser/pages/ovz/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "ovz"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'ovztr'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(ovzs_information):
            values = ovz_to_list(item)[1:]
            row = bs4.BeautifulSoup(ovz_info_row_template)
            replace_page_elements(ovz_info_replace_map, row, values)
            # replace_page_links(internationalDog_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------------------------- Доступная среда  ------------------------------------------------
# ---------------------- Ссылки на перечень электронных образовательных ресурсов ------------------------------

def linkOvz_to_list(row):
    return [row.id, row.name_link, row.link_ovz]


def linkOvz_format():
    return ['id', 'name_link', 'link_ovz']


@csrf_exempt
def linkOvzs(request):
    if request.method == 'GET':
        a = LinkOvz.objects.all()
        a = [linkOvz_to_list(item) for item in a]
        return JsonResponse({
            'format': linkOvz_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def linkOvzsFormat(request):
    if request.method == 'GET':
        return JsonResponse(linkOvz_format(), safe=False)


@csrf_exempt
def linkOvzs_by_id(request, id):
    if request.method == 'DELETE':
        obj = LinkOvz.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = LinkOvz(
            name_link=req_json['name_link'],
            link_ovz=req_json['link_ovz'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = LinkOvz.objects.get(id=id)
        obj = LinkOvz(
            id=int(id),
            name_link=req_json['name_link'],
            link_ovz=req_json['link_ovz'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


linkOvz_info_replace_map = {
    'td': {
        'nameLink': lambda obj: obj[0],
    }
}

linkOvz_info_replace_links_map = {
    'td': {
        'link': lambda obj: obj[1],
    }
}

linkOvz_info_row_template = \
    '<tr itemprop="erListOvz">' \
    '<td itemprop="nameLink"></td>' \
    '<td itemprop="link"><a href="">Ссылка</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def linkOvzs_publish(request):
    if request.method == 'GET':
        linkOvzs_information = LinkOvz.objects.all()

        file = 'EmployeeApp/parser/pages/ovz/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "links"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'erListOvz'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(linkOvzs_information):
            values = linkOvz_to_list(item)[1:]
            row = bs4.BeautifulSoup(linkOvz_info_row_template)
            replace_page_elements(linkOvz_info_replace_map, row, values)
            replace_page_links(linkOvz_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------------------------- Доступная среда  ------------------------------------------------
# --------------------------------------------- Сведения 2 ----------------------------------------------------

def ovzTwo_to_list(row):
    return [row.id, row.tech, row.hostel_inter, row.hostel_num, row.inter]


def ovzTwo_format():
    return ['id', 'tech', 'hostel_inter', 'hostel_num', 'inter']


@csrf_exempt
def ovzTwos(request):
    if request.method == 'GET':
        a = OvzTwo.objects.all()
        a = [ovzTwo_to_list(item) for item in a]
        return JsonResponse({
            'format': ovzTwo_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def ovzTwosFormat(request):
    if request.method == 'GET':
        return JsonResponse(ovzTwo_format(), safe=False)


@csrf_exempt
def ovzTwos_by_id(request, id):
    if request.method == 'DELETE':
        obj = OvzTwo.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = OvzTwo(
            tech=req_json['tech'],
            hostel_inter=req_json['hostel_inter'],
            hostel_num=req_json['hostel_num'],
            inter=req_json['inter'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = OvzTwo.objects.get(id=id)
        obj = OvzTwo(
            id=int(id),
            tech=req_json['tech'],
            hostel_inter=req_json['hostel_inter'],
            hostel_num=req_json['hostel_num'],
            inter=req_json['inter'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


ovzTwo_info_replace_map = {
    'td': {
        'techOvz': lambda obj: obj[0],
        'hostelInterOvz': lambda obj: obj[1],
        'hostelNumOvz': lambda obj: obj[2],
        'interNumOvz': lambda obj: obj[3],
    }
}

# ovzTwo_info_replace_links_map = {
#     'td': {
#         'link': lambda obj: obj[1],
#     }
# }

ovzTwo_info_row_template = \
    '<tr itemprop="ovzTwo">' \
    '<td itemprop="techOvz"></td>' \
    '<td itemprop="hostelInterOvz"></td>' \
    '<td itemprop="hostelNumOvz"></td>' \
    '<td itemprop="interNumOvz"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def ovzTwos_publish(request):
    if request.method == 'GET':
        ovzTwos_information = OvzTwo.objects.all()

        file = 'EmployeeApp/parser/pages/ovz/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "ovzTwos"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'ovzTwo'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(ovzTwos_information):
            values = ovzTwo_to_list(item)[1:]
            row = bs4.BeautifulSoup(ovzTwo_info_row_template)
            replace_page_elements(ovzTwo_info_replace_map, row, values)
            # replace_page_links(ovzTwo_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------- Стипендии и иные виды материальной поддержки ---------------------------------
# --- ЛОКАЛЬНЫЕ НОРМАТИВНЫЕ АКТЫ, КОТОРЫМИ РЕГЛАМЕНТИРУЮТСЯ НАЛИЧИЕ И УСЛОВИЯ ПРЕДОСТАВЛЕНИЯ СТИПЕНДИЙ ---

def grant_to_list(row):
    return [row.id, row.filename]


def grant_format():
    return ['id', 'filename']


@csrf_exempt
def grants(request):
    if request.method == 'GET':
        a = Grants.objects.all()
        a = [grant_to_list(item) for item in a]
        return JsonResponse({
            'format': grant_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def grantsFormat(request):
    if request.method == 'GET':
        return JsonResponse(grant_format(), safe=False)


@csrf_exempt
def grants_by_id(request, id):
    if request.method == 'DELETE':
        obj = Grants.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Grants(
            filename=req_json['filename'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Grants.objects.get(id=id)
        obj = Grants(
            id=int(id),
            filename=req_json['filename'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


# grant_info_replace_map = {
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

grant_info_replace_links_map = {
    'td': {
        'localAct': lambda obj: obj[0],
    }
}


grant_info_row_template = \
    '<tr itemprop="act">' \
    '<td itemprop="localAct"><a href="" download="">Ссылка на локальный нормативный акт</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def grants_publish(request):
    if request.method == 'GET':
        grants_information = Grants.objects.all()

        file = 'EmployeeApp/parser/pages/grants/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "acts"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'act'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(grants_information):
            values = grant_to_list(item)[1:]
            row = bs4.BeautifulSoup(grant_info_row_template)
            # replace_page_elements(grant_info_replace_map, row, values)
            replace_page_links(grant_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------- Стипендии и иные виды материальной поддержки ---------------------------------
# ----------------------------------------- Информация ---------------------------------------------------

def grantInfo_to_list(row):
    return [
            row.id,
            row.grant,
            row.support,
            row.hostel_info, row.inter_info,
            row.hostel_ts, row.inter_ts,
            row.hostel_ls, row.inter_ls,
            row.hostel_num, row.inter_num,
            row.hostel_inv, row.inter_inv,
            row.hostel_fd, row.inter_fd
            ]


def grantInfo_format():
    return ['id', 'grant', 'support', 'hostel_info', 'inter_info', 'hostel_ts', 'inter_ts', 'hostel_ls', 'inter_ls',
            'hostel_num', 'inter_num', 'hostel_inv', 'inter_inv', 'hostel_fd', 'inter_fd']


@csrf_exempt
def grantInfos(request):
    if request.method == 'GET':
        a = GrantInfo.objects.all()
        a = [grantInfo_to_list(item) for item in a]
        return JsonResponse({
            'format': grantInfo_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def grantInfosFormat(request):
    if request.method == 'GET':
        return JsonResponse(grantInfo_format(), safe=False)


@csrf_exempt
def grantInfos_by_id(request, id):
    if request.method == 'DELETE':
        obj = GrantInfo.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = GrantInfo(
            grant=req_json['grant'],
            support=req_json['support'],
            hostel_info=req_json['hostel_info'],
            inter_info=req_json['inter_info'],
            hostel_ts=req_json['hostel_ts'],
            inter_ts=req_json['inter_ts'],
            hostel_ls=req_json['hostel_ls'],
            inter_ls=req_json['inter_ls'],
            hostel_num=req_json['hostel_num'],
            inter_num=req_json['inter_num'],
            hostel_inv=req_json['hostel_inv'],
            inter_inv=req_json['inter_inv'],
            hostel_fd=req_json['hostel_fd'],
            inter_fd=req_json['inter_fd'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = GrantInfo.objects.get(id=id)
        obj = GrantInfo(
            id=int(id),
            grant=req_json['grant'],
            support=req_json['support'],
            hostel_info=req_json['hostel_info'],
            inter_info=req_json['inter_info'],
            hostel_ts=req_json['hostel_ts'],
            inter_ts=req_json['inter_ts'],
            hostel_ls=req_json['hostel_ls'],
            inter_ls=req_json['inter_ls'],
            hostel_num=req_json['hostel_num'],
            inter_num=req_json['inter_num'],
            hostel_inv=req_json['hostel_inv'],
            inter_inv=req_json['inter_inv'],
            hostel_fd=req_json['hostel_fd'],
            inter_fd=req_json['inter_fd'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


grantInfo_info_replace_map = {
    'td': {
        'grant': lambda obj: obj[0],
        'support': lambda obj: obj[1],
        'hostelInfo': lambda obj: obj[2],
        'interInfo': lambda obj: obj[3],
        'hostelTS': lambda obj: obj[4],
        'interTS': lambda obj: obj[5],
        'hostelLS': lambda obj: obj[6],
        'interLS': lambda obj: obj[7],
        'hostelNum': lambda obj: obj[8],
        'hostelInv': lambda obj: obj[9],
        'interInv': lambda obj: obj[10],
        'hostelFd': lambda obj: obj[11],
        'interFd': lambda obj: obj[12],
    }
}

grantInfo_info_row_template = \
    '<tr itemprop="infor">' \
    '<td itemprop="grant"></td>' \
    '<td itemprop="support"></td>' \
    '<td itemprop="hostelInfo"></td>' \
    '<td itemprop="interInfo"></td>' \
    '<td itemprop="hostelTS"></td>' \
    '<td itemprop="interTS"></td>' \
    '<td itemprop="hostelLS"></td>' \
    '<td id="its"></td>' \
    '<td itemprop="hostelNum"></td>' \
    '<td itemprop="hostelInv"></td>' \
    '<td itemprop="interInv"></td>' \
    '<td itemprop="hostelFd"></td>' \
    '<td itemprop="interFd"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def grantInfos_publish(request):
    if request.method == 'GET':
        grantInfos_information = GrantInfo.objects.all()

        file = 'EmployeeApp/parser/pages/grants/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "inf"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'infor'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(grantInfos_information):
            values = grantInfo_to_list(item)[1:]
            row = bs4.BeautifulSoup(grantInfo_info_row_template)
            replace_page_elements(grantInfo_info_replace_map, row, values)
            # replace_page_links(grant_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------- Стипендии и иные виды материальной поддержки ---------------------------------
# --- Копия локального нормативного акта, регламентирующего размер платы за пользование жилым помещением и коммунальные услуги в общежитии ---

def act_to_list(row):
    return [row.id, row.filename]


def act_format():
    return ['id', 'filename']


@csrf_exempt
def acts(request):
    if request.method == 'GET':
        a = Acts.objects.all()
        a = [act_to_list(item) for item in a]
        return JsonResponse({
            'format': act_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def actsFormat(request):
    if request.method == 'GET':
        return JsonResponse(act_format(), safe=False)


@csrf_exempt
def acts_by_id(request, id):
    if request.method == 'DELETE':
        obj = Acts.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Acts(
            filename=req_json['filename'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Acts.objects.get(id=id)
        obj = Acts(
            id=int(id),
            filename=req_json['filename'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


# grant_info_replace_map = {
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

act_info_replace_links_map = {
    'td': {
        'localAct': lambda obj: obj[0],
    }
}


act_info_row_template = \
    '<tr itemprop="local">' \
    '<td itemprop="localAct"><a href="" download="">Копия локального нормативного акта, регламентирующего размер платы за пользование жилым помещением и коммунальные услуги в общежитии</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def acts_publish(request):
    if request.method == 'GET':
        acts_information = Acts.objects.all()

        file = 'EmployeeApp/parser/pages/grants/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "localCopy"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'local'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(acts_information):
            values = act_to_list(item)[1:]
            row = bs4.BeautifulSoup(act_info_row_template)
            # replace_page_elements(grant_info_replace_map, row, values)
            replace_page_links(act_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ------------------------- Стипендии и иные виды материальной поддержки ---------------------------------
# --------------------------- Информация о трудоустройстве выпускников -----------------------------------

def job_to_list(row):
    return [row.id, row.code, row.name, row.numgrad, row.numworkgrad, row.numgrad1, row.numworkgrad1, row.numgrad2, row.numworkgrad2]


def job_format():
    return ['id', 'code', 'name', 'numgrad', 'numworkgrad', 'numgrad1', 'numworkgrad1', 'numgrad2', 'numworkgrad2']


@csrf_exempt
def jobs(request):
    if request.method == 'GET':
        a = Jobs.objects.all()
        a = [job_to_list(item) for item in a]
        return JsonResponse({
            'format': job_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def jobsFormat(request):
    if request.method == 'GET':
        return JsonResponse(job_format(), safe=False)


@csrf_exempt
def jobs_by_id(request, id):
    if request.method == 'DELETE':
        obj = Jobs.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Jobs(
            code=req_json['code'],
            name=req_json['name'],
            numgrad=req_json['numgrad'],
            numworkgrad=req_json['numworkgrad'],
            numgrad1=req_json['numgrad1'],
            numworkgrad1=req_json['numworkgrad1'],
            numgrad2=req_json['numgrad2'],
            numworkgrad2=req_json['numworkgrad2'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Jobs.objects.get(id=id)
        obj = Jobs(
            id=int(id),
            code=req_json['code'],
            name=req_json['name'],
            numgrad=req_json['numgrad'],
            numworkgrad=req_json['numworkgrad'],
            numgrad1=req_json['numgrad1'],
            numworkgrad1=req_json['numworkgrad1'],
            numgrad2=req_json['numgrad2'],
            numworkgrad2=req_json['numworkgrad2'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


job_info_replace_map = {
    'td': {
        'eduCode': lambda obj: obj[0],
        'eduName': lambda obj: obj[1],
        'v1': lambda obj: obj[2],
        't1': lambda obj: obj[3],
        'v2': lambda obj: obj[4],
        't2': lambda obj: obj[5],
        'v3': lambda obj: obj[6],
        't3': lambda obj: obj[7],
    }
}


job_info_row_template = \
    '<tr itemprop="graduateJob">' \
    '<td itemprop="eduCode"></td>' \
    '<td itemprop="eduName"></td>' \
    '<td itemprop="v1"></td>' \
    '<td itemprop="t1"></td>' \
    '<td itemprop="v2"></td>' \
    '<td itemprop="t2"></td>' \
    '<td itemprop="v3"></td>' \
    '<td itemprop="t3"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def jobs_publish(request):
    if request.method == 'GET':
        jobs_information = Jobs.objects.all()

        file = 'EmployeeApp/parser/pages/grants/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "info"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'graduateJob'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(jobs_information):
            values = job_to_list(item)[1:]
            row = bs4.BeautifulSoup(job_info_row_template)
            replace_page_elements(job_info_replace_map, row, values)
            # replace_page_links(grant_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ----------------------------------------------- ОБРАЗОВАНИЕ -----------------------------------------------------
# Информация о реализуемых уровнях образования, о формах обучения, нормативных сроках обучения,
# сроке действия государственной аккредитации образовательной программы (при наличии государственной аккредитации),
# о языках, на которых осуществляется образование (обучение)

def gosAccreditation_to_list(row):
    return [row.id, row.code, row.name, row.level, row.expdate, row.language, row.trainterm, row.column]


def gosAccreditation_format():
    return ['id', 'code', 'name', 'level', 'expdate', 'language', 'trainterm', 'column']


@csrf_exempt
def gosAccreditations(request):
    if request.method == 'GET':
        a = GosAccreditations.objects.all()
        a = [gosAccreditation_to_list(item) for item in a]
        return JsonResponse({
            'format': gosAccreditation_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def gosAccreditationsFormat(request):
    if request.method == 'GET':
        return JsonResponse(gosAccreditation_format(), safe=False)


@csrf_exempt
def gosAccreditations_by_id(request, id):
    if request.method == 'DELETE':
        obj = GosAccreditations.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = GosAccreditations(
            code=req_json['code'],
            name=req_json['name'],
            level=req_json['level'],
            expdate=req_json['expdate'],
            language=req_json['language'],
            trainterm=req_json['trainterm'],
            column=req_json['column'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = GosAccreditations.objects.get(id=id)
        obj = GosAccreditations(
            id=int(id),
            code=req_json['code'],
            name=req_json['name'],
            level=req_json['level'],
            expdate=req_json['expdate'],
            language=req_json['language'],
            trainterm=req_json['trainterm'],
            column=req_json['column'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


gosAccreditation_info_replace_map = {
    'td': {
        'eduCode': lambda obj: obj[0],
        'eduName': lambda obj: obj[1],
        'eduLevel': lambda obj: obj[2],
        'eduForm': lambda obj: obj[3],
        'learningTerm': lambda obj: obj[4],
        'dateEnd': lambda obj: obj[5],
        'language': lambda obj: obj[6],
    }
}


gosAccreditation_info_row_template = \
    '<tr itemprop="eduAccred">' \
    '<td itemprop="eduCode"></td>' \
    '<td itemprop="eduName"></td>' \
    '<td itemprop="eduLevel"></td>' \
    '<td itemprop="eduForm"></td>' \
    '<td itemprop="learningTerm"></td>' \
    '<td itemprop="dateEnd"></td>' \
    '<td itemprop="language"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def gosAccreditations_publish(request):
    if request.method == 'GET':
        gosAccreditations_information = GosAccreditations.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/education/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "gos"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'eduAccred'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(gosAccreditations_information):
            values = gosAccreditation_to_list(item)[1:]
            row = bs4.BeautifulSoup(gosAccreditation_info_row_template)
            replace_page_elements(gosAccreditation_info_replace_map, row, values)
            # replace_page_links(grant_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ----------------------------------------------- ОБРАЗОВАНИЕ -----------------------------------------------------
# Сведения о профессионально-общественной аккредитации образовательной программы (при наличии)

def prof_to_list(row):
    return [row.id, row.code, row.name, row.name_accr, row.time]


def prof_format():
    return ['id', 'code', 'name', 'name_accr', 'time']


@csrf_exempt
def profs(request):
    if request.method == 'GET':
        a = Prof.objects.all()
        a = [prof_to_list(item) for item in a]
        return JsonResponse({
            'format': prof_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def profsFormat(request):
    if request.method == 'GET':
        return JsonResponse(prof_format(), safe=False)


@csrf_exempt
def profs_by_id(request, id):
    if request.method == 'DELETE':
        obj = Prof.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Prof(
            code=req_json['code'],
            name=req_json['name'],
            name_accr=req_json['name_accr'],
            time=req_json['time'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Prof.objects.get(id=id)
        obj = Prof(
            id=int(id),
            code=req_json['code'],
            name=req_json['name'],
            name_accr=req_json['name_accr'],
            time=req_json['time'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


prof_info_replace_map = {
    'td': {
        'eduCode': lambda obj: obj[0],
        'eduName': lambda obj: obj[1],
        'orgName': lambda obj: obj[2],
        'dateEnd': lambda obj: obj[3],
    }
}


prof_info_row_template = \
    '<tr itemprop="eduPOAccred">' \
    '<td itemprop="eduCode"></td>' \
    '<td itemprop="eduName"></td>' \
    '<td itemprop="orgName"></td>' \
    '<td itemprop="dateEnd"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def profs_publish(request):
    if request.method == 'GET':
        profs_information = Prof.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/education/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "prof"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'eduPOAccred'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(profs_information):
            values = prof_to_list(item)[1:]
            row = bs4.BeautifulSoup(prof_info_row_template)
            replace_page_elements(prof_info_replace_map, row, values)
            # replace_page_links(grant_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ----------------------------------------------- ОБРАЗОВАНИЕ -----------------------------------------------------
# Информация о численности обучающихся по реализуемым образовательным программам по источникам финансирования

def inf_to_list(row):
    return [row.id, row.code, row.name, row.level, row.form, row.number_bf, row.number_br, row.number_bm, row.number_p, row.number_f]


def inf_format():
    return ['id', 'code', 'name', 'level', 'form', 'number_bf', 'number_br', 'number_bm', 'number_p', 'number_f']


@csrf_exempt
def infs(request):
    if request.method == 'GET':
        a = InfChi.objects.all()
        a = [inf_to_list(item) for item in a]
        return JsonResponse({
            'format': inf_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def infsFormat(request):
    if request.method == 'GET':
        return JsonResponse(inf_format(), safe=False)


@csrf_exempt
def infs_by_id(request, id):
    if request.method == 'DELETE':
        obj = InfChi.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = InfChi(
            code=req_json['code'],
            name=req_json['name'],
            level=req_json['level'],
            form=req_json['form'],
            number_bf=req_json['number_bf'],
            number_br=req_json['number_br'],
            number_bm=req_json['number_bm'],
            number_p=req_json['number_p'],
            number_f=req_json['number_f'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = InfChi.objects.get(id=id)
        obj = InfChi(
            id=int(id),
            code=req_json['code'],
            name=req_json['name'],
            level=req_json['level'],
            form=req_json['form'],
            number_bf=req_json['number_bf'],
            number_br=req_json['number_br'],
            number_bm=req_json['number_bm'],
            number_p=req_json['number_p'],
            number_f=req_json['number_f'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


inf_info_replace_map = {
    'td': {
        'eduCode': lambda obj: obj[0],
        'eduName': lambda obj: obj[1],
        'eduLevel': lambda obj: obj[2],
        'eduForm': lambda obj: obj[3],
        'numberBF': lambda obj: obj[4],
        'numberBR': lambda obj: obj[5],
        'numberBM': lambda obj: obj[6],
        'numberP': lambda obj: obj[7],
        'numberF': lambda obj: obj[8],
    }
}


inf_info_row_template = \
    '<tr itemprop="eduChislen">' \
    '<td itemprop="eduCode"></td>' \
    '<td itemprop="eduName"></td>' \
    '<td itemprop="eduLevel"></td>' \
    '<td itemprop="eduForm"></td>' \
    '<td itemprop="numberBF"></td>' \
    '<td itemprop="numberBR"></td>' \
    '<td itemprop="numberBM"></td>' \
    '<td itemprop="numberP"></td>' \
    '<td itemprop="numberF"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def infs_publish(request):
    if request.method == 'GET':
        infs_information = InfChi.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/education/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "inf"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'eduChislen'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(infs_information):
            values = inf_to_list(item)[1:]
            row = bs4.BeautifulSoup(inf_info_row_template)
            replace_page_elements(inf_info_replace_map, row, values)
            # replace_page_links(grant_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ----------------------------------------------- ОБРАЗОВАНИЕ -----------------------------------------------------
# Информация о результатах приема

def admis_to_list(row):
    return [row.id, row.code, row.name, row.level, row.studyform, row.budgetfederal, row.budgetrus, row.budgetplace, row.budgetfiz, row.summ]


def admis_format():
    return ['id', 'code', 'name', 'level', 'studyform', 'budgetfederal', 'budgetrus', 'budgetplace', 'budgetfiz', 'summ']


@csrf_exempt
def admiss(request):
    if request.method == 'GET':
        a = AdmissionResults.objects.all()
        a = [admis_to_list(item) for item in a]
        return JsonResponse({
            'format': admis_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def admissFormat(request):
    if request.method == 'GET':
        return JsonResponse(admis_format(), safe=False)


@csrf_exempt
def admiss_by_id(request, id):
    if request.method == 'DELETE':
        obj = AdmissionResults.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = AdmissionResults(
            code=req_json['code'],
            name=req_json['name'],
            level=req_json['level'],
            studyform=req_json['studyform'],
            budgetfederal=req_json['budgetfederal'],
            budgetrus=req_json['budgetrus'],
            budgetplace=req_json['budgetplace'],
            budgetfiz=req_json['budgetfiz'],
            summ=req_json['summ'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = AdmissionResults.objects.get(id=id)
        obj = AdmissionResults(
            id=int(id),
            code=req_json['code'],
            name=req_json['name'],
            level=req_json['level'],
            studyform=req_json['studyform'],
            budgetfederal=req_json['budgetfederal'],
            budgetrus=req_json['budgetrus'],
            budgetplace=req_json['budgetplace'],
            budgetfiz=req_json['budgetfiz'],
            summ=req_json['summ'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


admis_info_replace_map = {
    'td': {
        'eduCode': lambda obj: obj[0],
        'eduName': lambda obj: obj[1],
        'eduLevel': lambda obj: obj[2],
        'eduForm': lambda obj: obj[3],
        'numberBF': lambda obj: obj[4],
        'numberBR': lambda obj: obj[5],
        'numberBM': lambda obj: obj[6],
        'numberP': lambda obj: obj[7],
        'score': lambda obj: obj[8],
    }
}


admis_info_row_template = \
    '<tr itemprop="eduPriem">' \
    '<td itemprop="eduCode"></td>' \
    '<td itemprop="eduName"></td>' \
    '<td itemprop="eduLevel"></td>' \
    '<td itemprop="eduForm"></td>' \
    '<td itemprop="numberBF"></td>' \
    '<td itemprop="numberBR"></td>' \
    '<td itemprop="numberBM"></td>' \
    '<td itemprop="numberP"></td>' \
    '<td itemprop="score"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def admiss_publish(request):
    if request.method == 'GET':
        admiss_information = AdmissionResults.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/education/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "admis"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'eduPriem'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(admiss_information):
            values = admis_to_list(item)[1:]
            row = bs4.BeautifulSoup(admis_info_row_template)
            replace_page_elements(admis_info_replace_map, row, values)
            # replace_page_links(grant_admiso_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_admisormation_replace_map, page_parser, admisormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ----------------------------------------------- ОБРАЗОВАНИЕ -----------------------------------------------------
# Информация о результатах перевода, восстановления и отчисления

def perev_to_list(row):
    return [row.id, row.code, row.name, row.level, row.form, row.out, row.to, row.res, row.exp]


def perev_format():
    return ['id', 'code', 'name', 'level', 'form', 'out', 'to', 'res', 'exp']


@csrf_exempt
def perevs(request):
    if request.method == 'GET':
        a = Perevod.objects.all()
        a = [perev_to_list(item) for item in a]
        return JsonResponse({
            'format': perev_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def perevsFormat(request):
    if request.method == 'GET':
        return JsonResponse(perev_format(), safe=False)


@csrf_exempt
def perevs_by_id(request, id):
    if request.method == 'DELETE':
        obj = Perevod.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Perevod(
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
        obj_old = Perevod.objects.get(id=id)
        obj = Perevod(
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


perev_info_replace_map = {
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


perev_info_row_template = \
    '<tr itemprop="eduPerevod">' \
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
def perevs_publish(request):
    if request.method == 'GET':
        perevs_information = Perevod.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/education/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "perevod"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'eduPerevod'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(perevs_information):
            values = perev_to_list(item)[1:]
            row = bs4.BeautifulSoup(perev_info_row_template)
            replace_page_elements(perev_info_replace_map, row, values)
            # replace_page_links(grant_perevo_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_perevormation_replace_map, page_parser, perevormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ----------------------------------------------- ОБРАЗОВАНИЕ -----------------------------------------------------
# Информация об образовательной программе

def obraz_to_list(row):
    return [row.id, row.code, row.name, row.level, row.form, row.main, row.plan, row.annot, row.shed, row.method, row.pr, row.el]


def obraz_format():
    return ['id', 'code', 'name', 'level', 'form', 'main', 'plan', 'annot', 'shed', 'method', 'pr', 'el']


@csrf_exempt
def obrazs(request):
    if request.method == 'GET':
        a = Obraz.objects.all()
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
        obj = Obraz.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Obraz(
            code=req_json['code'],
            name=req_json['name'],
            level=req_json['level'],
            form=req_json['form'],
            main=req_json['main'],
            plan=req_json['plan'],
            annot=req_json['annot'],
            shed=req_json['shed'],
            method=req_json['method'],
            pr=req_json['pr'],
            el=req_json['el'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Obraz.objects.get(id=id)
        obj = Obraz(
            id=int(id),
            code=req_json['code'],
            name=req_json['name'],
            level=req_json['level'],
            form=req_json['form'],
            main=req_json['main'],
            plan=req_json['plan'],
            annot=req_json['annot'],
            shed=req_json['shed'],
            method=req_json['method'],
            pr=req_json['pr'],
            el=req_json['el'],
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
        'eduEl': lambda obj: obj[10],
    }
}


obraz_info_replace_links_map = {
    'td': {
        'opMain': lambda obj: obj[4],
        'educationPlan': lambda obj: obj[5],
        'educationAnnotation': lambda obj: obj[6],
        'educationShedule': lambda obj: obj[7],
        'methodology': lambda obj: obj[8],
        'eduPr': lambda obj: obj[9],
    }
}

obraz_info_row_template = \
    '<tr itemprop="eduOp">' \
    '<td itemprop="eduCode"></td>' \
    '<td itemprop="eduName"></td>' \
    '<td itemprop="eduLevel"></td>' \
    '<td itemprop="eduForm"></td>' \
    '<td itemprop="opMain"><a href="">Ссылка</a></td>' \
    '<td itemprop="educationPlan"><a href="">Ссылка</a></td>' \
    '<td itemprop="educationAnnotation"><a href="">Ссылка</a></td>' \
    '<td itemprop="educationShedule"><a href="">Ссылка</a></td>' \
    '<td itemprop="methodology"><a href="">Ссылка</a></td>' \
    '<td itemprop="eduPr"><a href="">Ссылка</a></td>' \
    '<td itemprop="eduEl"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def obrazs_publish(request):
    if request.method == 'GET':
        obrazs_information = Obraz.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/education/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "obraz"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'eduOp'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(obrazs_information):
            values = obraz_to_list(item)[1:]
            row = bs4.BeautifulSoup(obraz_info_row_template)
            replace_page_elements(obraz_info_replace_map, row, values)
            replace_page_links(obraz_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_obrazormation_replace_map, page_parser, obrazormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ----------------------------------------------- ОБРАЗОВАНИЕ -----------------------------------------------------
# Информация об адаптированной образовательной программе

def practic_to_list(row):
    return [row.id, row.code, row.name, row.profile, row.studyforms, row.opis_obraz, row.uch_plan, row.annot_link, row.calend_link, row.norm_doc, row.inf_pract, row.inf_isp]


def practic_format():
    return ['id', 'code', 'name', 'profile', 'studyforms', 'opis_obraz', 'uch_plan', 'annot_link', 'calend_link', 'norm_doc', 'inf_pract', 'inf_isp']


@csrf_exempt
def practics(request):
    if request.method == 'GET':
        a = Practices.objects.all()
        a = [practic_to_list(item) for item in a]
        return JsonResponse({
            'format': practic_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def practicsFormat(request):
    if request.method == 'GET':
        return JsonResponse(practic_format(), safe=False)


@csrf_exempt
def practics_by_id(request, id):
    if request.method == 'DELETE':
        obj = Practices.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Practices(
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
        obj_old = Practices.objects.get(id=id)
        obj = Practices(
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


practic_info_replace_map = {
    'td': {
        'eduCode': lambda obj: obj[0],
        'eduName': lambda obj: obj[1],
        'eduLevel': lambda obj: obj[2],
        'eduForm': lambda obj: obj[3],
        'eduEl': lambda obj: obj[10],
    }
}


practic_info_replace_links_map = {
    'td': {
        'opMain': lambda obj: obj[4],
        'educationPlan': lambda obj: obj[5],
        'educationAnnotation': lambda obj: obj[6],
        'educationShedule': lambda obj: obj[7],
        'methodology': lambda obj: obj[8],
        'eduPr': lambda obj: obj[9],
    }
}

practic_info_row_template = \
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
def practics_publish(request):
    if request.method == 'GET':
        practics_information = Practices.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/education/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "practices"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'eduAdOp'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(practics_information):
            values = practic_to_list(item)[1:]
            row = bs4.BeautifulSoup(practic_info_row_template)
            replace_page_elements(practic_info_replace_map, row, values)
            replace_page_links(practic_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_practicormation_replace_map, page_parser, practicormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ----------------------------------------------- ОБРАЗОВАНИЕ -----------------------------------------------------
# Информация о направлениях и результатах научной (научно-исследовательской) деятельности

def scienc_to_list(row):
    return [row.id, row.code, row.name, row.level, row.listdirections, row.result_nir, row.information]


def scienc_format():
    return ['id', 'code', 'name', 'level', 'listdirections', 'result_nir', 'information']


@csrf_exempt
def sciencs(request):
    if request.method == 'GET':
        a = ScienceResults.objects.all()
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
        obj = ScienceResults.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = ScienceResults(
            code=req_json['code'],
            name=req_json['name'],
            level=req_json['level'],
            listdirections=req_json['listdirections'],
            result_nir=req_json['result_nir'],
            information=req_json['information'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = ScienceResults.objects.get(id=id)
        obj = ScienceResults(
            id=int(id),
            code=req_json['code'],
            name=req_json['name'],
            level=req_json['level'],
            listdirections=req_json['listdirections'],
            result_nir=req_json['result_nir'],
            information=req_json['information'],
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
        'perechenNir': lambda obj: obj[3],
        'baseNir': lambda obj: obj[5],
    }
}


scienc_info_replace_links_map = {
    'td': {
        'resultNir': lambda obj: obj[4],
    }
}

scienc_info_row_template = \
    '<tr itemprop="eduNir">' \
    '<td itemprop="eduCode"></td>' \
    '<td itemprop="eduName"></td>' \
    '<td itemprop="eduLevel"></td>' \
    '<td itemprop="perechenNir"></td>' \
    '<td itemprop="resultNir"><a href="" download="">Положение</a></td>' \
    '<td itemprop="baseNir"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def sciencs_publish(request):
    if request.method == 'GET':
        sciencs_information = ScienceResults.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/education/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "sciences"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'eduNir'})

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


# -------------------- Материально-техническое обеспечение и оснащенность образовательного процесса -------------------
# Сведения о каждом месте осуществления образовательной деятельности, в том числе не указываемых в соответствии с частью
# 4 статьи 91 Федерального закона от 29.12.2012 N 273-ФЗ "Об образовании в Российской Федерации"
# (Собрание законодательства Российской Федерации, 2012, N 53, ст. 7598; 2019, N 49, ст. 6962) в приложении к лицензии на
# осуществление образовательной деятельности

def svedOrg_to_list(row):
    return [row.id, row.number, row.address]


def svedOrg_format():
    return ['id', 'number', 'address']


@csrf_exempt
def svedOrgs(request):
    if request.method == 'GET':
        a = SvedOrg.objects.all()
        a = [svedOrg_to_list(item) for item in a]
        return JsonResponse({
            'format': svedOrg_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def svedOrgsFormat(request):
    if request.method == 'GET':
        return JsonResponse(svedOrg_format(), safe=False)


@csrf_exempt
def svedOrgs_by_id(request, id):
    if request.method == 'DELETE':
        obj = SvedOrg.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = SvedOrg(
            number=req_json['number'],
            address=req_json['address'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = SvedOrg.objects.get(id=id)
        obj = SvedOrg(
            id=int(id),
            number=req_json['number'],
            address=req_json['address'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


svedOrg_info_replace_map = {
    'td': {
        'number': lambda obj: obj[0],
        'address': lambda obj: obj[1],
    }
}


# svedOrg_info_replace_links_map = {
#     'td': {
#         'resultNir': lambda obj: obj[4],
#     }
# }

svedOrg_info_row_template = \
    '<tr itemprop="addressPlace">' \
    '<td itemprop="number"></td>' \
    '<td itemprop="address"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def svedOrgs_publish(request):
    if request.method == 'GET':
        svedOrgs_information = SvedOrg.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/objects/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "place"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'addressPlace'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(svedOrgs_information):
            values = svedOrg_to_list(item)[1:]
            row = bs4.BeautifulSoup(svedOrg_info_row_template)
            replace_page_elements(svedOrg_info_replace_map, row, values)
            # replace_page_links(svedOrg_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_sciencormation_replace_map, page_parser, sciencormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# -------------------- Материально-техническое обеспечение и оснащенность образовательного процесса -------------------
# Сведения о наличии оборудованных учебных кабинетов

def facilit_to_list(row):
    return [row.id, row.address, row.special_premises, row.equipment]


def facilit_format():
    return ['id', 'address', 'special_premises', 'equipment']


@csrf_exempt
def facilits(request):
    if request.method == 'GET':
        a = Facilities.objects.all()
        a = [facilit_to_list(item) for item in a]
        return JsonResponse({
            'format': facilit_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def facilitsFormat(request):
    if request.method == 'GET':
        return JsonResponse(facilit_format(), safe=False)


@csrf_exempt
def facilits_by_id(request, id):
    if request.method == 'DELETE':
        obj = Facilities.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Facilities(
            address=req_json['address'],
            special_premises=req_json['special_premises'],
            equipment=req_json['equipment'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Facilities.objects.get(id=id)
        obj = Facilities(
            id=int(id),
            address=req_json['address'],
            special_premises=req_json['special_premises'],
            equipment=req_json['equipment'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


facilit_info_replace_map = {
    'td': {
        'addressCab': lambda obj: obj[0],
        'nameCab': lambda obj: obj[1],
        'osnCab': lambda obj: obj[2],
    }
}


# facilit_info_replace_links_map = {
#     'td': {
#         'resultNir': lambda obj: obj[4],
#     }
# }

facilit_info_row_template = \
    '<tr itemprop="purposeCab">' \
    '<td itemprop="addressCab"></td>' \
    '<td itemprop="nameCab"></td>' \
    '<td itemprop="osnCab"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def facilits_publish(request):
    if request.method == 'GET':
        facilits_information = Facilities.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/objects/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "purCab"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'purposeCab'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(facilits_information):
            values = facilit_to_list(item)[1:]
            row = bs4.BeautifulSoup(facilit_info_row_template)
            replace_page_elements(facilit_info_replace_map, row, values)
            # replace_page_links(facilit_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_sciencormation_replace_map, page_parser, sciencormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# -------------------- Материально-техническое обеспечение и оснащенность образовательного процесса -------------------
# Сведения о наличии объектов для проведения практических занятий

def objPract_to_list(row):
    return [row.id, row.address, row.name, row.pract]


def objPract_format():
    return ['id', 'address', 'name', 'pract']


@csrf_exempt
def objPracts(request):
    if request.method == 'GET':
        a = ObjPract.objects.all()
        a = [objPract_to_list(item) for item in a]
        return JsonResponse({
            'format': objPract_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def objPractsFormat(request):
    if request.method == 'GET':
        return JsonResponse(objPract_format(), safe=False)


@csrf_exempt
def objPracts_by_id(request, id):
    if request.method == 'DELETE':
        obj = ObjPract.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = ObjPract(
            address=req_json['address'],
            name=req_json['name'],
            pract=req_json['pract'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = ObjPract.objects.get(id=id)
        obj = ObjPract(
            id=int(id),
            address=req_json['address'],
            name=req_json['name'],
            pract=req_json['pract'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


objPract_info_replace_map = {
    'td': {
        'addressPrac': lambda obj: obj[0],
        'namePrac': lambda obj: obj[1],
        'osnPrac': lambda obj: obj[2],
    }
}


# objPract_info_replace_links_map = {
#     'td': {
#         'resultNir': lambda obj: obj[4],
#     }
# }

objPract_info_row_template = \
    '<tr itemprop="purposePrac">' \
    '<td itemprop="addressPrac"></td>' \
    '<td itemprop="namePrac"></td>' \
    '<td itemprop="osnPrac"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def objPracts_publish(request):
    if request.method == 'GET':
        objPracts_information = ObjPract.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/objects/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "purposePr"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'purposePrac'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(objPracts_information):
            values = objPract_to_list(item)[1:]
            row = bs4.BeautifulSoup(objPract_info_row_template)
            replace_page_elements(objPract_info_replace_map, row, values)
            # replace_page_links(objPract_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_sciencormation_replace_map, page_parser, sciencormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# -------------------- Материально-техническое обеспечение и оснащенность образовательного процесса -------------------
# Сведения наличии библиотек

def librare_to_list(row):
    return [row.id, row.types, row.address, row.square, row.sits]


def librare_format():
    return ['id', 'types', 'address', 'square', 'sits']


@csrf_exempt
def librares(request):
    if request.method == 'GET':
        a = Libraries.objects.all()
        a = [librare_to_list(item) for item in a]
        return JsonResponse({
            'format': librare_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def libraresFormat(request):
    if request.method == 'GET':
        return JsonResponse(librare_format(), safe=False)


@csrf_exempt
def librares_by_id(request, id):
    if request.method == 'DELETE':
        obj = Libraries.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Libraries(
            types=req_json['types'],
            address=req_json['address'],
            square=req_json['square'],
            sits=req_json['sits'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Libraries.objects.get(id=id)
        obj = Libraries(
            id=int(id),
            types=req_json['types'],
            address=req_json['address'],
            square=req_json['square'],
            sits=req_json['sits'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


librare_info_replace_map = {
    'td': {
        'objName': lambda obj: obj[0],
        'objAddress': lambda obj: obj[1],
        'objSq': lambda obj: obj[2],
        'objCnt': lambda obj: obj[3],
    }
}


# librare_info_replace_links_map = {
#     'td': {
#         'resultNir': lambda obj: obj[4],
#     }
# }

librare_info_row_template = \
    '<tr itemprop="purposeLibr">' \
    '<td itemprop="objName"></td>' \
    '<td itemprop="objAddress"></td>' \
    '<td itemprop="objSq"></td>' \
    '<td itemprop="objCnt"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def librares_publish(request):
    if request.method == 'GET':
        librares_information = Libraries.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/objects/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "purposeLib"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'purposeLibr'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(librares_information):
            values = librare_to_list(item)[1:]
            row = bs4.BeautifulSoup(librare_info_row_template)
            replace_page_elements(librare_info_replace_map, row, values)
            # replace_page_links(librare_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_sciencormation_replace_map, page_parser, sciencormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# -------------------- Материально-техническое обеспечение и оснащенность образовательного процесса -------------------
# Сведения о наличии объектов спорта

def sport_to_list(row):
    return [row.id, row.types, row.address, row.square, row.sits]


def sport_format():
    return ['id', 'types', 'address', 'square', 'sits']


@csrf_exempt
def sports(request):
    if request.method == 'GET':
        a = Sports.objects.all()
        a = [sport_to_list(item) for item in a]
        return JsonResponse({
            'format': sport_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def sportsFormat(request):
    if request.method == 'GET':
        return JsonResponse(sport_format(), safe=False)


@csrf_exempt
def sports_by_id(request, id):
    if request.method == 'DELETE':
        obj = Sports.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Sports(
            types=req_json['types'],
            address=req_json['address'],
            square=req_json['square'],
            sits=req_json['sits'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Sports.objects.get(id=id)
        obj = Sports(
            id=int(id),
            types=req_json['types'],
            address=req_json['address'],
            square=req_json['square'],
            sits=req_json['sits'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


sport_info_replace_map = {
    'td': {
        'objName': lambda obj: obj[0],
        'objAddress': lambda obj: obj[1],
        'objSq': lambda obj: obj[2],
        'objCnt': lambda obj: obj[3],
    }
}


# sport_info_replace_links_map = {
#     'td': {
#         'resultNir': lambda obj: obj[4],
#     }
# }

sport_info_row_template = \
    '<tr itemprop="purposeSport">' \
    '<td itemprop="objName"></td>' \
    '<td itemprop="objAddress"></td>' \
    '<td itemprop="objSq"></td>' \
    '<td itemprop="objCnt"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def sports_publish(request):
    if request.method == 'GET':
        sports_information = Sports.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/objects/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "purposeSp"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'purposeSport'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(sports_information):
            values = sport_to_list(item)[1:]
            row = bs4.BeautifulSoup(sport_info_row_template)
            replace_page_elements(sport_info_replace_map, row, values)
            # replace_page_links(sport_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_sciencormation_replace_map, page_parser, sciencormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# -------------------- Материально-техническое обеспечение и оснащенность образовательного процесса -------------------
# Сведения об условиях питания обучающихся

def meal_to_list(row):
    return [row.id, row.types, row.address, row.square, row.sits]


def meal_format():
    return ['id', 'types', 'address', 'square', 'sits']


@csrf_exempt
def meals(request):
    if request.method == 'GET':
        a = Meals.objects.all()
        a = [meal_to_list(item) for item in a]
        return JsonResponse({
            'format': meal_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def mealsFormat(request):
    if request.method == 'GET':
        return JsonResponse(meal_format(), safe=False)


@csrf_exempt
def meals_by_id(request, id):
    if request.method == 'DELETE':
        obj = Meals.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Meals(
            types=req_json['types'],
            address=req_json['address'],
            square=req_json['square'],
            sits=req_json['sits'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Meals.objects.get(id=id)
        obj = Meals(
            id=int(id),
            types=req_json['types'],
            address=req_json['address'],
            square=req_json['square'],
            sits=req_json['sits'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


meal_info_replace_map = {
    'td': {
        'objName': lambda obj: obj[0],
        'objAddress': lambda obj: obj[1],
        'objSq': lambda obj: obj[2],
        'objCnt': lambda obj: obj[3],
    }
}


# meal_info_replace_links_map = {
#     'td': {
#         'resultNir': lambda obj: obj[4],
#     }
# }

meal_info_row_template = \
    '<tr itemprop="meals">' \
    '<td itemprop="objName"></td>' \
    '<td itemprop="objAddress"></td>' \
    '<td itemprop="objSq"></td>' \
    '<td itemprop="objCnt"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def meals_publish(request):
    if request.method == 'GET':
        meals_information = Meals.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/objects/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "mealsss"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'meals'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(meals_information):
            values = meal_to_list(item)[1:]
            row = bs4.BeautifulSoup(meal_info_row_template)
            replace_page_elements(meal_info_replace_map, row, values)
            # replace_page_links(meal_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_sciencormation_replace_map, page_parser, sciencormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# -------------------- Материально-техническое обеспечение и оснащенность образовательного процесса -------------------
# Сведения об условиях охраны здоровья обучающихся

def healt_to_list(row):
    return [row.id, row.types, row.address, row.square, row.sits]


def healt_format():
    return ['id', 'types', 'address', 'square', 'sits']


@csrf_exempt
def healts(request):
    if request.method == 'GET':
        a = Health.objects.all()
        a = [healt_to_list(item) for item in a]
        return JsonResponse({
            'format': healt_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def healtsFormat(request):
    if request.method == 'GET':
        return JsonResponse(healt_format(), safe=False)


@csrf_exempt
def healts_by_id(request, id):
    if request.method == 'DELETE':
        obj = Health.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = Health(
            types=req_json['types'],
            address=req_json['address'],
            square=req_json['square'],
            sits=req_json['sits'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = Health.objects.get(id=id)
        obj = Health(
            id=int(id),
            types=req_json['types'],
            address=req_json['address'],
            square=req_json['square'],
            sits=req_json['sits'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


healt_info_replace_map = {
    'td': {
        'objName': lambda obj: obj[0],
        'objAddress': lambda obj: obj[1],
        'objSq': lambda obj: obj[2],
        'objCnt': lambda obj: obj[3],
    }
}


# healt_info_replace_links_map = {
#     'td': {
#         'resultNir': lambda obj: obj[4],
#     }
# }

healt_info_row_template = \
    '<tr itemprop="health">' \
    '<td itemprop="objName"></td>' \
    '<td itemprop="objAddress"></td>' \
    '<td itemprop="objSq"></td>' \
    '<td itemprop="objCnt"></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def healts_publish(request):
    if request.method == 'GET':
        healts_information = Health.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/objects/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "healtsss"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'health'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(healts_information):
            values = healt_to_list(item)[1:]
            row = bs4.BeautifulSoup(healt_info_row_template)
            replace_page_elements(healt_info_replace_map, row, values)
            # replace_page_links(healt_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_sciencormation_replace_map, page_parser, sciencormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ----------------- МАТЕРИАЛЬНО-ТЕХНИЧЕСКОЕ ОБЕСПЕЧЕНИЕ И ОСНАЩЁННОСТЬ ОБРАЗОВАТЕЛЬНОГО ПРОЦЕССА ----------------------
# Сведения о наличии средств обучения и воспитания

def one_to_list(row):
    return [row.id, row.name, row.link]


def one_format():
    return ['id', 'name', 'link']


@csrf_exempt
def ones(request):
    if request.method == 'GET':
        a = TableOne.objects.all()
        a = [one_to_list(item) for item in a]
        return JsonResponse({
            'format': one_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def onesFormat(request):
    if request.method == 'GET':
        return JsonResponse(one_format(), safe=False)


@csrf_exempt
def ones_by_id(request, id):
    if request.method == 'DELETE':
        obj = TableOne.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = TableOne(
            name=req_json['name'],
            link=req_json['link'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = TableOne.objects.get(id=id)
        obj = TableOne(
            id=int(id),
            name=req_json['name'],
            link=req_json['link'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


one_info_replace_map = {
    'td': {
        'name': lambda obj: obj[0],
    }
}


one_info_replace_links_map = {
    'td': {
         'purposeFacil': lambda obj: obj[1],
    }
}

one_info_row_template = \
    '<tr itemprop="facil">' \
    '<td itemprop="name"></td>' \
    '<td itemprop="purposeFacil"><a href=" ">Ссылка</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def ones_publish(request):
    if request.method == 'GET':
        ones_information = TableOne.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/objects/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "facil"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'facil'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(ones_information):
            values = one_to_list(item)[1:]
            row = bs4.BeautifulSoup(one_info_row_template)
            replace_page_elements(one_info_replace_map, row, values)
            replace_page_links(one_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_oneormation_replace_map, page_parser, oneormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ----------------- МАТЕРИАЛЬНО-ТЕХНИЧЕСКОЕ ОБЕСПЕЧЕНИЕ И ОСНАЩЁННОСТЬ ОБРАЗОВАТЕЛЬНОГО ПРОЦЕССА ----------------------
# Сведения о доступе к информационным системам и информационно-телекоммуникационным сетям

def two_to_list(row):
    return [row.id, row.name, row.link]


def two_format():
    return ['id', 'name', 'link']


@csrf_exempt
def twos(request):
    if request.method == 'GET':
        a = TableTwo.objects.all()
        a = [two_to_list(item) for item in a]
        return JsonResponse({
            'format': two_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def twosFormat(request):
    if request.method == 'GET':
        return JsonResponse(two_format(), safe=False)


@csrf_exempt
def twos_by_id(request, id):
    if request.method == 'DELETE':
        obj = TableTwo.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = TableTwo(
            name=req_json['name'],
            link=req_json['link'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = TableTwo.objects.get(id=id)
        obj = TableTwo(
            id=int(id),
            name=req_json['name'],
            link=req_json['link'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


two_info_replace_map = {
    'td': {
        'name': lambda obj: obj[0],
    }
}


two_info_replace_links_map = {
    'td': {
         'comNet': lambda obj: obj[1],
    }
}

two_info_row_template = \
    '<tr itemprop="net">' \
    '<td itemprop="name"></td>' \
    '<td itemprop="comNet"><a href=" ">Ссылка</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def twos_publish(request):
    if request.method == 'GET':
        twos_information = TableTwo.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/objects/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "net"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'net'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(twos_information):
            values = two_to_list(item)[1:]
            row = bs4.BeautifulSoup(two_info_row_template)
            replace_page_elements(two_info_replace_map, row, values)
            replace_page_links(two_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_twoormation_replace_map, page_parser, twoormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ----------------- МАТЕРИАЛЬНО-ТЕХНИЧЕСКОЕ ОБЕСПЕЧЕНИЕ И ОСНАЩЁННОСТЬ ОБРАЗОВАТЕЛЬНОГО ПРОЦЕССА ----------------------
# Наличие в образовательной организации электронной информационно-образовательной среды

def three_to_list(row):
    return [row.id, row.name, row.link]


def three_format():
    return ['id', 'name', 'link']


@csrf_exempt
def threes(request):
    if request.method == 'GET':
        a = TableThree.objects.all()
        a = [three_to_list(item) for item in a]
        return JsonResponse({
            'format': three_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def threesFormat(request):
    if request.method == 'GET':
        return JsonResponse(three_format(), safe=False)


@csrf_exempt
def threes_by_id(request, id):
    if request.method == 'DELETE':
        obj = TableThree.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = TableThree(
            name=req_json['name'],
            link=req_json['link'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = TableThree.objects.get(id=id)
        obj = TableThree(
            id=int(id),
            name=req_json['name'],
            link=req_json['link'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


three_info_replace_map = {
    'td': {
        'name': lambda obj: obj[0],
    }
}


three_info_replace_links_map = {
    'td': {
         'purposeEios': lambda obj: obj[1],
    }
}

three_info_row_template = \
    '<tr itemprop="eios">' \
    '<td itemprop="name"></td>' \
    '<td itemprop="purposeEios"><a href=" ">Ссылка</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def threes_publish(request):
    if request.method == 'GET':
        threes_information = TableThree.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/objects/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "eios"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'eios'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(threes_information):
            values = three_to_list(item)[1:]
            row = bs4.BeautifulSoup(three_info_row_template)
            replace_page_elements(three_info_replace_map, row, values)
            replace_page_links(three_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_threeormation_replace_map, page_parser, threeormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ----------------- МАТЕРИАЛЬНО-ТЕХНИЧЕСКОЕ ОБЕСПЕЧЕНИЕ И ОСНАЩЁННОСТЬ ОБРАЗОВАТЕЛЬНОГО ПРОЦЕССА ----------------------
# Наличие собственных электронных образовательных и информационных ресурсов

def four_to_list(row):
    return [row.id, row.name, row.link]


def four_format():
    return ['id', 'name', 'link']


@csrf_exempt
def fours(request):
    if request.method == 'GET':
        a = TableFour.objects.all()
        a = [four_to_list(item) for item in a]
        return JsonResponse({
            'format': four_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def foursFormat(request):
    if request.method == 'GET':
        return JsonResponse(four_format(), safe=False)


@csrf_exempt
def fours_by_id(request, id):
    if request.method == 'DELETE':
        obj = TableFour.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = TableFour(
            name=req_json['name'],
            link=req_json['link'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = TableFour.objects.get(id=id)
        obj = TableFour(
            id=int(id),
            name=req_json['name'],
            link=req_json['link'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


four_info_replace_map = {
    'td': {
        'name': lambda obj: obj[0],
    }
}


four_info_replace_links_map = {
    'td': {
         'eoisOwn': lambda obj: obj[1],
    }
}

four_info_row_template = \
    '<tr itemprop="own">' \
    '<td itemprop="name"></td>' \
    '<td itemprop="eoisOwn"><a href=" ">Ссылка</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def fours_publish(request):
    if request.method == 'GET':
        fours_information = TableFour.objects.all()

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
        for index, item in enumerate(fours_information):
            values = four_to_list(item)[1:]
            row = bs4.BeautifulSoup(four_info_row_template)
            replace_page_elements(four_info_replace_map, row, values)
            replace_page_links(four_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_fourormation_replace_map, page_parser, fourormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ----------------- МАТЕРИАЛЬНО-ТЕХНИЧЕСКОЕ ОБЕСПЕЧЕНИЕ И ОСНАЩЁННОСТЬ ОБРАЗОВАТЕЛЬНОГО ПРОЦЕССА ----------------------
# Наличие сторонних электронных образовательных и информационных ресурсов

def five_to_list(row):
    return [row.id, row.name, row.link]


def five_format():
    return ['id', 'name', 'link']


@csrf_exempt
def fives(request):
    if request.method == 'GET':
        a = TableFive.objects.all()
        a = [five_to_list(item) for item in a]
        return JsonResponse({
            'format': five_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def fivesFormat(request):
    if request.method == 'GET':
        return JsonResponse(five_format(), safe=False)


@csrf_exempt
def fives_by_id(request, id):
    if request.method == 'DELETE':
        obj = TableFive.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = TableFive(
            name=req_json['name'],
            link=req_json['link'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = TableFive.objects.get(id=id)
        obj = TableFive(
            id=int(id),
            name=req_json['name'],
            link=req_json['link'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


five_info_replace_map = {
    'td': {
        'name': lambda obj: obj[0],
    }
}


five_info_replace_links_map = {
    'td': {
         'eoisSide': lambda obj: obj[1],
    }
}

five_info_row_template = \
    '<tr itemprop="side">' \
    '<td itemprop="name"></td>' \
    '<td itemprop="eoisSide"><a href=" ">Ссылка</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def fives_publish(request):
    if request.method == 'GET':
        fives_information = TableFive.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/objects/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "side"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'side'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(fives_information):
            values = five_to_list(item)[1:]
            row = bs4.BeautifulSoup(five_info_row_template)
            replace_page_elements(five_info_replace_map, row, values)
            replace_page_links(five_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_fiveormation_replace_map, page_parser, fiveormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ----------------- МАТЕРИАЛЬНО-ТЕХНИЧЕСКОЕ ОБЕСПЕЧЕНИЕ И ОСНАЩЁННОСТЬ ОБРАЗОВАТЕЛЬНОГО ПРОЦЕССА ----------------------
# Наличие базы данных электронного каталога

def six_to_list(row):
    return [row.id, row.name, row.link]


def six_format():
    return ['id', 'name', 'link']


@csrf_exempt
def sixs(request):
    if request.method == 'GET':
        a = TableSix.objects.all()
        a = [six_to_list(item) for item in a]
        return JsonResponse({
            'format': six_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def sixsFormat(request):
    if request.method == 'GET':
        return JsonResponse(six_format(), safe=False)


@csrf_exempt
def sixs_by_id(request, id):
    if request.method == 'DELETE':
        obj = TableSix.objects.get(id=id)
        if obj is None:
            return HttpResponseBadRequest()
        obj.delete()
        return HttpResponse(200)
    elif request.method == 'POST':
        req_json = JSONParser().parse(request)
        obj = TableSix(
            name=req_json['name'],
            link=req_json['link'],
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        obj.save()
        return HttpResponse(200)
    elif request.method == 'PUT':
        req_json = JSONParser().parse(request)
        obj_old = TableSix.objects.get(id=id)
        obj = TableSix(
            id=int(id),
            name=req_json['name'],
            link=req_json['link'],
            updated_at=datetime.today(),
            created_at=obj_old.created_at
        )
        obj.save()
        return HttpResponse(200)


six_info_replace_map = {
    'td': {
        'name': lambda obj: obj[0],
    }
}


six_info_replace_links_map = {
    'td': {
         'bdec': lambda obj: obj[1],
    }
}

six_info_row_template = \
    '<tr itemprop="bd">' \
    '<td itemprop="name"></td>' \
    '<td itemprop="bdec"><a href=" ">Ссылка</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def sixs_publish(request):
    if request.method == 'GET':
        sixs_information = TableSix.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/objects/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "bd"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'bd'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(sixs_information):
            values = six_to_list(item)[1:]
            row = bs4.BeautifulSoup(six_info_row_template)
            replace_page_elements(six_info_replace_map, row, values)
            replace_page_links(six_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_sixormation_replace_map, page_parser, sixormation)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


# ----------------- МАТЕРИАЛЬНО-ТЕХНИЧЕСКОЕ ОБЕСПЕЧЕНИЕ И ОСНАЩЁННОСТЬ ОБРАЗОВАТЕЛЬНОГО ПРОЦЕССА ----------------------
# Ссылки на перечень электронных образовательных ресурсов

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
         'link': lambda obj: obj[1],
    }
}

seven_info_row_template = \
    '<tr itemprop="erList">' \
    '<td itemprop="name"></td>' \
    '<td itemprop="link"><a href=" ">Ссылка</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def sevens_publish(request):
    if request.method == 'GET':
        sevens_information = TableSeven.objects.all()

        file = 'EmployeeApp/parser/pages/sveden/objects/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'itemprop': "list"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'erList'})

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