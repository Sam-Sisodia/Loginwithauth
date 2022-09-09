"""project URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from accounts import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('course',views.CourseApi_Apiview , basename="Courses")
router.register('chapter',views.Chapter_apiview, basename="chepters")
router.register('assignment',views.Assi_view, basename="assignments")


urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.Loginview.as_view()),
    path('register/',views.registerUsereView.as_view()),
    path('all/',views.all_view.as_view()),
   # path('all/<id>/',views.all_view.as_view()),
    path ('add/', include(router.urls)),
   
    
]















    # path('add/',views.stuaddapiview.as_view()),
    # path('course/',views.CourseApi_Apiview.as_view()),
    # path('chepter/',views.CourseChepterApiview.as_view()),
    # path('Assignment/',views.Assignment_APIview.as_view())
    






