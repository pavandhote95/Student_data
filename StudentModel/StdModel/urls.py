from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home),
    path('add',views.add),
    path('addTask',views.addTask),
    path('show',views.show),
    path('delete',views.delete),
    path('update',views.update),
]
