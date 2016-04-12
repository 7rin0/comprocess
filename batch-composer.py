#!/usr/bin/python

# Import python modules
import json
import time
import shutil
import subprocess
from pprint import pprint

# Switch directories of both composers
shutil.move('composer.json', 'composer-tmp/composer.json')
shutil.move('composer-tmp/composer-schema.json', 'composer.json')

# Regenerate composer-schema.json
open('composer-tmp/composer-schema.json', 'a').close()

# Get real composer.json
with open('composer-tmp/composer.json') as data_file:
    current_composer = json.load(data_file)

# This only makes sense if exist key require in dictionary
# meaning if our composer has packages to install else skip everything
if 'require' in current_composer:
	# Clone from real composer.json and save an other empty in required packages
    tmp_composer = dict(current_composer)
    del tmp_composer['require']
    print current_composer['require']
    with open('composer.json', 'w') as no_data_file:
    	json.dump(tmp_composer, no_data_file)

    # For each item dictionary require dependency by defined version
    for dependency, version in current_composer['require'].iteritems():
    	requiredDependency = "composer require " + dependency + ":" + version
    	subprocess.Popen(requiredDependency, stdout=subprocess.PIPE, shell=True)
    	time.sleep(600)

# Revert action
shutil.move('composer-tmp/composer.json', 'composer.json')
