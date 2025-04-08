#!/usr/bin/env python3
import subprocess
import time
import json
import re

def get_volume(card=1, control="Speaker"):
    try:
        output = subprocess.check_output(["amixer", "-c", str(card), "get", control], text=True)
        match = re.search(r"\[([-+]?\d+\.\d+)dB\]", output)
        if match:
            db_value = float(match.group(1))
            return db_value
    except:
        return None

def print_volume(vol):
    print(json.dumps({
        "text": f"{vol}dB 󰕾",
        "tooltip": "Actual volume",
        "class": "volume"
    }), flush=True)

def main():
    last_vol = None
    while True:
        if subprocess.check_output(['pactl', 'get-default-sink']).decode() == 'alsa_output.usb-Creative_Technology_Ltd_Sound_Blaster_Play__3_YDSB1730322005593N-00.analog-stereo\n':
            vol = get_volume()
        else:
            vol = get_volume(0, 'Master')
        if vol is not None and vol != last_vol:
            print_volume(vol)
            last_vol = vol
        time.sleep(0.1)

if __name__ == "__main__":
    main()

