import json
from requests import get
from library.tool.time import getdate
def pixiv(date):
    if date == None:
        adate="date="+getdate()
    else:
        adate=date
    api=r"https://api.acgmx.com/public/ranking?ranking_type=illust&mode=daily&per_page=50&page=1&"+adate
    illustidlist,titlelist,pagecount,tagslist,userlist=getinfo(api)
    return illustidlist,titlelist,pagecount,tagslist,userlist
def getinfo(api):
    rawjson=json.loads(get(api).text)
    illustidlist,titlelist,pagecount,tagslist,userlist=[],[],[],[],[]
    for i in rawjson["illusts"]:
        illustidlist.append(i["id"])
        titlelist.append(i["title"])
        pagecount.append(i["page_count"])
        tagslist.append(i["tags"])
        userlist.append(i["user"])
    return illustidlist,titlelist,pagecount,tagslist,userlist