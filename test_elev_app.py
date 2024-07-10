import unittest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

class TestFastAPI(unittest.TestCase):

    def test_get_rides_per_day(self):
        response = client.get("/rides_per_day?date_start=2021-05-01&date_end=2021-05-05")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('rides_per_day', data)
        

    def test_get_rides_per_day_invalid_date(self):
        response = client.get("/rides_per_day?date_start=invalid_date&date_end=2021-05-05")
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertEqual(data["detail"], "Invalid date format")

    def test_get_rides_per_day_missing_dates(self):
        response = client.get("/rides_per_day")
        self.assertEqual(response.status_code, 422)  

    def test_hello_world(self):
        response = client.get("/hello")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello, World!"})

if __name__ == '__main__':
    unittest.main()

