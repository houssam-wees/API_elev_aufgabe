
FROM python:3.9-slim
WORKDIR /elev_app_fast
COPY . /elev_app_fast
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 12345
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "12345"]
