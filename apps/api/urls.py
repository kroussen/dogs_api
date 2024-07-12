from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import DogViewSet, BreedViewSet

router = DefaultRouter()
router.register(r'dogs', DogViewSet)
router.register(r'breeds', BreedViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
