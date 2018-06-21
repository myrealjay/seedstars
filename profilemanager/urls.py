from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
url(r'^$', views.index),
url(r'^list',views.listing, name = 'list'),
url(r'^add',views.add, name = 'add'),
url(r'^admin',admin.site.urls),
url(r'^myprofile', views.myprofile, name='myprofile'),
#url(r'^details/([0-9]+)/$',views.details, name = 'details'),
]