from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse

from .models import Departments, Employees, BasicInformations
from .serializers import DepartmentSerializer, EmployeeSerializer, BasicInformationSerializer

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
    with open(filename, "r") as f:
        content = f.read()
        return bs4.BeautifulSoup(content, 'lxml')


def write_page(filename, page):
    with open(filename, "w") as f:
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
    return str(parser)


@csrf_exempt
def publish_basic_information(request):
    if request.method == 'POST':
        body_json = JSONParser().parse(request)
        id = body_json['id']
        information = BasicInformations.objects.get(BIid=id)
        file = 'EmployeeApp/parser/pages/basic_information/index.html'
        page_parser = read_page(file)
        new_page = replace_page_elements(basic_information_replace_map, page_parser, information)
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
#         html = read_html('emploee/index.html')
#
#         # update data
#         emploee = Employees.objects.all()
#         for empl in emploee:
#             update_empl_info(html, empl)
#         for departm
#
#
#         # print
#         with open('emploee/index.html', 'w') as f:
#             print(str(html), file=f)
