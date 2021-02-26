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
    path('shoes/<int:shoe_id>/add_photo/', views.add_photo, name='add_photo'),
    path('shoes/<int:shoe_id>/assoc_replica/<int:replica_id>/', views.assoc_replica, name='assoc_replica'),
    path('shoes/<int:shoe_id>/unassoc_replica/<int:replica_id>/', views.unassoc_replica, name='unassoc_replica'),
    path('replicas/', views.ReplicaList.as_view(), name='replicas_index'),
    path('replicas/create/', views.ReplicaCreate.as_view(), name='replicas_create'),
    path('replicas/<int:pk>/', views.ReplicaDetail.as_view(), name='replicas_detail'),
    path('replicas/<int:pk>/update/', views.ReplicaUpdate.as_view(), name='replicas_update'),
    path('replicas/<int:pk>/delete/', views.ReplicaDelete.as_view(), name='replicas_delete'),
]