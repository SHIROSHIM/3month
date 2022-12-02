FROM python:3.10

EXPOSE 6785

RUN mkdir /parcer
WORKDIR /parcer

COPY . /parcer

RUN pip install -r requirements.txt

CMD ["python", "/parcer/parcer.py",  "/parcer/tg_bot.py"]