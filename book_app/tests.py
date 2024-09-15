from django.test import TestCase
from .models import Book
from datetime import date
# Create your tests here.
class Firsttestcase(TestCase):
    def setUp(self):
        # Setting up test data before running the test
        Book.objects.create(title="Test Book", author="John Doe", published_date=date(2022, 1, 1))

    def test_equal(self):
        self.assertEqual(1,1)