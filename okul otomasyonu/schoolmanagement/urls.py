from django.contrib import admin
from django.urls import path
from school import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name=''),
]