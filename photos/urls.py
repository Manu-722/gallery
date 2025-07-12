from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('upload/', views.upload_view, name='upload'),
    path('photo/<int:photo_id>/', views.detail_view, name='detail'),
    path('tag/<int:tag_id>/', views.filter_view, name='filter'),
    path('photo/<int:photo_id>/favorite/', views.toggle_favorite, name='toggle_favorite'),
]