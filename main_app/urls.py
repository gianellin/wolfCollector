from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for cats index
    path('wolfs/', views.wolfs_index, name='index'),
    path('wolfs/<int:wolf_id>/', views.wolfs_detail, name='detail'),
]

