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

    url(r'^accounts/register/$', views.register_user, name='sklep.views.register_user'),
    url(r'^accounts/register_success/$', views.register_success, name='sklep.views.register_success'),

    url(r'^accounts/login/', views.login_user, name='login_user'),
    url(r'^accounts/logout/', views.logout_user, name='logout_user'),
    url(r'^accounts/auth', views.auth_user, name='auth_user'),
    url(r'^new_cart/', views.new_cart, name='new_cart'),
    url(r'^book/add/(?P<pk>[0-9a-zA-Z-]+)$', views.add_to_cart, name='add_to_cart'),
    url(r'^book/remove/(?P<pk>[0-9a-zA-Z-]+)$', views.remove_from_cart, name='remove_from_cart'),
    url(r'^checkout/', views.checkout, name='checkout'),
    url(r'^mybooks/', views.mybooks, name='mybooks'),
]
