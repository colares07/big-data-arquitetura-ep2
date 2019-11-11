FROM colares07/flask 

COPY ./src /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "event-store-api.py" ]