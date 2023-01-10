from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for wolfs index
    path('wolfs/', views.wolfs_index, name='index'),
    path('wolfs/<int:wolf_id>/', views.wolfs_detail, name='detail'),
    path('wolfs/create/', views.WolfCreate.as_view(), name='wolfs_create'),
    path('wolfs/<int:pk>/update/', views.WolfUpdate.as_view(), name='wolfs_update'),
    path('wolfs/<int:pk>/delete/', views.WolfDelete.as_view(), name='wolfs_delete'),
    path('wolfs/<int:wolf_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('wolfs/<int:wolf_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
	path('wolfs/<int:wolf_id>/remove_toy/<int:toy_id>/', views.remove_toy, name='remove_toy'),
	path('toys/', views.ToyList.as_view(), name='toys_index'),
	path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
	path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
	path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
	path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('wolfs/<int:wolf_id>/add_photo/', views.add_photo, name='add_photo'),
]

