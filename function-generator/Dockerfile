FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN touch /code/main.py
COPY main.py /code/main.py

ARG CODE
COPY code-injector.sh /code/code-injector.sh

#CMD ["uvicorn","main:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["sh", "./code-injector.sh"]
