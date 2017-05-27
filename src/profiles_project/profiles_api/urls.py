# Django viewset
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from django.conf.urls import url

from . import views

# registriraj router
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name="hello-viewset")

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls)) # django router
]
