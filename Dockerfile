FROM python:3.11.0a6-alpine3.15
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt --no-cache-dir
COPY . /code
EXPOSE 5000
CMD [ "gunicorn", "-b","0.0.0.0:5000",  "app:app"]