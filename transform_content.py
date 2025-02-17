from pathlib import Path
import glob
import summarizer

if __name__ == "__main__":

    files = glob.glob("./storage/topic/*")
    for file in files:
        content_id = file.split("/")[-1].split(".")[0]
        with open(file, "r") as f:
            content = f.read()
        speak_script = summarizer.summarize_contens(f"{content}")
        with open(f"./storage/detail/{content_id}.txt", "w") as f:
            f.write(speak_script)