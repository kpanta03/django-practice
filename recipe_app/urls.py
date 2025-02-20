# sabai urls haru lai map garna use hunxa.
"""
URL configuration for recipe_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from home.views import *#home lai import gareko
from vege.views import *
urlpatterns = [
    path('',home,name="home"),#home app lai yeta import gareko
    path('about/',about,name="about"),
    path('contact/',contact,name="contact"),

    # path('hello/<str:name>/',practice),

    path('recipes/',recipes,name="recipes"),
    path('delete_recipe/<id>/',delete_recipe,name="delete_recipe"),
    path('update_recipe/<id>/',update_recipe,name="update_recipe"),

    path('login/',login_page,name="login_page"),
    path('logout/',logout_page,name="logout_page"),
    path('register/',register_page,name="register_page"),

     # report card project
    path('students/',get_students,name="get_students"),
    path('see_marks/<student_id>/',see_marks,name="see_marks"),#kina name use garxa vanera yeta sikayo.see_marks ko name change garera aru kei rakhyo vani sab thau ma auto change hunxa bcz of name.

    
    
    path('admin/', admin.site.urls),

]
