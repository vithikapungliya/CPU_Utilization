from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from .req import req
from math import ceil
import re

d={}
inp=''
system=''
version=''
cpu=0
l=[]
ram=[]
avaRam =0
usedRam =0
System = 0
NodeName = 0
Release = 0
Version = 0
Machine = 0
Processor = 0
LogicalCore = 0
PhysicalCore = 0
PlatformType = 0
OS = 0
OSrelease = 0
OSversion = 0
CN = 0
total=0
totalDisk=0
vidRam = 0
# Create your views here.

def stat(request):
    return render(request, 'stat.html')

def home(request):
    return render(request, 'pie.html')

def grp(request):
    return render(request, 'graph.html')


# def room(request, room):
#     username = request.GET.get('username')
#     room_details = Room.objects.get(name=room)
#     return render(request, 'room.html', {
#         'username': username,
#         'room': room,
#         'room_details': room_details
#     })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def dis(request):
    d={
    "NodeName":NodeName,
    "Version":Version,
    "Machine":Machine,
    "Processor":Processor,
    "LogicalCore":LogicalCore,
    "PhysicalCore":PhysicalCore,
    "OperatingSystem":OS,
    "Operating System Release":OSrelease,
    "Operating System Version":OSversion,
    "RAM":f"{ceil(float(total)/1024)} GB",
    "Total Disk":f"{totalDisk} GB"}
    return render(request,"static.html",{"d":d})

def execu(request):
    # print(cpu)
    return JsonResponse({"l":l,"ram":ram,"cpu":cpu})

def scrap(request):
    try:
        global total
    # totalDisk = ceil(float(total))
        comp = False
        
        inp = request.POST["requiremts"]
        data,title = req(inp)
        data=data['MINIMUM:']
        ram=data['Memory']
        print(data)
        print(f"{totalDisk} GB")
        total = ceil(float(total)/1024)
        print(f"{total} GB")
        graphics=data['Graphics']
        Storage = data['Storage']
        Storage = re.search(r"[0-9]+", Storage)
        Storage = Storage.group()
        print(graphics)
        a = re.search(r"[0-9]+\s*(MB|GB)", graphics)
        a_val = re.search(r"[0-9]+", a.group())
        a_val= a_val.group()
        if('GB' in a.group()):
            a_val = int(a_val)*1024
        print(type(vidRam),type(a_val))
        print(totalDisk)
        if(total>=int(ram[0]) and float(totalDisk)>=int(Storage) and float(vidRam)>=float(a_val)):
            comp = True
        else:
            comp = -1
        print(comp)
        return render(request, 'stat.html',{"title":title,"data":data,"total":total,"Processor":Processor,"totalDisk":totalDisk,"OS":OS,"a_val":a_val,"vidRam":vidRam,"comp":comp})
    except:
        print('except')
        return render(request,'stat.html',{"total":total,"Processor":Processor,"totalDisk":totalDisk,"OS":OS,"vidRam":vidRam})

def exec(request):
    if request.method == 'GET':    
        global inp,system,version,cpu,avaRam,usedRam,System,NodeName,Release,Version,Machine,Processor,LogicalCore,PhysicalCore,PlatformType,OS,OSrelease,OSversion,CN,total,totalDisk,vidRam   
        inp= request.GET.get('address')
        system=request.GET.get('system')
        version=request.GET.get('version')
        cpu=request.GET.get('cpu')
        avaRam=request.GET.get('avaRam')
        usedRam=request.GET.get('usedRam')
        System = request.GET.get('System')
        NodeName = request.GET.get('NodeName')
        Release = request.GET.get('Release')
        Version = request.GET.get('Version')
        Machine = request.GET.get('Machine')
        Processor = request.GET.get('Processor')
        LogicalCore = request.GET.get('LogicalCore')
        PhysicalCore = request.GET.get('PhysicalCore')
        PlatformType = request.GET.get('PlatformType')
        OS = request.GET.get('OS')
        vidRam = request.GET.get('vidRam')
        OSrelease = request.GET.get('OSrelease')
        OSversion = request.GET.get('OSversion')
        CN = request.GET.get('CN')
        total = request.GET.get('total')
        totalDisk = request.GET.get('totalDisk')
        global l,ram
        
        if(len(l)>10):
            l.pop(0)
        l.append(cpu)
        ram=[avaRam,usedRam]
        # print(l)
        # print(ram)
    return redirect(execu)
