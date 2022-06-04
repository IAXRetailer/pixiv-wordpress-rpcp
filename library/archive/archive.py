import tarfile
from os import walk,path
def entar(target,origin):
    tar = tarfile.open(target,"w:gz")
    for root,dir,files in walk(origin):
        for file in files:
            fullpath = path.join(root,file)
            tar.add(fullpath)
    tar.close()