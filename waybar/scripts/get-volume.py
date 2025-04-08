import subprocess

print(subprocess.run('amixer -c 0 get Speaker | grep "Front Left:"', shell=True, capture_output=True, text=True).stdout.split()[3])
