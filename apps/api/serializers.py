from rest_framework import serializers
from .models import Dog, Breed


class BreedSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Breed.

    Этот сериализатор преобразует объекты модели Breed в JSON формат и обратно.
    Он включает все поля модели Breed.

    Вложенный класс Meta определяет модель и поля для сериализации.

    Атрибуты:
        model (Model): Модель, используемая для сериализации.
        fields (str): Поля, которые должны быть включены в сериализацию. '__all__' означает, что все поля модели
        включены.
    """

    class Meta:
        model = Breed
        fields = '__all__'


class DogSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Dog.

    Этот сериализатор преобразует объекты модели Dog в JSON формат и обратно.
    Он включает поля модели Dog, а также вложенный сериализатор для породы (breed) и поле внешнего ключа (breed_id).

    Атрибуты:
        breed (Serializer): Вложенный сериализатор для отображения данных модели Breed.
        breed_id (PrimaryKeyRelatedField): Поле внешнего ключа для создания или обновления связанного объекта Breed.

    Вложенный класс Meta определяет модель и поля для сериализации.

    Атрибуты:
        model (Model): Модель, используемая для сериализации.
        fields (list): Список полей, которые должны быть включены в сериализацию.
    """
    breed = BreedSerializer(read_only=True)
    breed_id = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all(), source='breed')

    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'gender', 'color', 'favorite_food', 'favorite_toy', 'breed', 'breed_id']
