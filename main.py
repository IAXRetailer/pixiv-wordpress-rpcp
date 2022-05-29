from library.pixiv.api import pixiv
from library.tool import *
from os import listdir
import post
def posterui():
      post.USER,post.PASSWORD,post.SITE=cfg["USER"],cfg["PASSWORD"],cfg["SITE"]
      uncp=list(post.PASSWORD)[0]+"******"+list(post.PASSWORD)[-1]
      litelogger.infolog("Login as       |"+Fore.LIGHTGREEN_EX+post.USER)
      litelogger.infolog("Password is    |"+Fore.LIGHTGREEN_EX+uncp)
      litelogger.infolog("Target Site is |"+Fore.LIGHTGREEN_EX+post.SITE)
def downloadui():
      schedule=reader.get_schedule("schedule.txt")
      for i in schedule:
            illustidlist,titlelist,pagecount,tagslist,userlist=pixiv(i)
            writer.datedir(i)
def chosemode():
      modelist=[1,2,3,4]
      print(Fore.LIGHTMAGENTA_EX+ui)
      while True:
            print(Fore.LIGHTYELLOW_EX+"Chose the mode now—>",end="")
            mode=input()
            try:
                  mode=int(mode)
                  if mode not in modelist:
                        print(Fore.LIGHTRED_EX+"It's not a legal mode!")
                  else:
                        break
                        
            except:
                  print(Fore.LIGHTRED_EX+"It's not a legal mode!")
      if mode==4:
            print(Fore.LIGHTYELLOW_EX+"Are you sure(y/n)—>",end="")
            c=input()
            if c =="y" or c=="yes" or c=="Y":
                  exit()
      if mode==3:
            litelogger.infolog("Pick up config now...")
            cfg=reader.pickupcfg(".setting.txt")
            for i,j in cfg.items():
                  print(Fore.LIGHTWHITE_EX+i,Fore.LIGHTGREEN_EX+j)
            litelogger.infolog("Pick up finished")


title=r'''

      ___                         ___                   
     /  /\          ___          /  /\          ___     
    /  /::\        /  /\        /  /::\        /  /\    
   /  /:/\:\      /  /::\      /  /:/\:\      /  /::\   
  /  /::\ \:\    /  /:/\:\    /  /:/  \:\    /  /:/\:\  
 /__/:/\:\_\:\  /  /::\ \:\  /__/:/ \  \:\  /  /::\ \:\ 
 \__\/~|::\/:/ /__/:/\:\_\:\ \  \:\  \__\/ /__/:/\:\_\:\
    |  |:|::/  \__\/  \:\/:/  \  \:\       \__\/  \:\/:/
    |  |:|\/        \  \::/    \  \:\           \  \::/ 
    |__|:|~          \__\/      \  \:\           \__\/  
     \__\|                       \__\/                  

'''
ui=r'''

[1]Pixiv UI
[2]Post UI
[3]Refresh the config
[4]Exit

'''
if "resource" not in listdir():
      writer.mkdir("resource")
      writer.mkdir("resource/images")
      writer.mkdir("resource/archives")


litelogger.colorprint(title,Fore.GREEN)
litelogger.infolog("Pick up config now...")
cfg=reader.pickupcfg(".setting.txt")
litelogger.infolog("Pick up finished")
while True:
      chosemode()
