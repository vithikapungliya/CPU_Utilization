print(f"Current per-CPU utilization: {psutil.cpu_percent(interval=1, percpu=True)}")
    # #Total RAM
    # print(f"Total RAM installed: {round(psutil.virtual_memory().total/1000000000, 2)} GB")
    # #Available RAM
    # print(f"Available RAM: {round(psutil.virtual_memory().available/1000000000, 2)} GB")
    # #Used RAM
    # print(f"Used RAM: {round(psutil.virtual_memory().used/1000000000, 2)} GB")
    # #RAM usage
    # print(f"RAM usage: {psutil.virtual_memory().percent}%")