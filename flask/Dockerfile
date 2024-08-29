FROM python:3.12-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 5000

CMD ["flask", "run", "--debug", "--host=0.0.0.0", "--port=5000"]
