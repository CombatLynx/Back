from django.conf.urls import url, include
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
                  url(r'^', include(router.urls)),
                  url(r'^api-auth/', include('rest_framework.urls')),
                  url(r'^login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  url(r'^token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
                  url(r'^token/verify/', TokenVerifyView.as_view(), name='token_verify'),

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
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^basic_informations/$', views.basic_informations),
                  url(r'^basic_informations/format/$', views.basic_informationsFormat),
                  url(r'^basic_informations/([1-9][0-9]*)$', views.basic_informations_by_id),
                  url(r'^basic_informations/publish/$', views.basic_informations_publish),

                  url(r'^founders/$', views.founders),
                  url(r'^founders/format/$', views.foundersFormat),
                  url(r'^founders/([1-9][0-9]*)$', views.founders_by_id),
                  url(r'^founders/publish/$', views.founders_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^filiations/$', views.filiations),
                  url(r'^filiations/format/$', views.filiationsFormat),
                  url(r'^filiations/([1-9][0-9]*)$', views.filiations_by_id),
                  url(r'^filiations/publish/$', views.filiations_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^representations/$', views.representations),
                  url(r'^representations/format/$', views.representationsFormat),
                  url(r'^representations/([1-9][0-9]*)$', views.representations_by_id),
                  url(r'^representations/publish/$', views.representations_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^managements/$', views.managements),
                  url(r'^managements/format/$', views.managementsFormat),
                  url(r'^managements/([1-9][0-9]*)$', views.managements_by_id),
                  url(r'^managements/publish/$', views.managements_publish),

                  url(r'^volumes/$', views.volumes),
                  url(r'^volumes/format/$', views.volumesFormat),
                  url(r'^volumes/([1-9][0-9]*)$', views.volumes_by_id),
                  url(r'^volumes/publish/$', views.volumes_publish),

                  url(r'^rushs/$', views.rushs),
                  url(r'^rushs/format/$', views.rushsFormat),
                  url(r'^rushs/([1-9][0-9]*)$', views.rushs_by_id),
                  url(r'^rushs/publish/$', views.rushs_publish),

                  url(r'^vacs/$', views.vacs),
                  url(r'^vacs/format/$', views.vacsFormat),
                  url(r'^vacs/([1-9][0-9]*)$', views.vacs_by_id),
                  url(r'^vacs/publish/$', views.vacs_publish),
                  # ---------------------------------------------------------
                  url(r'^leaders/$', views.leaders),
                  url(r'^leaders/format/$', views.leadersFormat),
                  url(r'^leaders/([1-9][0-9]*)$', views.leaders_by_id),
                  url(r'^leaders/publish/$', views.leaders_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^leadersTwo/$', views.leadersTwos),
                  url(r'^leadersTwo/format/$', views.leadersTwosFormat),
                  url(r'^leadersTwo/([1-9][0-9]*)$', views.leadersTwos_by_id),
                  url(r'^leadersTwo/publish/$', views.leadersTwos_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^filialLeaders/$', views.filialLeaders),
                  url(r'^filialLeaders/format/$', views.filialLeadersFormat),
                  url(r'^filialLeaders/([1-9][0-9]*)$', views.filialLeaders_by_id),
                  url(r'^filialLeaders/publish/$', views.filialLeaders_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^teachers/$', views.teachers),
                  url(r'^teachers/format/$', views.teachersFormat),
                  url(r'^teachers/([1-9][0-9]*)$', views.teachers_by_id),
                  url(r'^teachers/publish/$', views.teachers_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^standartCopies/$', views.standartCopies),
                  url(r'^standartCopies/format/$', views.standartCopiesFormat),
                  url(r'^standartCopies/([1-9][0-9]*)$', views.standartCopies_by_id),
                  url(r'^standartCopies/publish/$', views.standartCopies_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^standartCopiestwos/$', views.standartCopiestwos),
                  url(r'^standartCopiestwos/format/$', views.standartCopiestwosFormat),
                  url(r'^standartCopiestwos/([1-9][0-9]*)$', views.standartCopiestwos_by_id),
                  url(r'^standartCopiestwos/publish/$', views.standartCopiestwos_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^paidServices/$', views.paidServices),
                  url(r'^paidServices/format/$', views.paidServicesFormat),
                  url(r'^paidServices/([1-9][0-9]*)$', views.paidServices_by_id),
                  url(r'^paidServices/publish/$', views.paidServices_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^plats/$', views.plats),
                  url(r'^plats/format/$', views.platsFormat),
                  url(r'^plats/([1-9][0-9]*)$', views.plats_by_id),
                  url(r'^plats/publish/$', views.plats_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^docas/$', views.docas),
                  url(r'^docas/format/$', views.docasFormat),
                  url(r'^docas/([1-9][0-9]*)$', views.docas_by_id),
                  url(r'^docas/publish/$', views.docas_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^docbs/$', views.docbs),
                  url(r'^docbs/format/$', views.docbsFormat),
                  url(r'^docbs/([1-9][0-9]*)$', views.docbs_by_id),
                  url(r'^docbs/publish/$', views.docbs_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^doccs/$', views.doccs),
                  url(r'^doccs/format/$', views.doccsFormat),
                  url(r'^doccs/([1-9][0-9]*)$', views.doccs_by_id),
                  url(r'^doccs/publish/$', views.doccs_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^docds/$', views.docds),
                  url(r'^docds/format/$', views.docdsFormat),
                  url(r'^docds/([1-9][0-9]*)$', views.docds_by_id),
                  url(r'^docds/publish/$', views.docds_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^doces/$', views.doces),
                  url(r'^doces/format/$', views.docesFormat),
                  url(r'^doces/([1-9][0-9]*)$', views.doces_by_id),
                  url(r'^doces/publish/$', views.doces_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^docfs/$', views.docfs),
                  url(r'^docfs/format/$', views.docfsFormat),
                  url(r'^docfs/([1-9][0-9]*)$', views.docfs_by_id),
                  url(r'^docfs/publish/$', views.docfs_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^docgs/$', views.docgs),
                  url(r'^docgs/format/$', views.docgsFormat),
                  url(r'^docgs/([1-9][0-9]*)$', views.docgs_by_id),
                  url(r'^docgs/publish/$', views.docgs_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^dochs/$', views.dochs),
                  url(r'^dochs/format/$', views.dochsFormat),
                  url(r'^dochs/([1-9][0-9]*)$', views.dochs_by_id),
                  url(r'^dochs/publish/$', views.dochs_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^docis/$', views.docis),
                  url(r'^docis/format/$', views.docisFormat),
                  url(r'^docis/([1-9][0-9]*)$', views.docis_by_id),
                  url(r'^docis/publish/$', views.docis_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^docjs/$', views.docjs),
                  url(r'^docjs/format/$', views.docjsFormat),
                  url(r'^docjs/([1-9][0-9]*)$', views.docjs_by_id),
                  url(r'^docjs/publish/$', views.docjs_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^docks/$', views.docks),
                  url(r'^docks/format/$', views.docksFormat),
                  url(r'^docks/([1-9][0-9]*)$', views.docks_by_id),
                  url(r'^docks/publish/$', views.docks_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^docls/$', views.docls),
                  url(r'^docls/format/$', views.doclsFormat),
                  url(r'^docls/([1-9][0-9]*)$', views.docls_by_id),
                  url(r'^docls/publish/$', views.docls_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^docms/$', views.docms),
                  url(r'^docms/format/$', views.docmsFormat),
                  url(r'^docms/([1-9][0-9]*)$', views.docms_by_id),
                  url(r'^docms/publish/$', views.docms_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^docns/$', views.docns),
                  url(r'^docns/format/$', views.docnsFormat),
                  url(r'^docns/([1-9][0-9]*)$', views.docns_by_id),
                  url(r'^docns/publish/$', views.docns_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^docos/$', views.docos),
                  url(r'^docos/format/$', views.docosFormat),
                  url(r'^docos/([1-9][0-9]*)$', views.docos_by_id),
                  url(r'^docos/publish/$', views.docos_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^docps/$', views.docps),
                  url(r'^docps/format/$', views.docpsFormat),
                  url(r'^docps/([1-9][0-9]*)$', views.docps_by_id),
                  url(r'^docps/publish/$', views.docps_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^internationalDogs/$', views.internationalDogs),
                  url(r'^internationalDogs/format/$', views.internationalDogsFormat),
                  url(r'^internationalDogs/([1-9][0-9]*)$', views.internationalDogs_by_id),
                  url(r'^internationalDogs/publish/$', views.internationalDogs_publish),

                  url(r'^internationalAccrs/$', views.internationalAccrs),
                  url(r'^internationalAccrs/format/$', views.internationalAccrsFormat),
                  url(r'^internationalAccrs/([1-9][0-9]*)$', views.internationalAccrs_by_id),
                  url(r'^internationalAccrs/publish/$', views.internationalAccrs_publish),

                  url(r'^svedenOnes/$', views.svedenOnes),
                  url(r'^svedenOnes/format/$', views.svedenOnesFormat),
                  url(r'^svedenOnes/([1-9][0-9]*)$', views.svedenOnes_by_id),
                  url(r'^svedenOnes/publish/$', views.svedenOnes_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^svedenTwos/$', views.svedenTwos),
                  url(r'^svedenTwos/format/$', views.svedenTwosFormat),
                  url(r'^svedenTwos/([1-9][0-9]*)$', views.svedenTwos_by_id),
                  url(r'^svedenTwos/publish/$', views.svedenTwos_publish),

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
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^grantInfos/$', views.grantInfos),
                  url(r'^grantInfos/format/$', views.grantInfosFormat),
                  url(r'^grantInfos/([1-9][0-9]*)$', views.grantInfos_by_id),
                  url(r'^grantInfos/publish/$', views.grantInfos_publish),

                  url(r'^grantInfoTwos/$', views.grantInfoTwos),
                  url(r'^grantInfoTwos/format/$', views.grantInfoTwosFormat),
                  url(r'^grantInfoTwos/([1-9][0-9]*)$', views.grantInfoTwos_by_id),
                  url(r'^grantInfoTwos/publish/$', views.grantInfoTwos_publish),

                  url(r'^acts/$', views.acts),
                  url(r'^acts/format/$', views.actsFormat),
                  url(r'^acts/([1-9][0-9]*)$', views.acts_by_id),
                  url(r'^acts/publish/$', views.acts_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

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
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^practics/$', views.practics),
                  url(r'^practics/format/$', views.practicsFormat),
                  url(r'^practics/([1-9][0-9]*)$', views.practics_by_id),
                  url(r'^practics/publish/$', views.practics_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^sciencs/$', views.sciencs),
                  url(r'^sciencs/format/$', views.sciencsFormat),
                  url(r'^sciencs/([1-9][0-9]*)$', views.sciencs_by_id),
                  url(r'^sciencs/publish/$', views.sciencs_publish),
                  url(r'^upload-file/$', views.handle_file),
                  url(r'^download-file/(.*)$', views.handle_file),

                  url(r'^svedOrgs/$', views.svedOrgs),
                  url(r'^svedOrgs/format/$', views.svedOrgsFormat),
                  url(r'^svedOrgs/([1-9][0-9]*)$', views.svedOrgs_by_id),
                  url(r'^svedOrgs/publish/$', views.svedOrgs_publish),

                  url(r'^facilits/$', views.facilits),
                  url(r'^facilits/format/$', views.facilitsFormat),
                  url(r'^facilits/([1-9][0-9]*)$', views.facilits_by_id),
                  url(r'^facilits/publish/$', views.facilits_publish),

                  url(r'^objPracts/$', views.objPracts),
                  url(r'^objPracts/format/$', views.objPractsFormat),
                  url(r'^objPracts/([1-9][0-9]*)$', views.objPracts_by_id),
                  url(r'^objPracts/publish/$', views.objPracts_publish),

                  url(r'^librares/$', views.librares),
                  url(r'^librares/format/$', views.libraresFormat),
                  url(r'^librares/([1-9][0-9]*)$', views.librares_by_id),
                  url(r'^librares/publish/$', views.librares_publish),

                  url(r'^sports/$', views.sports),
                  url(r'^sports/format/$', views.sportsFormat),
                  url(r'^sports/([1-9][0-9]*)$', views.sports_by_id),
                  url(r'^sports/publish/$', views.sports_publish),

                  url(r'^meals/$', views.meals),
                  url(r'^meals/format/$', views.mealsFormat),
                  url(r'^meals/([1-9][0-9]*)$', views.meals_by_id),
                  url(r'^meals/publish/$', views.meals_publish),

                  url(r'^healts/$', views.healts),
                  url(r'^healts/format/$', views.healtsFormat),
                  url(r'^healts/([1-9][0-9]*)$', views.healts_by_id),
                  url(r'^healts/publish/$', views.healts_publish),

                  url(r'^ones/$', views.ones),
                  url(r'^ones/format/$', views.onesFormat),
                  url(r'^ones/([1-9][0-9]*)$', views.ones_by_id),
                  url(r'^ones/publish/$', views.ones_publish),

                  url(r'^twos/$', views.twos),
                  url(r'^twos/format/$', views.twosFormat),
                  url(r'^twos/([1-9][0-9]*)$', views.twos_by_id),
                  url(r'^twos/publish/$', views.twos_publish),

                  url(r'^threes/$', views.threes),
                  url(r'^threes/format/$', views.threesFormat),
                  url(r'^threes/([1-9][0-9]*)$', views.threes_by_id),
                  url(r'^threes/publish/$', views.threes_publish),

                  url(r'^fours/$', views.fours),
                  url(r'^fours/format/$', views.foursFormat),
                  url(r'^fours/([1-9][0-9]*)$', views.fours_by_id),
                  url(r'^fours/publish/$', views.fours_publish),

                  url(r'^fives/$', views.fives),
                  url(r'^fives/format/$', views.fivesFormat),
                  url(r'^fives/([1-9][0-9]*)$', views.fives_by_id),
                  url(r'^fives/publish/$', views.fives_publish),

                  url(r'^sixs/$', views.sixs),
                  url(r'^sixs/format/$', views.sixsFormat),
                  url(r'^sixs/([1-9][0-9]*)$', views.sixs_by_id),
                  url(r'^sixs/publish/$', views.sixs_publish),

                  url(r'^sevens/$', views.sevens),
                  url(r'^sevens/format/$', views.sevensFormat),
                  url(r'^sevens/([1-9][0-9]*)$', views.sevens_by_id),
                  url(r'^sevens/publish/$', views.sevens_publish),

                  url(r'^SaveFile$', views.SaveFile)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
