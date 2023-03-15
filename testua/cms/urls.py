from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('prepare/page', views.prepare_page, name='prepare_page'),
    path('test/page/0', views.test_page, name='test_page'),
    path('test/page/done', views.done_page, name='done_page')
]