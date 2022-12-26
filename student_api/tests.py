from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Create your tests here.

class Testsample(TestCase):

    def setup(self):
        self.client = APIClient

    def test_index(self):
        url = reverse('student_api:index') #to get url pattern using name attribute
        res = self.client.get(url) #to get response from the curresponding url (here response will be "congratulation, you have created an API")
        #here res.data contains messege "congratulation, you have created an API"
        self.assertEquals(res.data,"congratulation, you have create an API") # assert.equals method compare two strings