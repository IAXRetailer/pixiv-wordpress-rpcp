from PIL import Image
import os
def checkimgsize(imgfile,maxsize):
    info=os.stat(imgfile)
    if int(info.st_size) > int(maxsize):
        return True
    else:
        return False
    
def imgzman(imgfile,maxsize):
    while checkimgsize(imgfile,maxsize):
        imga=Image.open(imgfile)
        w,h=imga.sizd
        imgb=imga.esize((int(w/2),int(h/2)),Image.ANTIALIAS)
        imgb.save(imgfile)
        break
