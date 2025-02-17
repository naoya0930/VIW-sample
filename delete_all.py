# storage配下のファイルを全て削除する.
# ディレクトリは残す

import os
import shutil

if __name__ == "__main__":
    try:
        shutil.rmtree("./storage/topic")
        shutil.rmtree("./storage/detail")
        shutil.rmtree("./storage/voice")
    except FileNotFoundError:
        pass
    
    os.mkdir("./storage/topic/")
    os.mkdir("./storage/detail/")
    os.mkdir("./storage/voice/")
    print("done")
