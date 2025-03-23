"""__INIT__"""

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
ROOT = os.getenv("ROOT")
if not os.path.isdir(f"{ROOT}/data"):
    os.makedirs(f"{ROOT}/data/")
