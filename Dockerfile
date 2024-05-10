# Dockerfile

FROM python:3

RUN apt update && apt upgrade -yq

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./bot.py" ]