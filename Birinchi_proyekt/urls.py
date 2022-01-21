from django.contrib import admin
from django.urls import path
from H_va_x.views import index,result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('search',result)


]
