from os import mkdir
from . import litelogger
def datedir(resourcefolder,date):
    try:
        mkdir(resourcefolder+"/images/"+date)
    except:
        litelogger.warnlog("The "+litelogger.cFore.LIGHTRED_EX+date+litelogger.cFore.YELLOW+" folder has existed")
def tempdir(resourcefolder,date):
    try:
        mkdir(resourcefolder+"/temp/"+date)
    except:
        litelogger.warnlog("The "+litelogger.cFore.LIGHTRED_EX+date+litelogger.cFore.YELLOW+" folder has existed")