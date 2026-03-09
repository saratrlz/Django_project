FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN apt-get update \
    && apt-get install -y gcc g++ unixodbc-dev curl gnupg


COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]