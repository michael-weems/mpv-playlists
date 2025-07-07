import json
import os
import sys

import log

def from_directory(name, dir):
	path = _path(name)
	if os.path.isfile(path):
		log.warn(f"playlist already exists: {path}")
		print(f" -> if you would like to replace this playlist, please delete it first")
		print(f" -> resolving to existing playlist at {path}")
		return path

	files = _walk_dir(dir, { "ext": ".mp4"})

	_write(path, files)
	log.verbose(f"playlist written to {path}")

	return path

def _path(name):
	path = name
	if not os.path.isabs(path):
		path = os.path.join(os.getcwd(), path)
	
	_, ext = os.path.splitext(path)
	if not ext == ".m3u":
		path = path + ".m3u"

	return path

def _write(path, list):
	# TODO: exception handling
	with open(path, "w") as file:
		file.write("\n".join(list) + "\n")

def _walk_dir(dir, opts):
	found = []
	for root, _, files in os.walk(dir):
		for file_name in files:
			if "ext" in opts:
				_, ext = os.path.splitext(file_name)
				if not ext == opts["ext"]:
					continue

			full_file_path = os.path.join(root, file_name)
			found.append(full_file_path)

	return found
