FROM python:3.10-alpine
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . code
WORKDIR /code
EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]