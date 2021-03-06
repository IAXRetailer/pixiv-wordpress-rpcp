from library.pixiv import *
from library.tool import *
from library.aria import *
from library.archive import *
from os import listdir,system
from shutil import rmtree,copyfile
import post
import random
def posterui():
      if cfg["BEDPOST"] == "True":
            bedpost()
            return
      post.USER,post.PASSWORD,post.SITE=cfg["USER"],cfg["PASSWORD"],cfg["SITE"]
      uncp=list(post.PASSWORD)[0]+"******"
      print(Fore.LIGHTGREEN_EX+"\n\n###########################")
      for i in listdir("resource/images"):
            print(Fore.LIGHTGREEN_EX+i)
      print(Fore.LIGHTGREEN_EX+"###########################")
      #schedule=reader.get_schedule("schedule.txt")
      print(Fore.LIGHTYELLOW_EX+"Chose a date to init post—>",end="")
      postdate=input()
      while postdate not in listdir("resource/images"):
            print(Fore.RED+"No such folder")
            print(Fore.LIGHTYELLOW_EX+"Chose a date to init post—>",end="")
            postdate=input()
      print(Fore.LIGHTGREEN_EX+postdate)
      infomation=open("resource/images/"+postdate+"/index.txt","r",encoding="utf-8").read().splitlines()
      for i in infomation:
            print(Fore.LIGHTGREEN_EX+"    |----"+i.split("|||")[2])
      print(Fore.LIGHTYELLOW_EX+"If you want to detele some illusts,you can do it now and then you should [Enter]",end="")
      input()
      litelogger.infolog("Login as       |"+Fore.LIGHTGREEN_EX+post.USER)
      litelogger.infolog("Password is    |"+Fore.LIGHTGREEN_EX+uncp)
      litelogger.infolog("Target Site is |"+Fore.LIGHTGREEN_EX+post.SITE)
      articletitle=cfg["TITLE"].replace("$[date]",postdate)
      litelogger.infolog("Title is "+Fore.LIGHTGREEN_EX+articletitle)
      listdir("resource/images/"+postdate)
      if cfg["MAX_PICTURE"] !="*":
            localsimgs=random.sample(listdir("resource/images/"+postdate), int(cfg["MAX_PICTURE"]))
      else:
            localsimgs=listdir("resource/images/"+postdate)
      writer.tempdir("resource",postdate)
      for i in localsimgs:
            copyfile("resource/images/"+postdate+"/"+i,"resource/temp/"+postdate+"/"+i)
            litelogger.infolog("copy "+i)
      for i in localsimgs:
            imager.imgzman("resource/temp/"+postdate+"/"+i,int(cfg["MAX_SIZE"]))
      siteimgsurl=[]
      for i in localsimgs:
            siteimgsurl.append(post.postimg("resource/temp/"+postdate+"/"+i)["url"])
            litelogger.infolog("post "+i+" successfully")
      litelogger.infolog("remove temp")
      rmtree("resource/temp/"+postdate)
      Rawtags=[]
      for i in infomation:
            for j in localsimgs:
                  ia=i.split("|||")
                  if ia[2] in j:
                        ib=ia[0].split(",%,")
                        for k in ib:
                              Rawtags.append(k)
      if cfg["MAX_TAG"] !="*" and cfg["MAX_TAG"] != "":
            fintagsl=random.sample(Rawtags, int(cfg["MAX_TAG"]))
      elif cfg["MAX_TAG"] == "":
            fintagsl=[]
      else:
            fintagsl=Rawtags
      print("Write the article content!")
      content=""
      while True:
            writein=input()
            latecontent=content+"\n"+writein
            if writein == "":
                  break
      content=""
      for surll in siteimgsurl:
            content=content+"<img src=\""+str(surll)+"\">\n"
      content=content+latecontent
      categorylist=[]
      pcategory=cfg["CATE"]
      if "," in pcategory:
            categorylist=pcategory.split(",")
      elif pcategory == "":
            categorylist=[]
      else:
            categorylist.append(pcategory)
      litelogger.infolog(str(categorylist))
      post.post_new_article(articletitle,content,categorylist,fintagsl,cfg["STATE"])

def bedpost():
      litelogger.infolog("Attention You have opened the BED_POST Mode")
      post.USER,post.PASSWORD,post.SITE=cfg["USER"],cfg["PASSWORD"],cfg["SITE"]
      uncp=list(post.PASSWORD)[0]+"******"
      print(Fore.LIGHTGREEN_EX+"\n\n###########################")
      for i in listdir("resource/images"):
            print(Fore.LIGHTGREEN_EX+i)
      print(Fore.LIGHTGREEN_EX+"###########################")
      #schedule=reader.get_schedule("schedule.txt")
      print(Fore.LIGHTYELLOW_EX+"Chose a date to init post—>",end="")
      postdate=input()
      while postdate not in listdir("resource/images"):
            print(Fore.RED+"No such folder")
            print(Fore.LIGHTYELLOW_EX+"Chose a date to init post—>",end="")
            postdate=input()
      print(Fore.LIGHTGREEN_EX+postdate)
      rawindex=open("resource/images/"+postdate+"/index.txt","r",encoding="utf-8").read().splitlines()
      for i in rawindex:
            print(Fore.LIGHTGREEN_EX+"    |----"+i.split("|||")[2])
      print(Fore.LIGHTYELLOW_EX+"If you want to detele some illusts,you can do it now and then you should [Enter]",end="")
      input()
      litelogger.infolog("Login as       |"+Fore.LIGHTGREEN_EX+post.USER)
      litelogger.infolog("Password is    |"+Fore.LIGHTGREEN_EX+uncp)
      litelogger.infolog("Target Site is |"+Fore.LIGHTGREEN_EX+post.SITE)
      articletitle=cfg["TITLE"].replace("$[date]",postdate)
      litelogger.infolog("Title is "+Fore.LIGHTGREEN_EX+articletitle)
      tags,pagecont,illustid,titlelist,sample,Rawtags,taglist=[],[],[],[],[],[],[]
      for i in rawindex:
            tags.append(i.split("|||")[0])
            titlelist.append(i.split("|||")[2])
            pagecont.append(i.split("|||")[3])
            illustid.append(i.split("|||")[4])
      for i in ms_arialist(pagecont,illustid,titlelist):
            sample.append(i["url"])
      if cfg["MAX_PICTURE"] != "*":
            finimgs=random.sample(sample,int(cfg["MAX_PICTURE"]))
      else:
            finimgs=sample
      for imgs,illustd in zip(finimgs,illustid):
            if illustd in imgs:
                  Rawtags.append(tags[illustid.index(illustd)])
      for tagg in Rawtags:
            taggg=tagg.split(",%,")
            for tag in taggg:
                  taglist.append(tag)
      if cfg["MAX_TAG"] !="*" and cfg["MAX_TAG"] != "":
            fintagsl=random.sample(taglist, int(cfg["MAX_TAG"]))
      elif cfg["MAX_TAG"] == "":
            fintagsl=[]
      else:
            fintagsl=taglist
      print("Write the article content!")
      content=""
      while True:
            writein=input()
            latecontent=content+"\n"+writein
            if writein=="":
                  break
      for surll in finimgs:
            content=content+"<img src=\""+str(surll)+"\">\n"
      
      content=content+latecontent
      categorylist=[]
      pcategory=cfg["CATE"]
      if "," in pcategory:
            categorylist=pcategory.split(",")
      elif pcategory == "":
            categorylist=[]
      else:
            categorylist.append(pcategory)
      litelogger.infolog(str(categorylist))
      post.post_new_article(articletitle,content,categorylist,fintagsl,cfg["STATE"])
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
            illustidlist,titlelist,pagecount,tagslist,userlist=pixiv(str(i))
            writer.datedir("resource",i)
            with open("resource/images/"+i+"/index.txt","w",encoding="utf-8") as f:
                  for tag,usr,title,count,illust in zip(tagslist,userlist,titlelist,pagecount,illustidlist):
                        taggslist=[]
                        for tagg in tag:
                              taggslist.append(tagg["name"])
                        sorttag=""
                        for fintag in taggslist:
                              if fintag == taggslist[0]:
                                    sorttag=fintag
                              else:
                                    sorttag=sorttag+",%,"+fintag
                        f.write(sorttag+"|||"+usr["name"]+"|||"+title+"|||"+str(count)+"|||"+str(illust)+"\n")
            arialist=ms_arialist(pagecount,illustidlist,titlelist)
            if cfg["OINF"] != "True":
                  for j in arialist:
                        post_to_aria("resource",i,j["url"],j["out"],customkeylist,customvaulist,cfg["PORT"])
            else:
                  litelogger.infolog("Only Information Mod has been opened"+Fore.BLUE+"(.setting.OINF==True)")
            
      

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
            global cfg
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
#print(aria.aria_rpctest(cfg["PORT"]))
if cfg["ARIA_LA"]=="True":
      try:
            aria.aria_rpctest(cfg["PORT"])
      except:
            system("Start aria2c --conf-path=./aria2.conf")
while True:
      chosemode()