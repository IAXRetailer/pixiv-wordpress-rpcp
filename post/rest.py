from requests import post
import post as postAPI
import json


def getusertoken():
    
    url=postAPI.SITE+"/wp-json/jwt-auth/v1/token"
    print(url)
    data={
        "username":postAPI.USER,
        "password":postAPI.PASSWORD
            }
    respon=post(url,data=data).text
    try:
        token=json.loads(respon)["token"]
    except:
        print(respon)
    print(token)
    return token
    

def restimgpost(filename):
    API_MEDIA = postAPI.SITE + "/wp-json/wp/v2/media"
    JWT_TOKEN = getusertoken()
    data = open(filename,'rb').read()
    #imgMime = gImageSuffixToMime[imgSuffix] # 'image/png'
    #imgeFilename = "%s.%s" % (processedGuid, imgSuffix) # 'f6956c30ef0b475fa2b99c2f49622e35.png'
    authValue = "Bearer %s" % JWT_TOKEN
    curHeaders = {
        "Authorization": authValue,
        "Content-Type": 'image/jpeg',
        'Content-Disposition': 'picture.jpg',
        }
    #li.info("curHeaders=%s", curHeaders)
        # curHeaders={'Authorization': 'Bearer eyJ0xxxyyy.zzzB4', 'Content-Type': 'image/png', 'Content-Disposition': 'attachment; filename=f6956c30ef0b475fa2b99c2f49622e35.png'}
    uploadImgUrl = API_MEDIA
    resp = post(
            uploadImgUrl,
        # proxies=cfgProxies,
            headers=curHeaders,
            data=data,
        )
def restarticlepost(title,content):
    url=postAPI.SITE+"/wp-json/wp/v2/posts"
    data={
        "title":title,
        "content":content
    }
    print(post(url,data=data).text)