from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest import views
from rest_framework.schemas import get_schema_view
from django.conf import settings

schema_view = get_schema_view(title='Pastebin API')


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('sklep.urls')),
    url(r'^books/$', views.BookList.as_view()),
    url(r'^books/(?P<pk>[0-9]+)$', views.BookDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url('^schema/$', schema_view),



]

urlpatterns += [

    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
