FROM ubuntu:22.04
ENV APP_NAME="vim-sample"

RUN mkdir -p  /app
RUN mkdir -p /var/empty/sshd
RUN mkdir -p /run/sshd

RUN apt update && apt upgrade -y \
    && apt install -y vim git cmake python3-dev python3-pip \
    && apt install -y openssh-server \
    && echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config \
    && echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config \
    && echo 'root:root' | chpasswd \
    && apt install -y chromium-browser chromium-chromedriver \
    && apt clean

RUN apt install -y portaudio19-dev
RUN apt install -y python3-gst-1.0
RUN apt install -y pulseaudio

# SSH ポートを公開
EXPOSE 22
COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

### gitでcloneなどする．今回はローカルをコピーする
COPY ./ /app/${APP_NAME}

WORKDIR /app/${APP_NAME}

RUN mkdir -p /app/${APP_NAME}/storage
RUN mkdir -p /app/${APP_NAME}/storage/topic
RUN mkdir -p /app/${APP_NAME}/storage/detail
RUN mkdir -p /app/${APP_NAME}/storage/voice

RUN pip install --upgrade pip
RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install pandas
RUN pip install selenium
RUN pip install tdqm
RUN pip install lxml
RUN pip install datetime
RUN pip install matplotlib
RUN pip install boto3
RUN pip install -q -U google-generativeai
RUN pip install pyaudio

## NOTE: ライセンスの確認をしてください
RUN wget https://github.com/VOICEVOX/voicevox_core/releases/download/0.14.3/voicevox_core-0.14.3+cpu-cp38-abi3-linux_x86_64.whl
RUN pip install voicevox_core-0.14.3+cpu-cp38-abi3-linux_x86_64.whl
## NOTE: ライセンスの確認をしてください
RUN wget https://github.com/microsoft/onnxruntime/releases/download/v1.13.1/onnxruntime-linux-x64-1.13.1.tgz
RUN tar xvzf onnxruntime-linux-x64-1.13.1.tgz
RUN mv onnxruntime-linux-x64-1.13.1/lib/libonnxruntime.so.1.13.1 ./
## NOTE: ライセンスの確認をしてください
RUN wget http://downloads.sourceforge.net/open-jtalk/open_jtalk_dic_utf_8-1.11.tar.gz
RUN tar xvzf open_jtalk_dic_utf_8-1.11.tar.gz
