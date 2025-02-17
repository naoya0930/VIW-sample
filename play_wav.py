import glob
import pyaudio
import wave
import time

if __name__ == "__main__":
    files = glob.glob("./storage/voice/*")
    for file in files:

        filename = file

        # WAVファイルを読み込む
        wf = wave.open(filename, 'rb')

        # PyAudioの初期化
        p = pyaudio.PyAudio()

        # ストリームを開く
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # 音声データを読み込み、再生
        data = wf.readframes(1024)
        while data != b'':
            stream.write(data)
            data = wf.readframes(1024)

        # ストリームを閉じる
        stream.stop_stream()
        stream.close()

        # PyAudioを終了
        p.terminate()