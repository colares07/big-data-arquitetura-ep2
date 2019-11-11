FROM colares07/python-queue

COPY ./src /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "event-store.py" ]