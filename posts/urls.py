from django.conf.urls import url
from django.contrib import admin
from marianamendezsiteapp import views
from . import views #. means from all

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    #?P = parameter; <id> specifies id parameter; \d means its a digit(number); + means at least one or more digits
]
