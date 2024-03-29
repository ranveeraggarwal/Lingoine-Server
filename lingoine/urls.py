"""lingoine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import re
import rest_framework_swagger.urls
import rest_framework_swagger
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from account.views import UserViewSet, UserLanguageViewSet, AccountViewSet
from language.views import LanguageViewSet

router = DefaultRouter()

router.register('user_profile', UserViewSet, base_name='user_profile')
router.register('user_language', UserLanguageViewSet, base_name='user_language')
router.register('language', LanguageViewSet, base_name='language')
router.register('accounts', AccountViewSet, base_name='accounts')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-docs/', include(rest_framework_swagger.urls, namespace='api-docs')),
]

# Fail safe! If nginx is down, this might come handy.
urlpatterns += [
    url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), serve,
        kwargs={
            'document_root': settings.STATIC_ROOT,
        }
        ),
    url(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')), serve,
        kwargs={
            'document_root': settings.MEDIA_ROOT,
        }
        ),
]