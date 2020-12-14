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

                  url(r'^filiations/$', views.filiations),
                  url(r'^filiations/format/$', views.filiationsFormat),
                  url(r'^filiations/([1-9][0-9]*)$', views.filiations_by_id),
                  url(r'^filiations/publish/$', views.filiations_publish),

                  url(r'^representations/$', views.representations),
                  url(r'^representations/format/$', views.representationsFormat),
                  url(r'^representations/([1-9][0-9]*)$', views.representations_by_id),
                  url(r'^representations/publish/$', views.representations_publish),

                  url(r'^managements/$', views.managements),
                  url(r'^managements/format/$', views.managementsFormat),
                  url(r'^managements/([1-9][0-9]*)$', views.managements_by_id),
                  url(r'^managements/publish/$', views.managements_publish),

                  url(r'^volumes/$', views.volumes),
                  url(r'^volumes/format/$', views.volumesFormat),
                  url(r'^volumes/([1-9][0-9]*)$', views.volumes_by_id),
                  url(r'^volumes/publish/$', views.volumes_publish),

                  url(r'^vacs/$', views.vacs),
                  url(r'^vacs/format/$', views.vacsFormat),
                  url(r'^vacs/([1-9][0-9]*)$', views.vacs_by_id),
                  url(r'^vacs/publish/$', views.vacs_publish),
                  # ---------------------------------------------------------
                  url(r'^leaders/$', views.leaders),
                  url(r'^leaders/format/$', views.leadersFormat),
                  url(r'^leaders/([1-9][0-9]*)$', views.leaders_by_id),
                  url(r'^leaders/publish/$', views.leaders_publish),

                  url(r'^leadersTwo/$', views.leadersTwos),
                  url(r'^leadersTwo/format/$', views.leadersTwosFormat),
                  url(r'^leadersTwo/([1-9][0-9]*)$', views.leadersTwos_by_id),
                  url(r'^leadersTwo/publish/$', views.leadersTwos_publish),

                  url(r'^filialLeaders/$', views.filialLeaders),
                  url(r'^filialLeaders/format/$', views.filialLeadersFormat),
                  url(r'^filialLeaders/([1-9][0-9]*)$', views.filialLeaders_by_id),
                  url(r'^filialLeaders/publish/$', views.filialLeaders_publish),

                  url(r'^teachers/$', views.teachers),
                  url(r'^teachers/format/$', views.teachersFormat),
                  url(r'^teachers/([1-9][0-9]*)$', views.teachers_by_id),
                  url(r'^teachers/publish/$', views.teachers_publish),

                  url(r'^standartCopies/$', views.standartCopies),
                  url(r'^standartCopies/format/$', views.standartCopiesFormat),
                  url(r'^standartCopies/([1-9][0-9]*)$', views.standartCopies_by_id),
                  url(r'^standartCopies/publish/$', views.standartCopies_publish),

                  url(r'^paidServices/$', views.paidServices),
                  url(r'^paidServices/format/$', views.paidServicesFormat),
                  url(r'^paidServices/([1-9][0-9]*)$', views.paidServices_by_id),
                  url(r'^paidServices/publish/$', views.paidServices_publish),


                  url(r'^SaveFile$', views.SaveFile)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)