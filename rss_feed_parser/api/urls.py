from django.urls import path, re_path, include
from rest_framework import routers
from . views import rssApi, RssApi

router = routers.DefaultRouter()

router.register(r'', RssApi)


urlpatterns = [
    re_path(r'^feedpaser',rssApi.as_view(), name="feedspaser" ),
    path("feedparse/", include(router.urls))
]