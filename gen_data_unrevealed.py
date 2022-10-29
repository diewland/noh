import json, os, glob, random
from pprint import pprint as pp
 
NAME = "Night of Halloween"
DESC = "A Halloween Mascot for Telling people that i'm Still alive through the night of Halloween in bear market.May the Pumpkin be with you 🎃"
IMG = "https://diewland.github.io/noh/unrevealed.png"
ENGINE = "Jigsaw Engine"

OUTPUT_DIR = "./data_unrevealed"
MAX_SUPPLY = 100

# craft metadata
metadata = {
  "name": "***",
  "description": DESC,
  "image": "***",
  "attributes": [
    #{
    #  "trait_type": "Volume",
    #  "value": "***",
    #},
  ],
  "compiler": ENGINE,
}

# build json + write to file
for id in range(0, MAX_SUPPLY):

    # update data
    metadata["name"] = "{} #{}".format(NAME, id)
    metadata["image"] = IMG

    # debug
    #print(metadata)

    # write file
    with open("./{}/{}.json".format(OUTPUT_DIR, id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
