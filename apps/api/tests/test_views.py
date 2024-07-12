import unittest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from apps.api.models import Dog, Breed
from apps.api.serializers import DogSerializer, BreedSerializer


class DogDetailTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.breed = Breed.objects.create(
            name='Golden Retriever',
            size='L',
            friendliness=5,
            trainability=5,
            shedding_amount=4,
            exercise_needs=5
        )
        self.dog = Dog.objects.create(name='Rex', age=5, gender='Male', color='Black', favorite_food='Bone',
                                      favorite_toy='Ball', breed=self.breed)

        self.valid_payload = {
            'name': 'Rexie',
            'age': 6,
            'gender': 'Male',
            'color': 'Brown',
            'favorite_food': 'Chicken',
            'favorite_toy': 'Frisbee',
            'breed_id': self.breed.id
        }
        self.invalid_payload = {
            'name': '',
            'age': 6,
            'gender': 'Male',
            'color': 'Brown',
            'favorite_food': 'Chicken',
            'favorite_toy': 'Frisbee',
            'breed_id': self.breed.id
        }

    def test_get_valid_dog(self):
        response = self.client.get(reverse('dog-detail', kwargs={'dog_id': self.dog.pk}))
        dog = Dog.objects.get(pk=self.dog.pk)
        serializer = DogSerializer(dog)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_dog(self):
        response = self.client.get(reverse('dog-detail', kwargs={'dog_id': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_valid_dog(self):
        response = self.client.put(
            reverse('dog-detail', kwargs={'dog_id': self.dog.pk}),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_dog(self):
        response = self.client.put(
            reverse('dog-detail', kwargs={'dog_id': self.dog.pk}),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_dog(self):
        response = self.client.delete(
            reverse('dog-detail', kwargs={'dog_id': self.dog.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_dog(self):
        response = self.client.delete(
            reverse('dog-detail', kwargs={'dog_id': 999})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class DogListTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.breed = Breed.objects.create(
            name='Golden Retriever',
            size='L',
            friendliness=5,
            trainability=5,
            shedding_amount=4,
            exercise_needs=5
        )
        self.valid_payload = {
            'name': 'Buddy',
            'age': 3,
            'gender': 'Male',
            'color': 'Golden',
            'favorite_food': 'Meat',
            'favorite_toy': 'Stick',
            'breed_id': self.breed.id
        }
        self.invalid_payload = {
            'name': '',
            'age': 3,
            'gender': 'Male',
            'color': 'Golden',
            'favorite_food': 'Meat',
            'favorite_toy': 'Stick',
            'breed_id': self.breed.id
        }

    def test_get_all_dogs(self):
        response = self.client.get(reverse('dog-list'))
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_dog(self):
        response = self.client.post(
            reverse('dog-list'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_dog(self):
        response = self.client.post(
            reverse('dog-list'),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class BreedAPITests(APITestCase):

    def setUp(self):
        self.breed = Breed.objects.create(
            name='Labrador',
            size='L',
            friendliness=5,
            trainability=4,
            shedding_amount=3,
            exercise_needs=5
        )

    def test_create_breed(self):
        url = reverse('breed-list')
        data = {
            'name': 'Golden Retriever',
            'size': 'L',
            'friendliness': 5,
            'trainability': 5,
            'shedding_amount': 4,
            'exercise_needs': 5
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Breed.objects.count(), 2)

    def test_list_breeds(self):
        url = reverse('breed-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_breed(self):
        url = reverse('breed-detail', args=[self.breed.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.breed.name)

    def test_update_breed(self):
        url = reverse('breed-detail', args=[self.breed.id])
        data = {
            'name': 'Labrador',
            'size': 'L',
            'friendliness': 4,
            'trainability': 4,
            'shedding_amount': 3,
            'exercise_needs': 5
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.breed.refresh_from_db()
        self.assertEqual(self.breed.friendliness, 4)

    def test_delete_breed(self):
        url = reverse('breed-detail', args=[self.breed.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Breed.objects.count(), 0)
