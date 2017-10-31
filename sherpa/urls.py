from django.conf.urls import url
from . import views

from accounts.views import (login_view, auth_view, logout_view, invalid_view, loggedin_view)

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details_view),
    url(r'^add', views.add_view, name='add'),
    url(r'^location_list/$', views.location_list_view),
    url(r'^college_list/$', views.category_list_view, {'category' : 'college', 'category_title' : 'Colleges'}),
    url(r'^library_list/$', views.category_list_view, {'category' : 'library', 'category_title' : 'Libraries'}),
    url(r'^industry_list/$', views.category_list_view, {'category' : 'industry', 'category_title' : 'Industries'}),
    url(r'^hotel_list/$', views.category_list_view, {'category' : 'hotel', 'category_title' : 'Hotels'}),
    url(r'^parks_list/$', views.category_list_view, {'category' : 'park', 'category_title' : 'Parks'}),
    url(r'^zoos_list/$', views.category_list_view, {'category' : 'zoo', 'category_title' : 'Zoos'}),
    url(r'^mueseums_list/$', views.category_list_view, {'category' : 'museum', 'category_title' : 'Mueseums'}),
    url(r'^restaurant_list/$', views.category_list_view, {'category' : 'restaurant', 'category_title' : 'Restaurants'}),
    url(r'^malls_list/$', views.category_list_view, {'category' : 'mall', 'category_title' : 'Malls'}),



    # user auth urls
    url(r'^login/$', login_view),
    url(r'^auth/$', auth_view),
    url(r'^logout/$', logout_view),
    url(r'^loggedin/$', loggedin_view),
    url(r'^invalid/$', invalid_view),

]
