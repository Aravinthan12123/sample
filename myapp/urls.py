from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('testing',views.testing,name='testing'),
    path('flex',views.flex,name='flex'),
    path('sample',views.sample,name='sample'),
    path('form',views.form,name='form'),
    path('form_result',views.form_result,name='form_result'),
    path('form-edit/<int:id>',views.form_edit,name='form_edit'),
    path('form-delete/<int:id>',views.form_delete,name='form_delete'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT);