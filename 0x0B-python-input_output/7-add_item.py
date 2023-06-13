#!/usr/bin/python3
"""
7-add_item.py
"""
from sys import argv
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

arg_list = []
if path.isfile(filename):
    arg_list = load_from_json_file(filename)

for a in argv[1:]:
    arg_list.append(a)

save_to_json_file(arg_list, "add_item.json")
