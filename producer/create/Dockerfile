FROM colares07/python-queue-flask

COPY ./src /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "create.py" ]