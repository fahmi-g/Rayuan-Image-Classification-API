FROM python:3.9.13-alpine3.16

ENV HOST 0.0.0.0
ENV PORT 80

WORKDIR /app
COPY . .
RUN mkdir images
RUN pip install -r requirements.txt
CMD python main.py