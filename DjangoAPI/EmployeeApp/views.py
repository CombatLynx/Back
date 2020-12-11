from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse, HttpResponseBadRequest

from .models import Departments, Employees, BasicInformations, DepartmentsInformation, Subdivisions, Founders, \
    Filiations, Representations, Managements, Volumes, Vacs, Leaders, Teachers, FilialLeaders, Leaderstwo
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
        file = 'EmployeeApp/parser/pages/basic_information/index.php'
        page_parser = read_page(file)
        new_page = str(replace_page_elements(basic_information_replace_map, page_parser, information))
        write_page(file, new_page)
        return HttpResponse("OK")


@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)


def fill_json(keys, values, json):
    for i, name in enumerate(keys):
        json[name] = values[i]
    return json


def get_department_table_header():
    header_row = DepartmentsInformation.objects.get(DIid=0)
    return header_row.DIrow.split('\t')


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

        file = 'EmployeeApp/parser/pages/subdivisions/index.html'
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


@csrf_exempt
def subdivisions(request):
    if request.method == 'GET':
        a = Subdivisions.objects.all()
        a = [subdivision_to_list(item) for item in a]
        return JsonResponse({
            'format': subdivision_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def subdivisionsFormat(request):
    if request.method == 'GET':
        return JsonResponse(subdivision_format(), safe=False)


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
        'divisionClauseDocLink': lambda obj: obj[6],
    }
}


def replace_page_links(replace_map, parser, obj):
    for tag, parameters in replace_map.items():
        for name, getter in parameters.items():
            tags = parser.find_all(tag, {'itemprop': name})
            if len(tags) == 1:
                print(getter(obj))
                tags[0].a.href = str(getter(obj))
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
    '<td itemprop="divisionClauseDocLink"><a href="" download="">Положение</a></td>' \
    '</tr>'


# будут проблемы, если оказалось так, что таблица пустая
@csrf_exempt
def subdivisions_publish(request):
    if request.method == 'GET':
        departments_information = Subdivisions.objects.all()

        file = 'EmployeeApp/parser/pages/subdivisions/index.html'
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
    '<tr itemprop="basic_information">' \
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

        file = 'EmployeeApp/parser/pages/basic_information/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'id': "main_information"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'basic_information'})

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


@csrf_exempt
def founders(request):
    if request.method == 'GET':
        a = Founders.objects.all()
        a = [founder_to_list(item) for item in a]
        return JsonResponse({
            'format': founder_format(),
            'data': a
        }, safe=False)
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def foundersFormat(request):
    if request.method == 'GET':
        return JsonResponse(founder_format(), safe=False)


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

        file = 'EmployeeApp/parser/pages/basic_information/index.html'
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

        file = 'EmployeeApp/parser/pages/basic_information/index.html'
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

        file = 'EmployeeApp/parser/pages/basic_information/index.html'
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
    '<td itemprop="finRas">a href="">Ссылка</a></td>' \
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
