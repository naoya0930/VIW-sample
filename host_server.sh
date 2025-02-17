# これは、ホスト側のサーバーで実行するスクリプトです。
brew install pulseaudio
pulseaudio --load=module-native-protocol-tcp --exit-idle-time=-1 --daemon
pulseaudio --check -v