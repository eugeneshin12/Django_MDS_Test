from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'mds02'
urlpatterns = [
    path('', views.signin, name='signin'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),

    path('signin/index/', views.PJTList.as_view(), name='pjt_list'),
    path('signin/index/<int:pk>', views.PJTDetail.as_view(), name='pjt_detail'),
    #path('signin/index/<str:P_Name>', views.PJTDetailView.as_view(), name='pjt_detail'),

    path('signin/index/mr/', views.MRList.as_view(), name='mr_list'),
    path('signin/index/<P_No>/', views.MRList.as_view(), name='mr_list'),


    path('signin/index/eqt/', views.EQTList.as_view(), name='eqt_list'),
    path('signin/index/<P_No>/<M_No>/', views.EQTList.as_view(), name='eqt_list'),

    #path('<P_No>/<M_No>/update/', views.eqt_update, name='eqt_update'),
    path('signin/index/<P_No>/<M_No>/<E_No>/pds/', views.eqt_pds, name='eqt_pds'),
    path('signin/index/<P_No>/<M_No>/<E_No>/mds/', views.eqt_mds, name='eqt_mds'),
    path('signin/index/<P_No>/<M_No>/<E_No>/mds/form/', views.eqt_mds_form, name='eqt_mds_form'),

    path('pjt/create/', views.PJTCreate.as_view(), name='PJT_create'),
    path('pjt/<int:pk>/update/', views.PJTUpdate.as_view(), name='PJT_update'),
    path('pjt/<int:pk>/delete/', views.PJTDelete.as_view(), name='PJT_delete'),

    path('mr/create/', views.MRCreate.as_view(), name='MR_create'),
    path('mr/<int:pk>/update/', views.MRUpdate.as_view(), name='MR_update'),
    path('mr/<int:pk>/delete/', views.MRDelete.as_view(), name='MR_delete'),

    path('eqt/create/', views.EQTCreate.as_view(), name='EQT_create'),
    path('eqt/<int:pk>/update/', views.EQTUpdate.as_view(), name='EQT_update'),
    path('eqt/<int:pk>/delete/', views.EQTDelete.as_view(), name='EQT_delete'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_change/', auth_views.LoginView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.LoginView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.LoginView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.LoginView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.LoginView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.LoginView.as_view(), name='password_reset_complete'),



    # url(r'^(?P<PJT_No>.+)/$', views.mr, name='mr'),
    # url(r'^(?P<PJT_No>.+)/(?P<MR_No>.+)/$', views.eqt, name='eqt'),
    # url(r'^$', views.pjt, name='pjt'),
    # url(r'^polls/(?P<poll_id>\d+)/$',views.polls),
    # url(r'^candidates/(?P<name>.+)/$', views.candidates),
]