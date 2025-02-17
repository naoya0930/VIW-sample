# VIW-sample
Voice in work - sample project

# セットアップ
- 1. `git clone` してください．
- 2. dockerのホストサーバに`brew install pulseaudio`をインストールします．
- 3. サウンド用のデーモンを起動します．`pulseaudio --load=module-native-protocol-tcp --exit-idle-time=-1 --daemon`
- 4. `summarizer.py`にAPIキーを入力します．
- 5. dockerをビルドします．`docker build . -t viw-image`
- 6. イメージからコンテナを作成します． `docker run --name viw_container -e PULSE_SERVER=docker.for.mac.localhost -v ~/.config/pulse:/root/.config/pulse -itd viw_container`
- 5. `tash.sh`を実行します．`docker exec -it viw_container "sh -c /app/viw-sample/task.sh"`