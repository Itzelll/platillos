FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /platillos
WORKDIR /platillos
COPY requirements.txt /platillos/
RUN pip install -r requirements.txt 
COPY . /platillos/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080