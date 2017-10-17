from api.models import *
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
#
#
# ModelsTestCase
class ModelTestCase(TestCase):
    """Test suite for the data model."""

#    def setUp(self):
#        """Define the test client and other test variables."""
#        user = User.objects.create(username="nerd")
#        data_name = "Write world class code"
#        self.data = Data(name=data_name, owner=user)

#        nickname = "breweez"
#        self.nickname = Nickname(nickname=nickname)
#
#        name = "breweez"
#        self.name = Name(name=name)
#
#        self.sniffed = Sniffed(nickname=nickname)
#
#    def test_model_can_create_a_data(self):
#        """Test the data model can create a data."""
#        old_count = Data.objects.count()
#        self.data.save()
#        new_count = Data.objects.count()
#        self.assertNotEqual(old_count, new_count)

# ViewTestCase
#class ViewTestCase(TestCase):
#    """Test suite for the api views."""
#
#    def setUp(self):
#        """Define the test client and other test variables."""
#        self.user = User.objects.create(username="mock")
#        self.client = APIClient()
#        data_name = "Write world class code"
#        self.data = Data(name=data_name, owner=self.user)
#        self.data.save()

#    def test_authorization_is_enforced(self):
#        """Test that the api has user authorization."""
#        new_client = APIClient()
#        res = new_client.get('/datas/', kwargs={'pk': 3}, format="json")
#        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

#    data
#    def test_api_can_create_a_data(self):
#        """Test the api has bucket creation capability."""
#        data_data = {'name': 'Go to Maasai Mara', 'owner':self.user.id}
#        response = self.client.post(
#                                    reverse('create'),
#                                    data_data,
#                                    format="json")
#        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
##
##    def test_api_can_get_a_data(self):
##        """Test the api can get a given data."""
##        data = Data.objects.all()
##        data1 = Data.objects.all()
##        self.assertEqual(data[0], data1[0])
#
##        response = self.client.get(
##                                   reverse('details'),
##                                   kwargs={'pk': data[0].id}, format="json")
##    self.assertEqual(data, data1)
##        self.assertEqual(response.status_code, status.HTTP_200_OK)
##    self.assertContains(response, data)
#
#
##    def test_api_can_update_a_data(self):
##        """Test the api has bucket update capability."""
##        edited_data = {'name':'I will win souls'}
##        self.client = APIClient()
##        response = self.client.put(
##                                   reverse('details', kwargs={'pk': data.id}),
##                                   edited_data, format='json')
##        self.assertEqual(response.status_code, status.HTTP_200_OK)
##
##    def test_api_can_delete_a_data(self):
##        """Test the api has bucket delete capability."""
##        data = Data.objects.all()
##        response = self.client.delete(
##                                      reverse('details', kwargs={'pk': data.id}),
##                                      format='json', follow=True)
##        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)