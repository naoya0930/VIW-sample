from pathlib import Path
import glob
import voice_vox_controller

if __name__ == "__main__":
    files = glob.glob("./storage/detail/*")
    for file in files:
        content_id = file.split("/")[-1].split(".")[0]
        wav_file = Path(f"./storage/voice/{content_id}.wav")
        with open(f"./storage/detail/{content_id}.txt", "r") as f:
            content_detail = f.read()
            voice_vox_controller.push_work(f"{content_detail}",wav_file,8)