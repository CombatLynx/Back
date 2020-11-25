from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse

from .models import Departments, Employees, BasicInformations, DepartmentsInformation, UchredsInformation
from .serializers import DepartmentSerializer, EmployeeSerializer, BasicInformationSerializer, \
    UchredBISerializer, DepartmentsInformationSerializer

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
        file = 'EmployeeApp/parser/pages/basic_information/index.html'
        page_parser = read_page(file)
        new_page = str(replace_page_elements(basic_information_replace_map, page_parser, information))
        write_page(file, new_page)
        return HttpResponse("OK")


@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)


#
# СТРУКТУРНЫЕ ПОДРАЗДЕЛЕНИЯ ОБРАЗОВАТЕЛЬНОЙ ОРГАНИЗАЦИИ
#

def fill_json(keys, values, json):
    for i, name in enumerate(keys):
        json[name] = values[i]
    return json


def get_department_table_header():
    header_row = DepartmentsInformation.objects.get(DIid=0)
    return header_row.DIrow.split('\t')


@csrf_exempt
def departmentTable(request, id=None):
    format = ['id'] + get_department_table_header()
    if request.method == 'GET':
        if id is None:
            departments_information = DepartmentsInformation.objects.all().order_by('DIid')
            response_data = []
            if len(departments_information) != 0:
                keys = get_department_table_header()
                for item in departments_information[1:]:
                    values = item.DIrow.split('\t')
                    json = {'id': item.DIid}
                    response_data.append(fill_json(keys, values, json))
                return JsonResponse({'format': format, 'data': response_data}, safe=False)
        else:
            departments_information = DepartmentsInformation.objects.get(DIid=id)
            json = {'id': departments_information.DIid}
            keys = get_department_table_header()
            values = departments_information.DIrow.split('\t')
            response = fill_json(keys, values, json)

            return JsonResponse({'format': format, 'data': response}, safe=False)

    elif request.method == 'POST' or request.method == 'PUT':
        department_info_json = JSONParser().parse(request)
        header_keys = get_department_table_header()
        if set(header_keys + ['id']) == set(
                department_info_json.keys()):  # наверное сет плохо, по крайней мере в случае одинаковых названий
            data_row = '\t'.join([department_info_json[key] for key in header_keys])
            DepartmentsInformation(DIid=department_info_json['id'], DIrow=data_row).save()
            return JsonResponse("Added Successfully!!", safe=False)

    elif request.method == 'DELETE':
        departments_information = DepartmentsInformation.objects.get(DIid=id)
        departments_information.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)


@csrf_exempt
def departmentTableFormat(request):
    if request.method == 'POST':
        req_json = JSONParser().parse(request)
        header = "\t".join(req_json)
        DepartmentsInformation.objects.all().delete()
        DepartmentsInformation(DIid=0, DIrow=header).save()
        return JsonResponse("Changed Successfully!!", safe=False)

    if request.method == 'GET':
        format = ['id'] + get_department_table_header()
        return JsonResponse(format, safe=False)


@csrf_exempt
def departmentTableDeleteColumn(request, col_name):
    if request.method == 'DELETE':
        keys = get_department_table_header()
        try:
            index = keys.index(col_name)
        except ValueError:
            return JsonResponse("Deleted Failed!!", safe=False)
        departments_informations = DepartmentsInformation.objects.all().order_by('DIid')
        for item in departments_informations:
            values = item.DIrow.split('\t')
            values.pop(index)
            item.DIrow = '\t'.join(values)
            item.save()
        return JsonResponse("Deleted Successfully!!", safe=False)


@csrf_exempt
def departmentTableAddColumn(request):
    if request.method == 'POST':
        req_json = JSONParser().parse(request)
        index = req_json['index']
        name = req_json['name']

        keys = get_department_table_header()
        keys.insert(index, name)
        DepartmentsInformation(DIid=0, DIrow='\t'.join(keys)).save()

        departments_informations = DepartmentsInformation.objects.all().order_by('DIid')
        for item in departments_informations[1:]:
            values = item.DIrow.split('\t')
            values.insert(index, '')
            item.DIrow = '\t'.join(values)
            item.save()
        return JsonResponse("Added Successfully!!", safe=False)


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


# будут проблемы, если окdepartmentTableазалось так, что таблица пустая
@csrf_exempt
def departmentTableRender(request):
    if request.method == 'GET':
        departments_information = DepartmentsInformation.objects.all().order_by('DIid')

        file = 'EmployeeApp/parser/pages/department_info/index.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'id': "departments"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'structOrgUprav'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(departments_information[1:]):
            values = item.DIrow.split('\t')
            row = bs4.BeautifulSoup(department_info_row_template)
            replace_page_elements(department_info_replace_map, row, values)
            replace_page_links(department_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")


#
# УЧРЕДИТЕЛИ ОБРАЗОВАТЕЛЬНОЙ ОРГАНИЗАЦИИ
#

def get_uchred_table_header():
    header_row = UchredsInformation.objects.get(UBIid=0)
    return header_row.UBIrow.split('\t')


@csrf_exempt
def uchredTable(request, id=None):
    format = ['id'] + get_uchred_table_header()
    if request.method == 'GET':
        if id is None:
            uchreds_information = UchredsInformation.objects.all().order_by('UBIid')
            response_data = []
            if len(uchreds_information) != 0:
                keys = get_uchred_table_header()
                for item in uchreds_information[1:]:
                    values = item.UBIrow.split('\t')
                    json = {'id': item.UBIid}
                    response_data.append(fill_json(keys, values, json))
                return JsonResponse({'format': format, 'data': response_data}, safe=False)
        else:
            uchreds_information = UchredsInformation.objects.get(UBIid=id)
            json = {'id': uchreds_information.UBIid}
            keys = get_uchred_table_header()
            values = uchreds_information.UBIrow.split('\t')
            response = fill_json(keys, values, json)

            return JsonResponse({'format': format, 'data': response}, safe=False)

    elif request.method == 'POST' or request.method == 'PUT':
        uchred_info_json = JSONParser().parse(request)
        header_keys = get_uchred_table_header()
        if set(header_keys + ['id']) == set(
                uchred_info_json.keys()):  # наверное сет плохо, по крайней мере в случае одинаковых названий
            data_row = '\t'.join([uchred_info_json[key] for key in header_keys])
            UchredsInformation(UBIid=uchred_info_json['id'], UBIrow=data_row).save()
            return JsonResponse("Added Successfully!!", safe=False)

    elif request.method == 'DELETE':
        uchreds_information = UchredsInformation.objects.get(UBIid=id)
        uchreds_information.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)


@csrf_exempt
def uchredTableFormat(request):
    if request.method == 'POST':
        req_json = JSONParser().parse(request)
        header = "\t".join(req_json)
        UchredsInformation.objects.all().delete()
        UchredsInformation(UBIid=0, UBIrow=header).save()
        return JsonResponse("Changed Successfully!!", safe=False)

    if request.method == 'GET':
        format = ['id'] + get_uchred_table_header()
        return JsonResponse(format, safe=False)


@csrf_exempt
def uchredTableDeleteColumn(request, col_name):
    if request.method == 'DELETE':
        keys = get_uchred_table_header()
        try:
            index = keys.index(col_name)
        except ValueError:
            return JsonResponse("Deleted Failed!!", safe=False)
        uchreds_informations = UchredsInformation.objects.all().order_by('UBIid')
        for item in uchreds_informations:
            values = item.UBIrow.split('\t')
            values.pop(index)
            item.UBIrow = '\t'.join(values)
            item.save()
        return JsonResponse("Deleted Successfully!!", safe=False)


@csrf_exempt
def uchredTableAddColumn(request):
    if request.method == 'POST':
        req_json = JSONParser().parse(request)
        index = req_json['index']
        name = req_json['name']

        keys = get_uchred_table_header()
        keys.insert(index, name)
        UchredsInformation(UBIid=0, UBIrow='\t'.join(keys)).save()

        uchreds_informations = UchredsInformation.objects.all().order_by('UBIid')
        for item in uchreds_informations[1:]:
            values = item.UBIrow.split('\t')
            values.insert(index, '')
            item.UBIrow = '\t'.join(values)
            item.save()
        return JsonResponse("Added Successfully!!", safe=False)


uchred_info_replace_map = {
    'td': {
        'nameUchred': lambda obj: obj[0],
        'addressUchred': lambda obj: obj[1],
        'telUchred': lambda obj: obj[2],
        'mailUchred': lambda obj: obj[3],
    }
}

uchred_info_replace_links_map = {
    'td': {
        'websiteUchred': lambda obj: obj[4]
    }
}

uchred_info_row_template = \
    '<tr itemprop="struct">' \
    '<td itemprop="nameUchred"></td>' \
    '<td itemprop="addressUchred"></td>' \
    '<td itemprop="telUchred"></td>' \
    '<td itemprop="mailUchred"></td>' \
    '<td itemprop="websiteUchred"><a href="">Ссылка</a></td>' \
    '</tr>'


# будут проблемы, если окdepartmentTableазалось так, что таблица пустая
@csrf_exempt
def uchredTableRender(request):
    if request.method == 'GET':
        uchreds_information = UchredsInformation.objects.all().order_by('UBIid')

        file = 'EmployeeApp/parser/pages/department_info/sveden-common-uchred.html'
        page_parser = read_page(file)
        tables = page_parser.find_all('table', {'id': "uchreds"})
        if len(tables) != 1:
            return HttpResponse("Error")
        table = tables[0]
        rows = table.find_all('tr', {'itemprop': 'struct'})

        for row in rows:
            row.extract()
        last_tr = table.tr
        for index, item in enumerate(uchreds_information[1:]):
            values = item.UBIrow.split('\t')
            row = bs4.BeautifulSoup(uchred_info_row_template)
            replace_page_elements(uchred_info_replace_map, row, values)
            replace_page_links(uchred_info_replace_links_map, row, values)
            last_tr.insert_after(row)
            last_tr = last_tr.next_sibling

        # new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
        write_page(file, str(page_parser))
        return HttpResponse("OK")
