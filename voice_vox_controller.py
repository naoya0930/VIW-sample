import dataclasses
import json
import logging
from argparse import ArgumentParser
from pathlib import Path
from typing import Tuple

import voicevox_core
from voicevox_core import AccelerationMode, AudioQuery, VoicevoxCore

def push_work(text,out,speeker_id):
    acceleration_mode = "CPU"
    open_jtalk_dict_dir = "./open_jtalk_dic_utf_8-1.11"
    core = VoicevoxCore(
        acceleration_mode=acceleration_mode, open_jtalk_dict_dir=open_jtalk_dict_dir
    )
 
    core.load_model(speeker_id)
    audio_query = core.audio_query(text, speeker_id)
    wav = core.synthesis(audio_query, speeker_id)
    
    out.write_bytes(wav)