from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.book_list, name='book_list'),
    url(r'^book/(?P<pk>[0-9]+)/$', views.book_detail, name='book_detail'),
	url(r'^zakup/$', views.shop_detail, name='shop_detail'),

    #user auth urls
    url(r'^accounts/login/$',  'sklep.views.login'),
    url(r'^accounts/auth/$',  'sklep.views.auth_view'),
    url(r'^accounts/logout/$', 'sklep.views.logout'),
    url(r'^accounts/loggedin/$', 'sklep.views.loggedin'),
    url(r'^accounts/invalid/$', 'sklep.views.invalid_login'),
    url(r'^accounts/register/$', 'sklep.views.register_user'),
    url(r'^accounts/register_success/$', 'sklep.views.register_success'),
]