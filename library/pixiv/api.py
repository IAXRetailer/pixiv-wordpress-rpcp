import json
from requests import get
from library.tool import litelogger
from library.tool.time import getdate
def pixiv(date):
    if date == None:
        adate="date="+getdate()
    else:
        adate="date="+date
    api=r"https://api.acgmx.com/public/ranking?ranking_type=illust&mode=daily&per_page=50&page=1&"+adate
    #print(api)
    illustidlist,titlelist,pagecount,tagslist,userlist=getinfo(api)
    return illustidlist,titlelist,pagecount,tagslist,userlist
def getinfo(api):
    try:
        apitext=get(api).text
    except:
        litelogger.errorlog("404")
        return [],[],[],[],[]
    if apitext == "{\"illusts\":[],\"next_url\":null}":
        litelogger.errorlog("The date not available now")
        return [],[],[],[],[]
    if apitext == "{\"code\":500,\"msg\":\"请求失败\"}" or apitext=="获取失败":
        litelogger.errorlog("Code:500")
        return [],[],[],[],[]
    try:
        rawjson=json.loads(apitext)
    except:
        litelogger.errorlog("Code:404")
        return [],[],[],[],[]
    illustidlist,titlelist,pagecount,tagslist,userlist=[],[],[],[],[]
    for i in rawjson["illusts"]:
        illustidlist.append(i["id"])
        titlelist.append(i["title"])
        pagecount.append(i["page_count"])
        tagslist.append(i["tags"])
        userlist.append(i["user"])
    return illustidlist,titlelist,pagecount,tagslist,userlist