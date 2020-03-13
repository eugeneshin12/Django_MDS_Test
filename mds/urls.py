from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'mds02'
urlpatterns = [
    path('', views.pjt),
    path('<P_No>/', views.mr, name='mr'),
    path('<P_No>/<M_No>/', views.eqt, name='eqt'),
    # url(r'^(?P<PJT_No>.+)/$', views.mr, name='mr'),
    # url(r'^(?P<PJT_No>.+)/(?P<MR_No>.+)/$', views.eqt, name='eqt'),
    # url(r'^$', views.pjt, name='pjt'),
    # url(r'^polls/(?P<poll_id>\d+)/$',views.polls),
    # url(r'^candidates/(?P<name>.+)/$', views.candidates),
]