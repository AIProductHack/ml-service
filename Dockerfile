FROM python:3.10

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV BYTHONUNBUFFERED 1
ENV PYTHONPATH /usr/src/app

COPY . .

RUN pip install 'poetry==1.5.1'
RUN poetry config virtualenvs.create false

RUN poetry install

# Для Yandex GPT
#ARG YAGPT_SERVICE_ACCOUNT_ID
#ARG YAGPT_PRIVATE_KEY
#ARG YAGPT_KEY_ID
#ENV YAGPT_SERVICE_ACCOUNT_ID=$YAGPT_SERVICE_ACCOUNT_ID
#ENV YAGPT_PRIVATE_KEY=$YAGPT_PRIVATE_KEY
#ENV YAGPT_KEY_ID=$YAGPT_KEY_ID
#
#CMD ["python", "src/main.py"]

# Для GigaChat
#ARG GIGACHAT_AUTHORIZATION_DATA
#ENV GIGACHAT_AUTHORIZATION_DATA=$GIGACHAT_AUTHORIZATION_DATA
#
#RUN wget https://gu-st.ru/content/lending/russian_trusted_root_ca_pem.crt
#RUN wget https://gu-st.ru/content/lending/russian_trusted_sub_ca_pem.crt
#
#CMD ["python", "--ca", "russian_trusted_root_ca_pem.crt", "--ca", "russian_trusted_sub_ca_pem.crt", "src/main.py"]

# Для GigaChat

ARG CHATGPT_API_KEY
ENV CHATGPT_API_KEY=$CHATGPT_API_KEY

CMD ["python", "-u", "src/main.py"]
