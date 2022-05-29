from colorama import Fore,init
from . import time

init(autoreset=True)
cFore=Fore
def gettime():
    time.getdate()
#print log
def infolog(msg):
    print(Fore.GREEN+f"[INFO | {gettime()}] "+Fore.WHITE+msg)

def warnlog(msg):
    print(Fore.YELLOW+f"[WARN | {gettime()}] "+Fore.YELLOW+msg)
    
def errorlog(msg):
    print(Fore.RED+f"[ERROR | {gettime()}] "+Fore.RED+msg)
    
def colorprint(msg,color):
    print(color+msg)