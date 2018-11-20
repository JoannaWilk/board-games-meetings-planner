FROM python:3.7-slim
ADD . /my-app
WORKDIR /my-app
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]