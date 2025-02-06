from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Breed(models.Model):
    '''
    Модель для описания породы собаки.

    Attributes:
        name(str): Название породы.
        size(str): Размер породы(Tiny, Small, Medium, Large).
        friendless(int): Дружелюбность(от 1 до 5)
        trainability(int): Обучаемость(от 1 до 5)
        shedding_amount(int): Кол-во линяющей шерсти(от 1 до 5)
        exrcise_needs(int): Потребность в физических нагрузках(от 1 до 5)
    '''
    SIZE_CHOICES = [
    ('Tiny', 'Очень маленькая'),
    ('Small', 'Маленькая'),
    ('Medium', 'Средняя'),
    ('Large', 'Большая'),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    friendless = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    shedding_amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    exercise_needs = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name
    

class Dog(models.Model):
    """Модель для описания собаки.

    Attributes:
        name (str): Имя собаки.
        age (int): Возраст собаки.
        breed (Breed): Порода собаки (внешний ключ).
        gender (str): Пол собаки.
        color (str): Окрас собаки.
        favorite_food (str): Любимая еда.
        favorite_toy (str): Любимая игрушка.
    """
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='dogs')
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    favorite_food = models.CharField(max_length=100)
    favorite_toy = models.CharField(max_length=100)

    def __str__(self):
        return self.name