from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index,name='course_index'),
    url(r'^add$', views.add,name='course_add'),
    url(r'^destroy/(?P<number>\d+)$', views.destroy,name='course_destroy'),
    url(r'^remove/(?P<number>\d+)$', views.remove,name='course_remove'),
]