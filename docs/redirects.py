import argparse
import json
import os
from collections import  OrderedDict
import operator
import glob
import itertools
import errno

for f in glob.glob("*.json"):
        with open(f, "r") as infile:
            file = json.load(infile, object_pairs_hook=OrderedDict)
            rules = file['rules']
            for rule in rules:
                old_path = rule['match']
                old_path = old_path['@url']
                old_dir = os.path.dirname(old_path)
                old_file = os.path.basename(old_path)
                new_path = rule['action']
                new_path = new_path['@url']
                new_dir = os.path.dirname(new_path)
                new_file = os.path.basename(new_path)

                if not os.path.exists(os.path.dirname(old_path)):
                    try:
                        os.makedirs(os.path.dirname(old_path))
                    except OSError as exc: # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                
                file = open(old_dir + "/" + old_file, "w")
                file.write("<html>\n")
                file.write("<head>\n")
                file.write("<meta http-equiv='refresh' content='0; url=" + "https://library.tradingtechnologies.com/" + new_path + "'>\n")
                file.write("</head>\n")
                file.write("</html>\n")
                file.close
                