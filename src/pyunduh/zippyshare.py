import re
from typing import Tuple
from urllib import request

errMsg = {
    "Url": "url does not supported",
    "FetchKey": "unable to fetch Key",
    "FetchServerCode": "unable to fetch server code",
    "FetchFileCode": "unable to fetch file code",
}

def Zippyshare(url: str):
    params = getParams(url)
    req = request.Request(**params)
    res = request.urlopen(req)
    return res

def getDefaultHeader() -> dict:
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0",
    }
    return headers

def validateUrl(url: str) -> bool:
    pattern = re.compile(r"(http(s)?\:\/\/)?www[\d]+\.zippyshare\.com\/v\/[\w\d]+\/file\.html")
    return pattern.match(url) != None

def getKeyAndCookies(url: str) -> Tuple[int, str]:
    headers = getDefaultHeader()
    headers["Accept-Encoding"] = "identity"

    req = request.Request(url, method = "GET", headers = headers)
    with request.urlopen(req) as res:
        cookies = res.headers.get_all("Set-Cookie")
        content = b''.join(res.readlines()).decode('utf-8')
    
    pattern = re.compile(r"([\d]+)\s\+\s([\d]+)\s\%\s([\d]+)\)")
    matches = pattern.findall(content)
    if len(matches) == 0:
        raise Exception(errMsg["FetchKey"])
    
    key =  (int(matches[0][1]) % int(matches[0][0])) + (int(matches[0][1]) % int(matches[0][2]))
    return (key, cookies)
  
def getServerCode(url: str) -> str:
    pattern = re.compile(r'www([\d]+)')

    matches = pattern.findall(url)
    if len(matches) == 0:
        raise Exception(errMsg["FetchServerCode"])

    serverCode = matches[0]
    return serverCode

def getFileCode(url: str) -> str:
    pattern = re.compile(r'v\/([\w\d]+)\/')

    match = pattern.findall(url)
    if len(match) == 0:
        raise Exception(errMsg["FechFileCode"])

    fileCode = match[0]
    return fileCode

def getParams(url: str) -> dict:
    if validateUrl(url) == False:
        raise ValueError(errMsg["Url"])

    (keys, cookies) = getKeyAndCookies(url)
    serverCode = getServerCode(url)
    fileCode = getFileCode(url)

    headers = getDefaultHeader()
    headers["Cookie"] = "; ".join([x.split(";")[0] for x in cookies])
    params = {
        "method": "GET",
        "url": "https://www{}.zippyshare.com/d/{}/{}/file".format(serverCode, fileCode, keys),
        "headers": headers,
    }

    return params
