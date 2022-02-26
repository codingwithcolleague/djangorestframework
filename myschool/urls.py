"""myschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from email.mime import base
import imp
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from serializerapp.serializers import SongSerializer
# from crudopration.views import studentapi,StudentView
# from functionapiview.views import studentapi
# from classbasedview.views import StudentApi
# from generericapiview.views import (StudentListMixing,StudentCreateMixing
# ,StudentRetriveMixing,StudentUpdateMixing)

from throtllingconcept.views import StuList

from concretclassapiview.views import (StudentListApi,StudentCreateApi,
StudentUpdateApi,StudentRetriveApi)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
from viewsset.views import StudentViewset
# from modelviewset.views import StudentViewsetModel
from authenticated.views import StudentViewsetModel
from rest_framework.authtoken.views import obtain_auth_token
from authenticated.views import CustomAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from throtllingconcept.views import StudentThrotallingViewsetModel
from djangofliter.views import StudentFilterListApi
from serializerapp.views import SingerViewset,SongViewset

router.register('studentapi' , StudentThrotallingViewsetModel, basename='student' )
router.register('singer' , SingerViewset, basename='singer' )
router.register('song' , SongViewset, basename='song' )


urlpatterns = [
    path('admin/', admin.site.urls),
    # # path("getallStudent/" , StudentView.as_view() , name="getallStudent" ),
    # path("getallStudent/" , StudentListMixing.as_view() , name="studentapi"),
    # # path("getallStudent/<int:pk>/" , StudentApi.as_view() , name="studenta")
    # path("createStudent/" , StudentCreateMixing.as_view() , name="create"),
    # path("retrive/<int:pk>" , StudentRetriveMixing.as_view() , name="retrive"),
    # path("update/<int:pk>" , StudentUpdateMixing.as_view() , name="update"),
    # path("studentapi/" , StudentListApi.as_view() , name="studentapi"),
    # path("studentcreateapi/" , StudentCreateApi.as_view() , name="studentapi"),
    # path("studentupdateapi/<int:pk>/" , StudentUpdateApi.as_view() , name="studentupdateapi"),
    # path("studentretriveapi/<int:pk>/" , StudentRetriveApi.as_view() , name="studentretriveapi")
    path("" , include(router.urls)),
    path( "auth/" , include("rest_framework.urls") , name="rest_framework"),
    # path("gettoken/" , obtain_auth_token , name="gettoken" )    
    path("gettoken/" , CustomAuthToken.as_view() , name="gettoken"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view() , name='token_verify'),
    path("stulist/" , StuList.as_view() , name="stulist"),
    path("stulisttttt/" , StudentFilterListApi.as_view() , name='stulisttt' )
]
