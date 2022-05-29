from library.pixiv.api import pixiv
from library.tool import *
from library.aria import *
from os import listdir,system
from shutil import rmtree
import post
def posterui():
      post.USER,post.PASSWORD,post.SITE=cfg["USER"],cfg["PASSWORD"],cfg["SITE"]
      uncp=list(post.PASSWORD)[0]+"******"
      litelogger.infolog("Login as       |"+Fore.LIGHTGREEN_EX+post.USER)
      litelogger.infolog("Password is    |"+Fore.LIGHTGREEN_EX+uncp)
      litelogger.infolog("Target Site is |"+Fore.LIGHTGREEN_EX+post.SITE)
      print(Fore.LIGHTGREEN_EX+"\n\n###########################")
      for i in listdir("resource/images"):
            print(Fore.LIGHTGREEN_EX+i)
      print(Fore.LIGHTGREEN_EX+"###########################")
      
      schedule=reader.get_schedule("schedule.txt")
      
def downloadui():
      schedule=reader.get_schedule("schedule.txt")
      if cfg["ARIA_ARGV"] == "None":
            customkeylist,customvaulist=None,None
      else:
            customkeylist,customvaulist=[],[]
            for i in cfg["ARIA_ARGV"].split(","):
                  customkeylist.append(i.split(":")[0])
                  customvaulist.append(i.split(":")[1])
      
      for i in schedule:
            litelogger.infolog("remote to "+i)
            illustidlist,titlelist,pagecount,tagslist,userlist=pixiv(i)
            writer.datedir("resource",i)
            for j in ms_arialist(pagecount,illustidlist,titlelist):
                  post_to_aria("resource",i,j["url"],j["out"],customkeylist,customvaulist,cfg["PORT"])
            
      

def archiveui():
      print(Fore.LIGHTGREEN_EX+"\n\n###########################")
      for i in listdir("resource/images"):
            print(Fore.LIGHTGREEN_EX+i)
      print(Fore.LIGHTGREEN_EX+"###########################")
def chosemode():
      modelist=[1,2,3,4,5,6]
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
      if mode==6:
            print(Fore.LIGHTYELLOW_EX+"Are you sure(y/n)—>",end="")
            c=input()
            if c =="y" or c=="yes" or c=="Y":
                  exit()
      if mode==5:
            print(Fore.LIGHTYELLOW_EX+"Are you sure(y/n)—>",end="")
            c=input()
            if c =="y" or c=="yes" or c=="Y":
                  for i in listdir("resource/images"):
                        rmtree("resource/images/"+i)
      if mode==3:
            archiveui()
      if mode==4:
            litelogger.infolog("Pick up config now...")
            cfg=reader.pickupcfg(".setting.txt")
            for i,j in cfg.items():
                  print(Fore.LIGHTWHITE_EX+i,Fore.LIGHTGREEN_EX+j)
            litelogger.infolog("Pick up finished")
      if mode==2:
            posterui()
      if mode==1:
            downloadui()

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
[3]Archive UI
[4]Refresh the config
[5]Make the "resource/images" Empty
[6]Exit

'''
if "resource" not in listdir():
      writer.mkdir("resource")
      writer.mkdir("resource/images")
      writer.mkdir("resource/archives")
      writer.mkdir("resource/temp")


litelogger.colorprint(title,Fore.GREEN)
litelogger.infolog("Pick up config now...")
cfg=reader.pickupcfg(".setting.txt")
litelogger.infolog("Pick up finished")
if cfg["ARIA_LA"]=="True":
      system("Start aria2c --conf-path=./aria2.conf")
while True:
      chosemode()
