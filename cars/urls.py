from django.urls import path
from .views import CarListView, CarDetailView, CreateCarView, UpdateCarView, DeleteCarView, CarReviewView, CarSearch

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car_list'),
    path('cars/<int:id>/', CarDetailView.as_view(), name='car_detail'),
    path('add_car/', CreateCarView.as_view(), name='car_create'),
    path('add_review/', CarReviewView.as_view(), name='car_review'),
    path('cars/<int:id>/delete', DeleteCarView.as_view(), name='car_delete'),
    path('cars/<int:id>/update', UpdateCarView.as_view(), name='car_update'),
    path('search/', CarSearch.as_view(), name='search')
]
