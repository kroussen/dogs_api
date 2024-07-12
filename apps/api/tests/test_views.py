from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.api.models import Dog, Breed


class DogAPITests(APITestCase):

    def setUp(self):
        self.breed = Breed.objects.create(
            name='Labrador',
            size='Large',
            friendliness=5,
            trainability=4,
            shedding_amount=3,
            exercise_needs=5
        )
        self.dog = Dog.objects.create(
            name='Buddy',
            age=3,
            gender='Male',
            color='Brown',
            favorite_food='Chicken',
            favorite_toy='Ball',
            breed=self.breed
        )

    def test_create_dog(self):
        url = reverse('dog-list')
        data = {
            'name': 'Max',
            'age': 2,
            'gender': 'Male',
            'color': 'Black',
            'favorite_food': 'Beef',
            'favorite_toy': 'Frisbee',
            'breed_id': self.breed.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dog.objects.count(), 2)

    def test_list_dogs(self):
        url = reverse('dog-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_dog(self):
        url = reverse('dog-detail', args=[self.dog.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.dog.name)

    def test_update_dog(self):
        url = reverse('dog-detail', args=[self.dog.id])
        data = {
            'name': 'Buddy',
            'age': 4,
            'gender': 'Male',
            'color': 'Brown',
            'favorite_food': 'Chicken',
            'favorite_toy': 'Ball',
            'breed_id': self.breed.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.dog.refresh_from_db()
        self.assertEqual(self.dog.age, 4)

    def test_delete_dog(self):
        url = reverse('dog-detail', args=[self.dog.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Dog.objects.count(), 0)


class BreedAPITests(APITestCase):

    def setUp(self):
        self.breed = Breed.objects.create(
            name='Labrador',
            size='Large',
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
