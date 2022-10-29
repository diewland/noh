import json, glob, random
from datetime import datetime
from pprint import pprint as pp

NAME = "Night of Halloween"
DESC = "A Halloween Mascot for Telling people that i'm Still alive through the night of Halloween in bear market.May the Pumpkin be with you 🎃"
IMG = "https://diewland.github.io/noh/assets/{}"
ENGINE = "Jigsaw Engine"

SRC_PATH = "./assets/*"
OUTPUT_DIR = "./data_revealed"
MAX_SUPPLY = 100
SHUFFLE_TIME = 99

# extract raw data
raw = []
for file in glob.glob(SRC_PATH):
    raw.append(file.split('/')[-1])

# shuffle
for rnd in range(1, SHUFFLE_TIME+1):
    random.shuffle(raw)

# pick first 100 items
raw = raw[:100]

# build chunk
chunk = []
for id, img_file in enumerate(raw):
    # debug
    #print(id, img_file)

    # template
    metadata = {
      "name": "***",
      "description": DESC,
      "image": "***",
      "attributes": [
        #{
        #  "trait_type": "Scene",
        #  "value": "***",
        #},
      ],
      "compiler": ENGINE,
    }

    # update data
    metadata["name"] = "{} #{}".format(NAME, id)
    metadata["image"] = IMG.format(img_file)

    # add to chunk
    chunk.append(metadata)

#pp(chunk)

# write file
for id, metadata in enumerate(chunk):
    with open("./{}/{}.json".format(OUTPUT_DIR, id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
