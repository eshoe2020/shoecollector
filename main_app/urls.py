from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),
 path('about/', views.about, name='about'),
 path('shoes/', views.shoes_index, name='shoes_index'),
 path('shoes/<int:shoe_id>/', views.shoes_detail, name='shoes_detail'),
 path('shoes/create/', views.ShoeCreate.as_view(), name='shoes_create'),
 path('shoes/<int:pk>/delete', views.ShoeDelete.as_view(), name='shoes_delete'),
 path('shoes/<int:pk>/update', views.ShoeUpdate.as_view(), name='shoes_update'),
]