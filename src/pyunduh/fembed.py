import re
from urllib import request
import json

host = "https://fakyutube.com"

errMsg = {
    "Url": "url does not supported",
    "VideoID": "unable to parse video id",
}

def Fembed(url: str, resolution: str = "720p"):
    params = getParams(url, resolution)
    req = request.Request(**params)
    res = request.urlopen(req)
    return res

def getDefaultHeader() -> dict:
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0",
    }
    return headers

def validateUrl(url: str) -> bool:
    pattern = re.compile(r"(http(s)?\:\/\/)?(www\.)?fembed\.com\/v\/[\w\d\-\_]+")
    return pattern.match(url) != None

def getVideoId(url: str) -> str:
    pattern = re.compile(r"\/v\/([\w\d\-\_]+)")
    matches = pattern.findall(url)
    if matches == None:
        raise Exception(errMsg["VideoID"])
    return matches[0]

def getSources(videoId: str) -> dict:
    url = "{}/api/source/{}".format(host, videoId)

    headers = getDefaultHeader()
    headers["Accept-Encoding"] = "identity"

    req = request.Request(url, method = "POST", headers = headers)
    with request.urlopen(req) as res:
        content = b''.join(res.readlines()).decode('utf-8')
        jsonRes = json.loads(content)

    videos = {}
    for data in jsonRes["data"]:
        resolution = data["label"]
        url = data["file"]
        videos[resolution] = url

    return videos

def getParams(url: str, resolution: str) -> dict:
    if validateUrl(url) == False:
        raise ValueError(errMsg["Url"])
    videoId = getVideoId(url)
    sources = getSources(videoId)
    url = sources[resolution]

    headers = getDefaultHeader()
    params = {
        "method": "GET",
        "url": url,
        "headers": headers,
    }

    return params
