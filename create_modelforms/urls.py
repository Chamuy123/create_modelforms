"""
URL configuration for create_modelforms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_topicforms/',insert_topicforms,name='insert_topicforms'),
    path('insert_webpageforms/',insert_webpageforms,name='insert_webpageforms'),
    path('insert_accessrecordforms/',insert_accessrecordforms,name='insert_accessrecordforms'),
]
admin.site.site_header='DJANGO'
admin.site.site_title='E1 batch'
admin.site.index_title='djangosite'

