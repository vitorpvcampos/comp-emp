import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('username', 'foo@bar.com', 'password')
    assert User.objects.count() == 1
