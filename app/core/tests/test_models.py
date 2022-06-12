"""
Test for models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """Test model"""

    def test_create_user_with_email_successful(self):
        email = 'test@fff.com'
        password = '12345'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_enail_normalized(self):
        """Test email is normalized for new users."""
        sample_email = [
            ['test1@ExaMple.com', 'test1@example.com'],
            ['tesT2@Example.com', 'tesT2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
        ]
        for email, expected in sample_email:
            user = get_user_model().objects.create_user(
                email, '12345'
            )
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', '12345')

    def test_create_superuser(self):
        """Test create superuser,"""
        user = get_user_model().objects.create_superuser(
            'test1@example.com',
            '12345',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
