from json import loads as l
from requests import get as g
from pandas.io.json import json_normalize as n
from bs4 import BeautifulSoup as b
from pandas import concat as c

c([n(l(g("https://xkcd.com<id>info.0.json".replace("<id>", link["href"])).text)) for link in b(g("https://xkcd.com/archive/").text).find(id="middleContainer").find_all("a")]).to_pickle("xkcd_metadata.pkl")

