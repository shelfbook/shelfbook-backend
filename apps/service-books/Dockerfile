FROM python:3.10

RUN mkdir /app/
COPY . /app/
WORKDIR /app/

RUN pip install pip==21.3.1
RUN pip install poetry
RUN poetry export --without-hashes -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
