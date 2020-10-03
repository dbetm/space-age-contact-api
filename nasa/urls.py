"""nasa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
from rest_framework import permissions, routers
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from spaceAgeContact.views.user_view import UserViewSet
from spaceAgeContact.views.team_view import TeamViewSet
from spaceAgeContact.views.job_view import JobViewSet
from spaceAgeContact.views.school_view import SchoolViewSet
from spaceAgeContact.views.game_view import GameViewSet
from spaceAgeContact.views.game_topic_view import GameTopicViewSet

admin.site.site_header = "Space Age Control - Admin"
admin.site.site_title = "Space Age Control - Admin"
admin.site.index_title = "Space Age Control - Admin"

router = DefaultRouter()
router.register(r'api/users', UserViewSet, basename='user')
router.register(r'api/teams', TeamViewSet, basename='teams')
router.register(r'api/games', GameViewSet, basename='games')
router.register(r'api/topics', GameTopicViewSet, basename='topics')
router.register(r'api/schools', SchoolViewSet, basename='schools')
router.register(r'api/jobs', JobViewSet, basename='jobs')

schema_view = get_schema_view(
   openapi.Info(
      title="GO Control de Accesos - API",
      default_version='v1',
      description="API para administrar accesos residenciales",
      terms_of_service="",
      contact=openapi.Contact(email="support@mail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', admin.site.urls),
    path(r'', include(router.urls)),
    path('api/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
