import re
from urllib.parse import urlparse

def extract_features(url):
    return [
        len(url),                 # 1 URL length
        url.count('.'),            # 2 dots
        url.count('-'),            # 3 hyphens
        url.count('@'),            # 4 @ symbol
        url.count('?'),            # 5 ?
        url.count('='),            # 6 =
        1 if url.startswith("https") else 0  # 7 https
    ]
