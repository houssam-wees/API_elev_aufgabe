from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_get_rides_per_day_valid():
    response = client.get("/rides_per_day?date_start=2021-05-01&date_end=2021-05-05")
    assert response.status_code == 200
    assert response.json() == {
    "rides_per_day": {
        "2021-05-01": 137,
        "2021-05-02": 84,
        "2021-05-03": 161,
        "2021-05-04": 125,
        "2021-05-05": 167
    }
}
    