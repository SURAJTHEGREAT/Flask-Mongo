FROM python:2.7-alpine3.7

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "./test-script.py" ]
