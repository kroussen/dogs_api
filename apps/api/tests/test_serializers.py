from django.test import TestCase
from apps.api.models import Dog, Breed
from apps.api.serializers import DogSerializer, BreedSerializer


class BreedSerializerTest(TestCase):

    def setUp(self):
        self.breed_attributes = {
            'name': 'Labrador',
            'size': 'Large',
            'friendliness': 5,
            'trainability': 4,
            'shedding_amount': 3,
            'exercise_needs': 5
        }
        self.breed = Breed.objects.create(**self.breed_attributes)
        self.serializer = BreedSerializer(instance=self.breed)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()),
                         {'id', 'name', 'size', 'friendliness', 'trainability', 'shedding_amount', 'exercise_needs'})

    def test_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.breed_attributes['name'])
        self.assertEqual(data['size'], self.breed_attributes['size'])
        self.assertEqual(data['friendliness'], self.breed_attributes['friendliness'])
        self.assertEqual(data['trainability'], self.breed_attributes['trainability'])
        self.assertEqual(data['shedding_amount'], self.breed_attributes['shedding_amount'])
        self.assertEqual(data['exercise_needs'], self.breed_attributes['exercise_needs'])


class DogSerializerTest(TestCase):

    def setUp(self):
        self.breed = Breed.objects.create(
            name='Labrador',
            size='Large',
            friendliness=5,
            trainability=4,
            shedding_amount=3,
            exercise_needs=5
        )
        self.dog_attributes = {
            'name': 'Buddy',
            'age': 3,
            'gender': 'Male',
            'color': 'Brown',
            'favorite_food': 'Chicken',
            'favorite_toy': 'Ball',
            'breed': self.breed
        }
        self.dog = Dog.objects.create(**self.dog_attributes)
        self.serializer = DogSerializer(instance=self.dog)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()),
                         {'id', 'name', 'age', 'gender', 'color', 'favorite_food', 'favorite_toy', 'breed', 'breed_id'})

    def test_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.dog_attributes['name'])
        self.assertEqual(data['age'], self.dog_attributes['age'])
        self.assertEqual(data['gender'], self.dog_attributes['gender'])
        self.assertEqual(data['color'], self.dog_attributes['color'])
        self.assertEqual(data['favorite_food'], self.dog_attributes['favorite_food'])
        self.assertEqual(data['favorite_toy'], self.dog_attributes['favorite_toy'])
        self.assertEqual(data['breed']['name'], self.breed.name)
