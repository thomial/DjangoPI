from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^upload/', views.upload_file_csv, name='upload'),
    url(r'^upload/proccess/(?P<id>\d+)/$',views.process_input ,name='proccess'),
]