from urllib.request import urlopen
from tool import litelogger
import json
def post_to_aria(resourcefolder,date,url,customkeylist,customvaulist,rpcport):
    dicta={'refer': url,'dir':resourcefolder+"/images/"+date}
    for i,j in zip(customkeylist,customvaulist):
        dicta.update({i:j})
    jsonreq = json.dumps({'jsonrpc': '2.0', 'id': 'qwer',
                                'method': 'aria2.addUri',
                                'params': [[url],dicta],
                                }).encode()
    c = urlopen('http://localhost:'+rpcport+'/jsonrpc', jsonreq)
    litelogger.infolog("Send "+url+" to aria")