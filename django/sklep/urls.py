from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.book_list, name='book_list'),
    url(r'^book/(?P<pk>[0-9a-zA-Z-]+)/$', views.book_detail, name='book_detail'),
    url(r'^authors', views.author_list, name='author_list'),
	url(r'^books', views.book, name='book'),
    url(r'^author/(?P<pk>[0-9a-zA-Z-]+)/$', views.author_detail, name='author_detail'),
    url(r'^zakup/$', views.shop_detail, name='shop_detail'),
    url(r'^add_book',views.add_book, name='add_book'),
    url(r'^add_author',views.add_author, name='add_author'),
    url(r'^cart',views.cart, name="cart"),

]
