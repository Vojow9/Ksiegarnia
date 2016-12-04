from django.conf.urls import include, url
from django.contrib import admin
from rest import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('sklep.urls')),
    url(r'^books/', views.BookList.as_view()),
    url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)