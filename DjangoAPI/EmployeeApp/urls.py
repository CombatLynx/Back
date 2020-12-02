from django.conf.urls import url
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  url(r'^department/$', views.departmentApi),
                  url(r'^department/([0-9]+)$', views.departmentApi),

                  url(r'^employee/$', views.employeeApi),
                  url(r'^employee/([0-9]+)$', views.employeeApi),

                  url(r'^basicInformations/publish/$', views.publish_basic_information),
                  url(r'^basicInformations/$', views.basicInformationApi),
                  url(r'^basicInformations/([0-9]+)$', views.basicInformationApi),

                  # url(r'^departmentInformations/publish/$', views.publish_department_information),
                  url(r'^subdivisions/$', views.subdivisions),
                  url(r'^subdivisions/format/$', views.subdivisionsFormat),
                  url(r'^subdivisions/([1-9][0-9]*)$', views.subdivisions_by_id),
                  url(r'^subdivisions/publish/$', views.subdivisions_publish),

                  url(r'^basic_informations/$', views.basic_informations),
                  url(r'^basic_informations/format/$', views.basic_informationsFormat),
                  url(r'^basic_informations/([1-9][0-9]*)$', views.basic_informations_by_id),
                  url(r'^basic_informations/publish/$', views.basic_informations_publish),

                  url(r'^founders/$', views.founders),
                  url(r'^founders/format/$', views.foundersFormat),
                  url(r'^founders/([1-9][0-9]*)$', views.founders_by_id),
                  url(r'^founders/publish/$', views.founders_publish),

                  url(r'^SaveFile$', views.SaveFile)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
