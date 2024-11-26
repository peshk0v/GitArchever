import os
import tomllib
import json

def load(filename, mode):
    if mode == 1:
        return tomllib.load(open(filename, "rb"))
    elif mode == 2:
        return json.load(open(filename, "r"))
    else:
        return False

def jsDump(filename, object):
    json.dump(object, open(filename, "w"))

def fRead(fileName):
    with open(fileName, "r") as f:
        return f.read()

def fReadLines(fileName):
    with open(fileName, "r") as f:
        return f.readlines()

def fWrite(fileName, text):
    with open(fileName, "w") as f:
        f.write(text)

