FROM python:3.11-slim

WORKDIR /opt/psi

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y netcat-traditional

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .

RUN pwd
RUN ls

RUN sed -i 's/\r$//g' /opt/psi/entrypoint.sh
RUN chmod +x /opt/psi/entrypoint.sh

COPY . .

ENTRYPOINT [ "/opt/psi/entrypoint.sh" ]