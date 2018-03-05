"""
amigoInvisible URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.authtoken import views as v
from rest_framework import routers
from app.api import ParticipantEntry

admin.autodiscover()
router = routers.SimpleRouter()

router.register(r'participant', ParticipantEntry)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls, namespace='api')),
]
