FROM python:3.11

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY ./app /app
RUN ls -la

CMD ["python3", "main.py" ]