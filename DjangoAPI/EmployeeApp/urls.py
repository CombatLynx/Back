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

                  url(r'^internationalDogs/$', views.internationalDogs),
                  url(r'^internationalDogs/format/$', views.internationalDogsFormat),
                  url(r'^internationalDogs/([1-9][0-9]*)$', views.internationalDogs_by_id),
                  url(r'^internationalDogs/publish/$', views.internationalDogs_publish),

                  url(r'^internationalAccrs/$', views.internationalAccrs),
                  url(r'^internationalAccrs/format/$', views.internationalAccrsFormat),
                  url(r'^internationalAccrs/([1-9][0-9]*)$', views.internationalAccrs_by_id),
                  url(r'^internationalAccrs/publish/$', views.internationalAccrs_publish),

                  url(r'^specCabs/$', views.specCabs),
                  url(r'^specCabs/format/$', views.specCabsFormat),
                  url(r'^specCabs/([1-9][0-9]*)$', views.specCabs_by_id),
                  url(r'^specCabs/publish/$', views.specCabs_publish),

                  url(r'^specPracs/$', views.specPracs),
                  url(r'^specPracs/format/$', views.specPracsFormat),
                  url(r'^specPracs/([1-9][0-9]*)$', views.specPracs_by_id),
                  url(r'^specPracs/publish/$', views.specPracs_publish),

                  url(r'^specLibs/$', views.specLibs),
                  url(r'^specLibs/format/$', views.specLibsFormat),
                  url(r'^specLibs/([1-9][0-9]*)$', views.specLibs_by_id),
                  url(r'^specLibs/publish/$', views.specLibs_publish),

                  url(r'^specSports/$', views.specSports),
                  url(r'^specSports/format/$', views.specSportsFormat),
                  url(r'^specSports/([1-9][0-9]*)$', views.specSports_by_id),
                  url(r'^specSports/publish/$', views.specSports_publish),

                  url(r'^specMeals/$', views.specMeals),
                  url(r'^specMeals/format/$', views.specMealsFormat),
                  url(r'^specMeals/([1-9][0-9]*)$', views.specMeals_by_id),
                  url(r'^specMeals/publish/$', views.specMeals_publish),

                  url(r'^specHealths/$', views.specHealths),
                  url(r'^specHealths/format/$', views.specHealthsFormat),
                  url(r'^specHealths/([1-9][0-9]*)$', views.specHealths_by_id),
                  url(r'^specHealths/publish/$', views.specHealths_publish),

                  url(r'^ovzs/$', views.ovzs),
                  url(r'^ovzs/format/$', views.ovzsFormat),
                  url(r'^ovzs/([1-9][0-9]*)$', views.ovzs_by_id),
                  url(r'^ovzs/publish/$', views.ovzs_publish),

                  url(r'^linkOvzs/$', views.linkOvzs),
                  url(r'^linkOvzs/format/$', views.linkOvzsFormat),
                  url(r'^linkOvzs/([1-9][0-9]*)$', views.linkOvzs_by_id),
                  url(r'^linkOvzs/publish/$', views.linkOvzs_publish),

                  url(r'^ovzTwos/$', views.ovzTwos),
                  url(r'^ovzTwos/format/$', views.ovzTwosFormat),
                  url(r'^ovzTwos/([1-9][0-9]*)$', views.ovzTwos_by_id),
                  url(r'^ovzTwos/publish/$', views.ovzTwos_publish),

                  url(r'^grants/$', views.grants),
                  url(r'^grants/format/$', views.grantsFormat),
                  url(r'^grants/([1-9][0-9]*)$', views.grants_by_id),
                  url(r'^grants/publish/$', views.grants_publish),

                  url(r'^grantInfos/$', views.grantInfos),
                  url(r'^grantInfos/format/$', views.grantInfosFormat),
                  url(r'^grantInfos/([1-9][0-9]*)$', views.grantInfos_by_id),
                  url(r'^grantInfos/publish/$', views.grantInfos_publish),

                  url(r'^acts/$', views.acts),
                  url(r'^acts/format/$', views.actsFormat),
                  url(r'^acts/([1-9][0-9]*)$', views.acts_by_id),
                  url(r'^acts/publish/$', views.acts_publish),

                  url(r'^jobs/$', views.jobs),
                  url(r'^jobs/format/$', views.jobsFormat),
                  url(r'^jobs/([1-9][0-9]*)$', views.jobs_by_id),
                  url(r'^jobs/publish/$', views.jobs_publish),

                  url(r'^gosAccreditations/$', views.gosAccreditations),
                  url(r'^gosAccreditations/format/$', views.gosAccreditationsFormat),
                  url(r'^gosAccreditations/([1-9][0-9]*)$', views.gosAccreditations_by_id),
                  url(r'^gosAccreditations/publish/$', views.gosAccreditations_publish),

                  url(r'^profs/$', views.profs),
                  url(r'^profs/format/$', views.profsFormat),
                  url(r'^profs/([1-9][0-9]*)$', views.profs_by_id),
                  url(r'^profs/publish/$', views.profs_publish),

                  url(r'^infs/$', views.infs),
                  url(r'^infs/format/$', views.infsFormat),
                  url(r'^infs/([1-9][0-9]*)$', views.infs_by_id),
                  url(r'^infs/publish/$', views.infs_publish),

                  url(r'^admiss/$', views.admiss),
                  url(r'^admiss/format/$', views.admissFormat),
                  url(r'^admiss/([1-9][0-9]*)$', views.admiss_by_id),
                  url(r'^admiss/publish/$', views.admiss_publish),

                  url(r'^perevs/$', views.perevs),
                  url(r'^perevs/format/$', views.perevsFormat),
                  url(r'^perevs/([1-9][0-9]*)$', views.perevs_by_id),
                  url(r'^perevs/publish/$', views.perevs_publish),

                  url(r'^obrazs/$', views.obrazs),
                  url(r'^obrazs/format/$', views.obrazsFormat),
                  url(r'^obrazs/([1-9][0-9]*)$', views.obrazs_by_id),
                  url(r'^obrazs/publish/$', views.obrazs_publish),

                  url(r'^practics/$', views.practics),
                  url(r'^practics/format/$', views.practicsFormat),
                  url(r'^practics/([1-9][0-9]*)$', views.practics_by_id),
                  url(r'^practics/publish/$', views.practics_publish),

                  url(r'^sciencs/$', views.sciencs),
                  url(r'^sciencs/format/$', views.sciencsFormat),
                  url(r'^sciencs/([1-9][0-9]*)$', views.sciencs_by_id),
                  url(r'^sciencs/publish/$', views.sciencs_publish),

                  url(r'^SaveFile$', views.SaveFile)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
