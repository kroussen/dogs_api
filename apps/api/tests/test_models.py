from django.core.exceptions import ValidationError
from django.test import TestCase
from apps.api.models import Dog, Breed


class TestDogModel(TestCase):
    """
    Тесты для модели Dog.
    """

    def setUp(self):
        """
        Устанавливает тестовые данные для тестов.
        """
        self.breed = Breed.objects.create(
            name='Labrador',
            size='L',
            friendliness=5,
            trainability=5,
            shedding_amount=3,
            exercise_needs=4
        )

        self.dog = Dog.objects.create(
            name='Buddy',
            age=3,
            gender='Male',
            color='Black',
            favorite_food='Bones',
            favorite_toy='Ball',
            breed=self.breed
        )

    def test_dog_creation(self):
        """
        Тест создания объекта Dog.
        """
        self.assertEqual(self.dog.name, 'Buddy')
        self.assertEqual(self.dog.age, 3)
        self.assertEqual(self.dog.gender, 'Male')
        self.assertEqual(self.dog.color, 'Black')
        self.assertEqual(self.dog.favorite_food, 'Bones')
        self.assertEqual(self.dog.favorite_toy, 'Ball')
        self.assertEqual(self.dog.breed.name, 'Labrador')

    def test_dog_str_method(self):
        """
        Тест строкового представления объекта Dog.
        """
        self.assertEqual(str(self.dog), 'Buddy, 3 - Labrador')

    def test_valid_dog(self):
        """
        Тест валидации корректного объекта Dog.
        """
        dog = Dog.objects.create(
            name='Buddy',
            age=3,
            gender='Male',
            color='Black',
            favorite_food='Bones',
            favorite_toy='Ball',
            breed=self.breed
        )
        dog.full_clean()  # Должен пройти без ошибок

    def test_invalid_dog_gender(self):
        """
        Тест валидации объекта Dog с некорректным значением gender.
        """
        dog = Dog(
            name='Buddy',
            age=3,
            gender='',
            color='Black',
            favorite_food='Bones',
            favorite_toy='Ball',
            breed=self.breed
        )
        with self.assertRaises(ValidationError):
            dog.full_clean()  # Должен выбросить ValidationError

    def test_negative_age(self):
        """
        Тест валидации объекта Dog с отрицательным значением age.
        """
        dog = Dog(
            name='Buddy',
            age=-5,
            gender='Male',
            color='Black',
            favorite_food='Bones',
            favorite_toy='Ball',
            breed=self.breed
        )
        with self.assertRaises(ValidationError):
            dog.full_clean()  # Должен выбросить ValidationError


class TestBreedModel(TestCase):
    """
    Тесты для модели Breed.
    """

    def setUp(self):
        """
        Устанавливает тестовые данные для тестов.
        """
        self.breed = Breed.objects.create(
            name='Labrador',
            size='L',
            friendliness=5,
            trainability=5,
            shedding_amount=3,
            exercise_needs=4
        )

    def test_valid_breed(self):
        """
        Тест валидации корректного объекта Breed.
        """
        self.breed.full_clean()  # Должен пройти без ошибок

    def test_invalid_breed_size(self):
        """
        Тест валидации объекта Breed с некорректным значением size.
        """
        breed = Breed(
            name='Labrador',
            size='XXL',
            friendliness=5,
            trainability=5,
            shedding_amount=3,
            exercise_needs=4
        )
        with self.assertRaises(ValidationError):
            breed.full_clean()  # Должен выбросить ValidationError

    def test_invalid_breed_friendliness(self):
        """
        Тест валидации объекта Breed с некорректным значением friendliness.
        """
        breed = Breed(
            name='Labrador',
            size='L',
            friendliness=6,
            trainability=5,
            shedding_amount=3,
            exercise_needs=4
        )
        with self.assertRaises(ValidationError):
            breed.full_clean()  # Должен выбросить ValidationError

    def test_invalid_breed_trainability(self):
        """
        Тест валидации объекта Breed с некорректным значением trainability.
        """
        breed = Breed(
            name='Labrador',
            size='L',
            friendliness=5,
            trainability=6,
            shedding_amount=3,
            exercise_needs=4
        )
        with self.assertRaises(ValidationError):
            breed.full_clean()  # Должен выбросить ValidationError

    def test_invalid_breed_shedding_amount(self):
        """
        Тест валидации объекта Breed с некорректным значением shedding_amount.
        """
        breed = Breed(
            name='Labrador',
            size='L',
            friendliness=5,
            trainability=5,
            shedding_amount=6,
            exercise_needs=4
        )
        with self.assertRaises(ValidationError):
            breed.full_clean()  # Должен выбросить ValidationError

    def test_invalid_breed_exercise_needs(self):
        """
        Тест валидации объекта Breed с некорректным значением exercise_needs.
        """
        breed = Breed(
            name='Labrador',
            size='L',
            friendliness=5,
            trainability=5,
            shedding_amount=5,
            exercise_needs=6
        )
        with self.assertRaises(ValidationError):
            breed.full_clean()  # Должен выбросить ValidationError
