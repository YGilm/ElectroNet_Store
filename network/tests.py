from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

User = get_user_model()


class IsActiveStaffPermissionTests(APITestCase):
    def setUp(self):
        # Создаем пользователя, который является активным сотрудником
        self.active_staff_user = User.objects.create_user(
            username="active_staff",
            password="test123",
            is_active=True,
            is_staff=True
        )

        # Создаем пользователя, который является активным, но не сотрудником
        self.active_non_staff_user = User.objects.create_user(
            username="active_non_staff",
            password="test123",
            is_active=True,
            is_staff=False
        )

        # Создаем неактивного пользователя
        self.inactive_user = User.objects.create_user(
            username="inactive",
            password="test123",
            is_active=False,
            is_staff=True
        )

        self.client = APIClient()

    def test_access_for_active_staff_user(self):
        """
        Проверяет, что активный сотрудник имеет доступ к API.
        """
        self.client.force_authenticate(user=self.active_staff_user)
        response = self.client.get('/api/businessunits/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_for_active_non_staff_user(self):
        """
        Проверяет, что активный, но не являющийся сотрудником пользователь, не имеет доступа к API.
        """
        self.client.force_authenticate(user=self.active_non_staff_user)
        response = self.client.get('/api/businessunits/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_access_for_inactive_user(self):
        """
        Проверяет, что неактивный пользователь не имеет доступа к API.
        """
        self.client.force_authenticate(user=self.inactive_user)
        response = self.client.get('/api/businessunits/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_for_unauthenticated_user(self):
        """
        Проверяет, что не аутентифицированным пользователям отказано в доступе.
        """
        response = self.client.get('/api/businessunits/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
