from pathlib import Path
from voicevox_core import VoicevoxCore, METAS
from openai import OpenAI
import sys, os
import config

openai_api_key = config.OPENAI_API_KEY

core = VoicevoxCore(open_jtalk_dict_dir=Path("./open_jtalk_dic_utf_8-1.11"))
speaker_id = 1

text = input(str)
if not core.is_model_loaded(speaker_id):
    core.load_model(speaker_id)
wave_bytes = core.tts(text, speaker_id)
with open("./output.wav", "wb") as f:
    f.write(wave_bytes)
