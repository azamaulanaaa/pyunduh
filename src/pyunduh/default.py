from urllib import request
from urllib.parse import quote

def Default(url: str, method: str = "GET"):
    params = getParams(url, method)
    req = request.Request(**params)
    res = request.urlopen(req)
    return res

def getParams(url: str, method: str) -> dict:
    return {
        "url": urlEncoder(url),
        "method": method,
        "headers": {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0",
        },
    }

def urlEncoder(url: str) -> str:
    return quote(url, safe=":/")
