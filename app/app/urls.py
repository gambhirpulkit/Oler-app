"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from oler.views import UserViewSet, RideHistoryView, RideRequestView, RideTrackView
from rest_framework import routers

#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'history', RiderHistoryView.as_view(), base_name='history')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^history/(?P<pk>[0-9]+)/$', RideHistoryView.as_view()),
    url(r'^book/', RideRequestView.as_view()),
    url(r'^ride_track/$', RideTrackView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
