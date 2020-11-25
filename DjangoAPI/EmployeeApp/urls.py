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
                  url(r'^departmentTable/$', views.departmentTable),
                  url(r'^departmentTable/([1-9][0-9]*)$', views.departmentTable),
                  url(r'^departmentTable/format$', views.departmentTableFormat),
                  url(r'^departmentTable/deleteColumn/([0-9a-zA-Z_]+)$', views.departmentTableDeleteColumn),
                  url(r'^departmentTable/addColumn$', views.departmentTableAddColumn),
                  url(r'^departmentTable/publish/$', views.departmentTableRender),

                  # url(r'^departmentInformations/publish/$', views.publish_department_information),
                  url(r'^uchredTable/$', views.uchredTable),
                  url(r'^uchredTable/([1-9][0-9]*)$', views.uchredTable),
                  url(r'^uchredTable/format$', views.uchredTableFormat),
                  url(r'^uchredTable/deleteColumn/([0-9a-zA-Z_]+)$', views.uchredTableDeleteColumn),
                  url(r'^uchredTable/addColumn$', views.uchredTableAddColumn),
                  url(r'^uchredTable/publish/$', views.uchredTableRender),

                  url(r'^SaveFile$', views.SaveFile)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
