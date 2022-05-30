from . import time
def pickupcfg(target):
    rawlist=open(target,"r",encoding="utf-8").read().splitlines()
    coklist=[]
    cfgdict={}
    for i in rawlist:
        if  "#" in i:
            pass
        else:
            coklist.append(i)
    for i in coklist:
        keyname=i.split("=")[0]
        keyvaule=i.split("=")[1]
        cfgdict.update({keyname:keyvaule})
    return cfgdict

def get_schedule(target):
    schedulelist=open(target,"r").read().splitlines()
    if len(schedulelist)==1 and schedulelist[0] == "None":
        datelist=[]
        datelist.append(time.getdate())
        return datelist
    elif len(schedulelist)==1 and schedulelist[0] != "None":
        if "~" in schedulelist[0]:
            begin,end=schedule_list(schedulelist[0])
            datelist=time.getdatelist(begin,end)
            return datelist
        else:
            return schedulelist
    elif len(schedulelist)!=1:
        schedules=[]
        for i in schedulelist:
            if "~" in i:
                begin,end=schedule_list(i)
                for j in time.getdatelist(begin,end):
                    schedules.append(j)
            else:
                schedules.append(i)
        return schedules
    else:
        datelist=[]
        datelist.append(time.getdate())
        return datelist

def schedule_list(format_string):
    begin,end=format_string.split("~")[0],format_string.split("~")[1]
    begin=begin.split("-")
    end=end.split("-")
    return begin,end