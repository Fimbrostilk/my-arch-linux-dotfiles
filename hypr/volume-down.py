import subprocess


if subprocess.check_output(['pactl', 'get-default-sink']).decode() == 'alsa_output.usb-Creative_Technology_Ltd_Sound_Blaster_Play__3_YDSB1730322005593N-00.analog-stereo\n':
	card = subprocess.run(
		'aplay -l | grep "Sound Blaster Play! 3"', shell=True, capture_output=True, text=True
	).stdout.split()[1].strip(':')

	subprocess.run(['amixer', '-c', card, 'set', 'Speaker', '2%-'])
else:
	subprocess.run('amixer set Master 2%-', shell=True)
