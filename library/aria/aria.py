from urllib.request import urlopen
from tool import litelogger
import json
def post_to_aria(resourcefolder,date,url,out,customkeylist,customvaulist,rpcport):
    dicta={'refer': url,'dir':resourcefolder+"/images/"+date,"out":out}
    if customvaulist!=None and customkeylist!=None:
        for i,j in zip(customkeylist,customvaulist):
            dicta.update({i:j})
    jsonreq = json.dumps({'jsonrpc': '2.0', 'id': 'qwer',
                                'method': 'aria2.addUri',
                                'params': [[url],dicta],
                                }).encode()
    c = urlopen('http://localhost:'+rpcport+'/jsonrpc', jsonreq)
    litelogger.infolog("Send "+url+" to aria")

def ms_arialist(pagecont,illustid,titlelist):
    arialist=[]
    for page,pid,title in zip(pagecont,illustid,titlelist):
        if int(page) == 1:
            arialist.append({"url":"https://pixiv.re/"+pid+".jpg","out":title})
        else:
            for pagenum in range(1,int(page)+1):
                arialist.append({"url":"https://pixiv.re/"+pid+"-"+pagenum+".jpg","out":title+" "+pagenum})
    return arialist