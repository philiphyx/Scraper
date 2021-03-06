from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)


urlpatterns = [
    # path('',views.index, name='index'),
    # path('',include(router.urls))
    url(r'^$', views.flight_list),
    url(r'^(?P<pk>[0-9]+)$', views.flight_detail),

    url(r'^quotes/$',views.quotesList),
    url(r'^quotes/(?P<pk>[0-9]+)$', views.quotesList),
]