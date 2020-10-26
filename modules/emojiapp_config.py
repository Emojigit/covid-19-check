import os , sys
from configparser import ConfigParser
from pathlib import Path
def get_root(name):
	home = str(Path.home())
	if not os.path.isdir(home+"/.emoji"):
		print("[Warning] Data Dir not found, creating")
		os.mkdir(home+"/.emoji")
	if not os.path.isdir(home+"/.emoji/"+name):
		print("[Warning] Data Sub Dir not found, creating")
		os.mkdir(home+"/.emoji/"+name)
	return home+"/.emoji/"+name

def get_config_dir(name):
	rdir = get_root(name)
	print("[Warning] Config File not found, creating")
	if not os.path.isfile(name+"/config.conf"):
		with open(name+"/config.conf", "w") as fp: 
			pass
	return name+"/config.conf"

def get_config(name,section,item):
	cfg = ConfigParser()
	cdir = get_config_dir(name)
	cfg.read(cdir)
	return cfg.get(section,item)

def set_config(name,section,item,content):
	cfg = ConfigParser()
	cdir = get_config_dir(name)
	cfg.read(cdir)
	cfg.set(section,item,content)
	with open(cdir, 'w') as configfile:
		cfg.write(configfile)
	cfg = ""
	
	
