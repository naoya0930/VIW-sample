# VIW-sample
Voice in work - sample project

# 記事

# セットアップ
- 1. `git clone` します．
- 2. dockerのホストサーバに`pulseaudio`をインストールします．brewがあれば，`brew install pulseaudio`などでインストール可能です．
- 3. サウンド用のデーモンを起動します．`pulseaudio --load=module-native-protocol-tcp --exit-idle-time=-1 --daemon`
- 4. クローンしたコードの内容の`summarizer.py`にAPIキーを入力します．gemini AI Studioから生成が可能です．
- 5. dockerをビルドします．`docker build . -t viw-image`
- 6. イメージからコンテナを作成します． `docker run --name viw_container -e PULSE_SERVER=docker.for.mac.localhost -v ~/.config/pulse:/root/.config/pulse -itd viw_container`
- 5. `tash.sh`を実行します．`docker exec -it viw_container "sh -c /app/viw-sample/task.sh"`
