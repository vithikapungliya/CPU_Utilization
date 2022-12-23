import requests
import psutil

import platform
from pyadl import *


print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")
print(f"Number of physical cores: {psutil.cpu_count(logical=False)}")
print(f"Number of logical cores: {psutil.cpu_count(logical=True)}")
print(f"Platform type: {platform.platform()}")
print(f"Operating system: {platform.system()}")
print(f"Operating system release: {platform.release()}")
print(f"Operating system version: {platform.version()}")
print(f"Computer network name: {platform.node()}")

# devices = ADLManager.getInstance().getDevices()
# # for device in devices:
# #         print("{0}. {1}".format(device.adapterIndex, device.adapterName))
# #         coreVoltageMin, coreVoltageMax = device.getCoreVoltageRange()
# #         print ("\tEngine core voltage: {0} mV ({1} mV - {2} mV)".format(device.getCurrentCoreVoltage(), coreVoltageMin, coreVoltageMax))

# import GPUtil
# GPUtil.showUtilization()
# gpus = GPUtil.getGPUs()
# print(gpus)
# for gpu in gpus:
#     # get the GPU id
#     gpu_id = gpu.id
#     # name of GPU
#     gpu_name = gpu.name
#     print(gpu_name)
import wmi

computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]

os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB
vidRam = abs((gpu_info.AdapterRAM)/1048576)
availGPU = gpu_info.StatusInfo
print(availGPU)

print('OS Name: {0}'.format(os_name))
print('OS Version: {0}'.format(os_version))
print('CPU: {0}'.format(proc_info.Name))
print('RAM: {0} GB'.format(system_ram))
print('Graphics Card: {0}'.format((gpu_info.name)))
print('Graphics Card: {0}'.format(vidRam))

memory = psutil.virtual_memory()
total = round(memory.total/1024.0/1024.0,1)
disk = psutil.disk_usage('/')
totalDisk = round(disk.total/1024.0/1024.0/1024.0,1)
print(f"total:{total}")
print(f"totalDisk:{totalDisk}")
while(True):
    print(f"Current CPU utilization: {psutil.cpu_percent(interval=1)}")
    print(f"Available RAM: {round(psutil.virtual_memory().available/1000000000, 2)} GB")
    #Used RAM
    print(f"Used RAM: {round(psutil.virtual_memory().used/1000000000, 2)} GB")
    #RAM usage
    print(f"RAM usage: {psutil.virtual_memory().percent}%")
    #gpu
    print(f"GPU Usage: {availGPU}")
    print(f"vidRam: {vidRam}")
    

    URL = "http://192.168.1.4:8000/exec"

    PARAMS = {'address':"indiaaa","system":uname.system,"version":uname.version,
    "cpu":psutil.cpu_percent(interval=1),"usedRam":round(psutil.virtual_memory().used/1000000000, 2),
    "avaRam":round(psutil.virtual_memory().available/1000000000, 2),
    "System": uname.system,"NodeName": uname.node,"Release": uname.release,
    "Version": uname.version,"Machine": uname.machine,"Processor": uname.processor,
    "LogicalCore": psutil.cpu_count(logical=True),"PhysicalCore":psutil.cpu_count(logical=False),
    "PlatformType": platform.platform(),"OS": platform.system(),
    "OSrelease": platform.release(), "OSversion":platform.version(),"CN": platform.node(),
    "total":round(memory.total/1024.0/1024.0,1),"totalDisk":round(disk.total/1024.0/1024.0/1024.0,1),
    "vidRam":vidRam}
    # while True:
    r = requests.get(url = URL,params = PARAMS,allow_redirects=True)
    

# data=r.json()
# message=data["message"]
# if "name" in data:
#     name=data["name"]
#     print (f" {message} your name is {name} ")

# else:
#     print(message)