from rest_framework import viewsets
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer


class BreedViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Breed.

    Этот ViewSet предоставляет действия `list`, `create`, `retrieve`, `update` и `destroy` для модели Breed.
    Использует сериализатор BreedSerializer для преобразования данных модели в JSON и обратно.

    Атрибуты:
        queryset (QuerySet): Набор данных, содержащий все объекты Breed из базы данных.
        serializer_class (Serializer): Сериализатор, используемый для преобразования данных модели.
    """
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class DogViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Dog.

    Этот ViewSet предоставляет действия `list`, `create`, `retrieve`, `update` и `destroy` для модели Dog.
    Использует сериализатор DogSerializer для преобразования данных модели в JSON и обратно.

    Атрибуты:
        queryset (QuerySet): Набор данных, содержащий все объекты Dog из базы данных.
        serializer_class (Serializer): Сериализатор, используемый для преобразования данных модели.
    """
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
