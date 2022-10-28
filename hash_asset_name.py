import glob, os
import hashlib

SRC_PATH = "/Users/m1/Desktop/noh/*"
OUT_DIR = "./assets"

for file in glob.glob(SRC_PATH):
    cmd = "cp {} {}/{}.png"
    new_name = hashlib.md5(file.encode('utf-8')).hexdigest()
    print(cmd.format(file, OUT_DIR, new_name))
