
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 12345
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "12345"]
