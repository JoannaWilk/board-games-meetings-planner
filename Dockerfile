FROM python:3.7-slim
ADD . /my-app
WORKDIR /my-app
COPY .  /my-app
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver"]