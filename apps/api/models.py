from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Dog(models.Model):
    """
        Модель для представления информации о собаке.

        Атрибуты:
        name (str): Имя собаки.
        age (int): Возраст собаки.
        gender (str): Пол собаки.
        color (str): Цвет шерсти собаки.
        favorite_food (str): Любимая еда собаки.
        favorite_toy (str): Любимая игрушка собаки.
        breed (Breed): Порода собаки, связанная внешним ключом с моделью Breed.
    """

    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст',
                              validators=[
                                  MinValueValidator(0)
                              ])
    gender = models.CharField(max_length=10, verbose_name='Пол')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    favorite_food = models.CharField(max_length=100, verbose_name='Любимая еда')
    favorite_toy = models.CharField(max_length=100, verbose_name='Любимая игрушка')
    breed = models.ForeignKey('Breed',
                              on_delete=models.CASCADE,
                              related_name='dogs',
                              verbose_name='Порода')

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'

    def __str__(self):
        return f"{self.name}, {self.age} - {self.breed.name}"


class Breed(models.Model):
    """
        Модель для представления информации о породе собаки.

        Атрибуты:
        name (str): Название породы.
        size (str): Размер собаки, выбираемый из предопределенных значений.
        friendliness (int): Уровень дружелюбия породы, принимающий значения от 1 до 5.
        trainability (int): Уровень обучаемости породы, принимающий значения от 1 до 5.
        shedding_amount (int): Уровень линьки породы, принимающий значения от 1 до 5.
        exercise_needs (int): Потребность породы в физических упражнениях, принимающая значения от 1 до 5.
    """

    SHIRT_SIZES = (
        ('T', 'Tiny'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=100, verbose_name='Название породы')
    size = models.CharField(max_length=1, choices=SHIRT_SIZES, verbose_name='Размер собаки')
    friendliness = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Дружелюбие'
    )
    trainability = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Обучаемость'
    )
    shedding_amount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Линяемость'
    )
    exercise_needs = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Потребность в физических упражнениях'
    )

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"
