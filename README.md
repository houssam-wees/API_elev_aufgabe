# API_elev_aufgabe
implementation of an API that reads elevator data from a csv file, plus analysis of the data



### Prerequisites
- Python 3.9+
- pip

### If you want to Install the dependencies locally:
- pip install -r requirements.txt

## Usage 

- to use the app pull the docker container with the command:
- docker pull houssamwees/app_docker_2
- Access the API documentation at:
     Swagger UI: `http://0.0.0.0:12345/docs`
- run the docker container with the command:  
   docker run -p 12345:12345 houssamwees/app_docker_2:latest


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

- 