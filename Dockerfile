FROM mrismanaziz/man-userbot:buster

RUN git clone -b main https://github.com/Keyyasst/KeyyUserbot /home/KeyyUserbot/ \
    && chmod 777 /home/KeyyUserbot \
    && mkdir /home/KeyyUserbot/bin/

COPY ./sample_config.env ./config.env* /home/KeyyUserbot/

WORKDIR /home/KeyyUserbot/

CMD ["python3", "-m", "userbot"]
