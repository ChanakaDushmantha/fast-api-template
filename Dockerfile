FROM python:3.11.9-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /app/requirements.txt
RUN python3 -m venv /home/app/venv && \
    /home/app/venv/bin/pip install --no-cache-dir -r requirements.txt

COPY ./app /app

RUN mkdir -p /home/vector_store /home/prompt_store && \
    groupadd appgroup && useradd -m -g appgroup appuser && \
    chown -R appuser:appgroup /home/vector_store /home/prompt_store /app

USER appuser

EXPOSE 8000

CMD ["/home/app/venv/bin/python", "main.py"]