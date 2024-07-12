# Django REST API для управления собаками и их породами

Этот проект предоставляет REST API для управления информацией о собаках и их породах. API включает модели Dog и Breed, позволяя выполнять CRUD-операции с данными.

## Установка и настройка

1. Клонируйте репозиторий.
2. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```
3. Для конфигурации базы данных используется python-decouple
4. Примените миграции базы данных:
    ```sh
    python manage.py migrate
    ```
5. Запустите сервер разработки:
    ```sh
    python manage.py runserver
    ```

## Модели

### Dog
Представляет информацию о собаке.

- `name`: Имя собаки.
- `age`: Возраст собаки.
- `gender`: Пол собаки.
- `color`: Цвет шерсти собаки.
- `favorite_food`: Любимая еда собаки.
- `favorite_toy`: Любимая игрушка собаки.
- `breed`: Порода собаки (связанная внешним ключом с моделью Breed).

### Breed
Представляет информацию о породе собаки.

- `name`: Название породы.
- `size`: Размер собаки (Tiny, Small, Medium, Large).
- `friendliness`: Уровень дружелюбия породы (от 1 до 5).
- `trainability`: Уровень обучаемости породы (от 1 до 5).
- `shedding_amount`: Уровень линьки породы (от 1 до 5).
- `exercise_needs`: Потребность породы в физических упражнениях (от 1 до 5).

## API Методы

## Breed

### Получить список всех пород

GET /breeds/

Ответ:

```json
[
    {
        "id": 1,
        "name": "Labrador",
        "size": "L",
        "friendliness": 5,
        "trainability": 4,
        "shedding_amount": 3,
        "exercise_needs": 5
    },
    ...
]
```

### Создать новую породу

POST /breeds/

Тело запроса:

```json
{
    "name": "Beagle",
    "size": "M",
    "friendliness": 4,
    "trainability": 3,
    "shedding_amount": 3,
    "exercise_needs": 4
}
```

Ответ:

```json
{
    "id": 2,
    "name": "Beagle",
    "size": "M",
    "friendliness": 4,
    "trainability": 3,
    "shedding_amount": 3,
    "exercise_needs": 4
}
```

### Получить информацию о конкретной породе

GET /breeds/{id}/

Ответ:

```json
{
    "id": 1,
    "name": "Labrador",
    "size": "L",
    "friendliness": 5,
    "trainability": 4,
    "shedding_amount": 3,
    "exercise_needs": 5
}
```

### Обновить информацию о породе

PUT /breeds/{id}/

Тело запроса:

```json
{
    "name": "Golden Retriever",
    "size": "L",
    "friendliness": 5,
    "trainability": 5,
    "shedding_amount": 4,
    "exercise_needs": 4
}
```

Ответ:

```json
{
    "id": 1,
    "name": "Golden Retriever",
    "size": "L",
    "friendliness": 5,
    "trainability": 5,
    "shedding_amount": 4,
    "exercise_needs": 4
}
```

### Удалить породу

DELETE /breeds/{id}/

Ответ:

```204 No Content```

## Dog

### Получить список всех собак
GET /dogs/

Ответ:

```json
[
    {
        "id": 1,
        "name": "Buddy",
        "age": 3,
        "gender": "Male",
        "color": "Yellow",
        "favorite_food": "Chicken",
        "favorite_toy": "Ball",
        "breed": {
            "id": 1,
            "name": "Labrador",
            "size": "L",
            "friendliness": 5,
            "trainability": 4,
            "shedding_amount": 3,
            "exercise_needs": 5
        },
        "breed_id": 1
    },
    ...
]
```

### Создать новую собаку

POST /dogs/

Тело запроса:

```json
{
    "name": "Charlie",
    "age": 2,
    "gender": "Female",
    "color": "Brown",
    "favorite_food": "Beef",
    "favorite_toy": "Frisbee",
    "breed_id": 2
}
```

Ответ:

```json
{
    "id": 2,
    "name": "Charlie",
    "age": 2,
    "gender": "Female",
    "color": "Brown",
    "favorite_food": "Beef",
    "favorite_toy": "Frisbee",
    "breed": {
        "id": 2,
        "name": "Beagle",
        "size": "M",
        "friendliness": 4,
        "trainability": 3,
        "shedding_amount": 3,
        "exercise_needs": 4
    },
    "breed_id": 2
}
```

### Получить информацию о конкретной собаке

GET /dogs/{id}/

Ответ:

```json
{
    "id": 1,
    "name": "Buddy",
    "age": 3,
    "gender": "Male",
    "color": "Yellow",
    "favorite_food": "Chicken",
    "favorite_toy": "Ball",
    "breed": {
        "id": 1,
        "name": "Labrador",
        "size": "L",
        "friendliness": 5,
        "trainability": 4,
        "shedding_amount": 3,
        "exercise_needs": 5
    },
    "breed_id": 1
}
```

### Обновить информацию о собаке

PUT /dogs/{id}/

Тело запроса:

```json
{
    "name": "Max",
    "age": 4,
    "gender": "Male",
    "color": "Black",
    "favorite_food": "Fish",
    "favorite_toy": "Rope",
    "breed_id": 1
}
```
Ответ:

```json

{
    "id": 1,
    "name": "Max",
    "age": 4,
    "gender": "Male",
    "color": "Black",
    "favorite_food": "Fish",
    "favorite_toy": "Rope",
    "breed": {
        "id": 1,
        "name": "Labrador",
        "size": "L",
        "friendliness": 5,
        "trainability": 4,
        "shedding_amount": 3,
        "exercise_needs": 5
    },
    "breed_id": 1
}
```

### Удалить собаку

DELETE /dogs/{id}/

Ответ:

```204 No Content```