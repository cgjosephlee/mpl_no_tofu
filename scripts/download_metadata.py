#!/usr/bin/env python
import os
import json
import urllib.request

with open("mpl_no_tofu/config.json") as f:
    config = json.load(f)

for k, v in config.items():
    u = v["SRC_PREFIX"]
    src = os.path.join(u, "METADATA.pb")
    tgt = f"mpl_no_tofu/assets/{k}/METADATA.pb"
    os.makedirs(os.path.dirname(tgt), exist_ok=True)
    urllib.request.urlretrieve(src, tgt)
