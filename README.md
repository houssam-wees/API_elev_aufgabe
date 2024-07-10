# API_elev_aufgabe
implementation of an API that reads elevator data from a csv file, plus analysis of the data



### Prerequisites
- Python 3.9+
- pip

### Install the dependencies:
- pip install -r requirements.txt

## Usage 

- Build and run the container according to the Dockerfile
- Run the Application : uvicorn main:app --reload --port 12345
- Access the API documentation at:
     Swagger UI: `http://127.0.0.1:12345/docs`

- **Request**:
    ```http
    GET /rides_per_day?date_start=2021-05-01&date_end=2021-05-05
    ```
- **Response**:
    ```json
    {
      "rides_per_day": {
        "2021-05-01": 137,
        "2021-05-02": 84,
        "2021-05-03": 161,
        "2021-05-04": 125,
        "2021-05-05": 167
      },