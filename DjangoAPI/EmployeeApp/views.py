from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse, HttpResponseBadRequest

from .models import Departments, Employees, BasicInformations, DepartmentsInformation, Subdivisions
from .serializers import DepartmentSerializer, EmployeeSerializer, BasicInformationSerializer, \
    DepartmentsInformationSerializer, SubdivisionsSerializer

from django.core.files.storage import default_storage

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


# def update_empl_info(html, empl):
#     tags = html.find_all('div', {'id': 'asdasd'})
#     if len(tags) == 1:
#         tags.string = empl.name
#
#
# @csrf_exempt
# def generate_html_page(request):
#     if request.method == 'GET':
#         html = read_html('emploee/index.php')
#
#         # update data
#         emploee = Employees.objects.all()
#         for empl in emploee:
#             update_empl_info(html, empl)
#         for departm
#
#
#         # print
#         with open('emploee/index.php', 'w') as f:
#             print(str(html), file=f)


def fill_json(keys, values, json):
    for i, name in enumerate(keys):
        json[name] = values[i]
    return json


# ------------------------- СТРУКТУРНЫЕ ПОДРАЗДЕЛЕНИЯ ОБРАЗОВАТЕЛЬНОЙ ОРГАНИЗАЦИИ ---------------------------------


def get_department_table_header():
    header_row = DepartmentsInformation.objects.get(DIid=0)
    return header_row.DIrow.split('\t')


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


from datetime import datetime


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


from datetime import datetime


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


# def replace_page_links(replace_map, parser, obj):
#     for tag, parameters in replace_map.items():
#         for name, getter in parameters.items():
#             tags = parser.find_all(tag, {'itemprop': name})
#             if len(tags) == 1:
#                 print(getter(obj))
#                 tags[0].a.href = str(getter(obj))
#             else:
#                 pass
#     return parser


basic_information_info_row_template = \
    '<tr>' \
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
        rows = table.find_all('tr')

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
