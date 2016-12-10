from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.book_list, name='book_list'),
    url(r'^book/(?P<pk>[0-9a-zA-Z-]+)/$', views.book_detail, name='book_detail'),
	url(r'^zakup/$', views.shop_detail, name='shop_detail'),
]
