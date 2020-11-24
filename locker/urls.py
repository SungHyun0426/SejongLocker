from django.urls import path, re_path
from . import views

app_name = 'LOCKER'
urlpatterns = [
    path('', views.v_index, name='index'),
    re_path(r'^([A-E]{1})/$', views.v_showLockers, name='lockers'),
    re_path(r'^([A-E]{1}\d{2})/$', views.v_showLocker, name='locker'),
]
