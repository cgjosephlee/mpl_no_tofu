# No Tofu
*Eat all the tofus in your matplotlib plot!*

Download and install Noto fonts to matplotlib library without modifying system fonts. Supports Chinese, Japanese, Korean, and any font in [Google fonts repo](https://github.com/google/fonts/tree/main/ofl). This is useful when using Google Colab and Sagemaker Studio/Notebooks.

[Demo notebook](https://github.com/cgjosephlee/mpl_no_tofu/blob/master/tests/tofu.ipynb).

# Quick guide
## Installation
```
pip install git+https://github.com/cgjosephlee/mpl_no_tofu.git
```

## Load fonts
```python
import matplotlib.pyplot as plt
from mpl_no_tofu import load_fonts
load_fonts()  # default installs "NotoSansTC"
# your plots
```

## Available fonts
- NotoSansTC
- NotoSerifTC
- NotoSansSC
- NotoSerifSC
- NotoSansHK
- NotoSansJP
- NotoSerifJP
- NotoSansKR
- NotoSerifKR

## Install fonts via google fonts `METADATA.pb` file
Find your font in [Google fonts repo](https://github.com/google/fonts/tree/main/ofl) and copy the path of `METADATA.pb`.
```python
load_fonts("https://github.com/google/fonts/raw/main/ofl/notosansthailooped/METADATA.pb")
```

# Similar projects
- https://github.com/Hsins/mpl-tc-fonts
- https://github.com/Clarmy/mplfonts
