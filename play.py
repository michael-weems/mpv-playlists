import os
import subprocess

import log
import config # our module

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)

playlist, c = config.parse_args()

log.verbose(f"playlist: {playlist}")
log.verbose(f"config: {c}")

try:
	cmd = config.build_cmd(playlist, c)
	log.verbose(f"run shell command: {cmd}")
	subprocess.run(cmd)
except KeyboardInterrupt:
	print("Cancelled")
except subprocess.CalledProcessError as e:
    print(f"Subprocess failed with error: {e}")
