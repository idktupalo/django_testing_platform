from django.urls import path

from . import views

urlpatterns = [
    path('authy/login/', views.login_page, name='login'),
    path('authy/registry/', views.registry_page, name='registry'),
    path('authy/logout/', views.logout_page, name='logout')
]