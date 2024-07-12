from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .controllers import DogList, DogDetail, BreedList, BreedDetail

urlpatterns = [
    path('api/dogs/', DogList.as_view(), name='dog-list'),
    path('api/dogs/<int:dog_id>', DogDetail.as_view(), name='dog-detail'),
    path('api/breeds/', BreedList.as_view({'get': 'list', 'post': 'create'}), name='breed-list'),
    path('api/breeds/<int:breed_id>', BreedDetail.as_view({'get': 'retrieve',
                                                           'put': 'update',
                                                           'delete': 'destroy'}), name='breed-detail'),
]
