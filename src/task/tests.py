# from django.test import TestCase
# import json
# from django.test import Client


# class KeyValueViewTests(TestCase):
#     def test_get_data(self):
#         self.client.post('/values', {"1": "eyakub", "2": "sorkar"})
#         response = self.client.get('/values')
#         self.assertEqual(response.status_code, 200)

#     # def test_get_data_by_keys(self):
#     #     self.client.post('/values', {"1": "eyakub", "2": "sorkar"})
#     #     response = self.client.get('/values', {"keys": "1"})
#     #     self.assertJSONEqual(response.content.decode("utf-8"), {"1": "eyakub"})