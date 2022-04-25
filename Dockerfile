FROM mrismanaziz/man-userbot:buster

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
RUN git clone -b Keyy https://github.com/Keyyasst/KeyyUserbot /home/Keyyuserbot/ \
    && chmod 777 /home/Keyyuserbot \
    && mkdir /home/Keyyuserbot/bin/
WORKDIR /home/Keyyuserbot/
COPY ./sample_config.env ./config.env* /home/Keyyuserbot/
RUN pip install -r requirements.txt
CMD ["python3", "-m", "userbot"]
