from django.test import TestCase
from .models import Hero

class HeroTest(TestCase):
    def test_django (self):
        self.assertTrue 
    
    def test_num_hero(self):
        self.assertEqual(len(Hero.objects.all()), 0)
    
    def test_add_hero(self):
        Hero.objects.create(name='The Flash', description = 'Im The Flash, zOOOO000oooooom')
        self.assertEqual(len(Hero.objects.all()), 1)
