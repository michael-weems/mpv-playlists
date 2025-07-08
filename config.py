import json
import os
import sys

import log
import playlist

# NOTE: use a function instead of a variable so it cannot be mutated
def defaults():
	c = {
		"shuffle": False,
		"fullscreen": False,
		"performance": False,
	}
	return c

def parse_args():

	config_file = ""
	config = defaults()

	argc = len(sys.argv)
	i = 0
	while i < argc:
		if sys.argv[i] == "-v" or sys.argv[i] == "--verbose":
			log._verbose = True
		i = i + 1

	# NOTE: multiple loops fine since arg count is generally small and we want to make sure we get the config file before applying other options on top of it
	i = 0
	while i < argc:
		if sys.argv[i] == "-c" or sys.argv[i] == "--config-file":
			i = i + 1
			config_file = sys.argv[i]
			log.verbose(f"[arg] config-file: {config_file}")
		i = i + 1
	
	if not config_file == "":
		try:
			log.verbose(f"read config from: {config_file}")
			config = _read(config_file)
		except:
			config = defaults()
			log.fail(f"read config file: {config_file}")
			print(f"fallback to using default configuration: {config}")

	directory=""
	out = ""
	list_path=""
	
	i = 1
	# NOTE: get all other options
	while i < argc:
		if sys.argv[i] == "-v" or sys.argv[i] == "--verbose": # NOTE: already processed above
			i = i + 1
			continue
		elif sys.argv[i] == "-c" or sys.argv[i] == "--config-file": # NOTE: already processed above
			i = i + 1
		elif sys.argv[i] == "-o" or sys.argv[i] == "--output":
			i = i + 1
			out = sys.argv[i]
			log.verbose(f"[arg] output config to: {out}")
		elif sys.argv[i] == "--performance":
			config["performance"] = True
			log.verbose(f"[arg] performance: True")
		elif sys.argv[i] == "--shuffle":
			config["shuffle"] = True
			log.verbose(f"[arg] shuffle: True")
		elif sys.argv[i] == "--fullscreen":
			config["fullscreen"] = True
			log.verbose(f"[arg] fullscreen: True")
		elif sys.argv[i] == "-d" or sys.argv[i] == "--from-directory":
			i = i + 1
			directory = sys.argv[i]
			log.verbose(f"[arg] from-directory: {directory}")
		else:
			list_path = sys.argv[i]
			log.verbose(f"[arg] playlist: {list_path}")
		i = i + 1

	log.verbose(f"config: {config}")

	if not directory == "":
		default_name = os.path.basename(os.path.dirname(directory))
		list_path = playlist.from_directory(default_name, directory)
		print(f"using playlist ({list_path}) from directory: {directory}")

	if not out == "":
		if not os.path.isabs(out):
			out = os.path.join(os.getcwd(), out)

		_write(out, config)
		print(f"config saved to {out}")

	if list_path == "":
		raise RuntimeError("no playlist specified, abort.")

	return list_path, config

def _write(file_name, config):
	# TODO: exception handling
	with open(file_name, 'w') as json_file:
		json.dump(config, json_file, indent=4)

def _read(file_path):
	if not os.path.isfile(file_path):
		raise RuntimeError("config file not found")

	# TODO: exception handling
	with open(file_path, 'r') as json_file:
		config = json.load(json_file)
		return config

def build_cmd(playlist, config):
	args = ["mpv"]

	if config["shuffle"]:
		args.append("--shuffle")

	if config["fullscreen"]:
		args.append("--fullscreen")

	if config["performance"]:
		args.append("--profile=fast")

	args.append(playlist)

	return args

