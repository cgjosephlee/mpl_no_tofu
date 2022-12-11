from google.protobuf import text_format
from . import fonts_public_pb2
import urllib.request
import os
import json
import matplotlib
import matplotlib.font_manager
from typing import List

MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
METADATA_FILE = "METADATA.pb"
MPL_DATA = matplotlib.get_data_path()
MPL_FONT = os.path.join(MPL_DATA, "fonts/ttf")

def load_config(file=os.path.join(MODULE_PATH, "config.json")):
    with open(file) as f:
        config = json.load(f)
    return config

def load_metadata(path):
    """
    :path: Can be url or local path.
    """
    if path.startswith("https"):
        resp = urllib.request.urlopen(path)
        data = resp.read().decode()
    else:
        with open(path) as f:
            data = f.read()
    msg = text_format.Parse(data, fonts_public_pb2.FamilyProto(), allow_unknown_field=True)
    return msg

def download_fonts(filenames: List[str], src: str, dest: str, force: bool=False):
    for f in filenames:
        source = os.path.join(src, f)
        target = os.path.join(dest, f)
        if not os.path.exists(target) and not force:
            r = urllib.request.urlretrieve(source, target)

def mpl_add_fonts(filenames: List[str], dest: str):
    for f in filenames:
        matplotlib.font_manager.fontManager.addfont(os.path.join(dest, f))

def mpl_set_fonts(name):
    tmp = matplotlib.rcParams['font.sans-serif']
    if name not in tmp:
        matplotlib.rcParams['font.sans-serif'] = [name] + tmp
    matplotlib.rcParams['axes.unicode_minus'] = False

def mpl_current_fonts():
    return matplotlib.rcParams['font.sans-serif']

def load_fonts(name: str="NotoSansTC", force: bool=False):
    """
    Download and laod fonts for matplotlib.
    
    :name: Can be font name defined in config, or an url of "METADATA.pd".
    :force: Force re-download and overwrite fonts.
    """
    config = load_config()
    if name in config.keys():
        SRC_PREFIX = config[name]["SRC_PREFIX"]
        METADATA_PATH = os.path.join(MODULE_PATH, "assets", name, METADATA_FILE)
    elif name.startswith("https") and name.endswith(METADATA_FILE):
        METADATA_PATH = name
        SRC_PREFIX = os.path.dirname(METADATA_PATH)
    else:
        raise ValueError(f"Not supported format: \"{name}\".")
    msg = load_metadata(METADATA_PATH)
    filenames = [x.filename for x in msg.fonts]
    download_fonts(filenames, SRC_PREFIX, MPL_FONT, force=force)
    mpl_add_fonts(filenames, MPL_FONT)
    mpl_set_fonts(msg.name)
    return

def eat_tofu(tofu="NotoSansTC", *kwargs):
    load_fonts(name=tofu, *kwargs)
