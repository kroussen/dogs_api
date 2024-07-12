from rest_framework import status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer


class DogDetail(APIView):
    """
    Получение, обновление или удаление экземпляра собаки.
    """

    def get(self, request, dog_id, format=None):
        """
        Получение собаки по её ID.
        """
        dog = get_object_or_404(Dog, pk=dog_id)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request, dog_id, format=None):
        """
        Обновление данных собаки по её ID.
        """
        dog = get_object_or_404(Dog, pk=dog_id)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, dog_id, format=None):
        """
        Удаление собаки по её ID.
        """
        dog = get_object_or_404(Dog, pk=dog_id)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DogList(APIView):
    """
    Получение списка всех собак или создание новой собаки.
    """

    def get(self, request):
        """
        Получение списка всех собак.
        """
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Создание новой собаки.
        """
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BreedDetail(viewsets.ViewSet):
    """
    Получение, обновление или удаление породы собак.
    """

    def update(self, request, breed_id):
        """
        Обновление данных породы по её ID.
        """
        breed = get_object_or_404(Breed, pk=breed_id)
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, breed_id):
        """
        Получение породы по её ID.
        """
        breed = get_object_or_404(Breed, pk=breed_id)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    def destroy(self, request, breed_id):
        """
        Удаление породы по её ID.
        """
        breed = get_object_or_404(Breed, pk=breed_id)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedList(viewsets.ViewSet):
    """
    Получение списка всех пород или создание новой породы.
    """

    def list(self, request):
        """
        Получение списка всех пород.
        """
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Создание новой породы.
        """
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
