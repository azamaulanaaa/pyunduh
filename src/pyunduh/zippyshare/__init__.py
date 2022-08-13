import re
import os
from urllib import request
from bs4 import BeautifulSoup
import js2py

errMsg = {
    "Url": "url does not supported",
    "Path": "unable to fetch path",
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

def getPath(url: str) -> str:

    headers = getDefaultHeader()
    headers["Accept-Encoding"] = "identity"

    req = request.Request(url, method = "GET", headers = headers)
    with request.urlopen(req) as res:
        content = b''.join(res.readlines()).decode('utf-8')
        soup = BeautifulSoup(content, "html.parser")
    
    scripts = soup.select("script")
    jsscript = None
    for script in scripts:
        if script.get_text().__contains__("dlbutton"):
            jsscript = script.get_text()
            break
    if jsscript == None:
        raise Exception(errMsg["Path"])

    vm = js2py.EvalJs()

    mod_dir = os.path.dirname(os.path.realpath(__file__))
    stub = os.path.join(mod_dir, "stub.js")
    with open(stub) as f:
        vm.execute(f.read())

    vm.execute(jsscript)

    path = vm.document.dlbutton.href
    if path == None:
        raise Exception(errMsg["Path"])

    return path
  
def getServerCode(url: str) -> str:
    pattern = re.compile(r'www([\d]+)')

    matches = pattern.findall(url)
    if len(matches) == 0:
        raise Exception(errMsg["FetchServerCode"])

    serverCode = matches[0]
    return serverCode

def getParams(url: str) -> dict:
    if validateUrl(url) == False:
        raise ValueError(errMsg["Url"])

    serverCode = getServerCode(url)
    path = getPath(url)

    headers = getDefaultHeader()
    params = {
        "method": "GET",
        "url": "https://www{}.zippyshare.com{}".format(serverCode, path),
        "headers": headers,
    }

    return params
