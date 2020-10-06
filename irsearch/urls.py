from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.display, name='index'),
    path('<int:id>/', views.test, name = 'test'),
    path('ketqua/', views.index_result, name = 'result'),
]