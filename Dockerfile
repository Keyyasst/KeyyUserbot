FROM mrismanaziz/man-userbot:buster

RUN git clone -b main https://github.com/Keyyasst/KeyyUserbot /home/keyyuserbot/ \
    && chmod 777 /home/keyyuserbot \
    && mkdir /home/keyyuserbot/bin/

COPY ./sample_config.env ./config.env* /home/keyyuserbot/

WORKDIR /home/keyyuserbot/

CMD ["python3", "-m", "userbot"]
