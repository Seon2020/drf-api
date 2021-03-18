from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Hits

class HitsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_hits = Hits.objects.create(
            added_by = testuser1,
            title = 'This is a test yo',
            description = 'cannot describe perfection'
        )
        test_hits.save()

    def test_hit_content(self):
        hits = Hits.objects.get(id=1)
        actual_added_by = str(hits.added_by)
        actual_title = str(hits.title)
        actual_description = str(hits.description)
        self.assertEqual(actual_added_by, 'testuser1')
        self.assertEqual(actual_title, 'This is a test yo')
        self.assertEqual(actual_description, 'cannot describe perfection')
